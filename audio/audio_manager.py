from typing import Optional
import numpy as np
import sounddevice as sd
import scipy.io.wavfile as wav
import keyboard
import tempfile
import os
import pygame
import time
from config import Config

class AudioManager:
    @staticmethod
    def record_audio(max_duration: int = Config.MAX_DURATION, 
                    samplerate: int = Config.SAMPLE_RATE,
                    threshold: float = 0.0003) -> Optional[str]:
        """Records audio with improved noise reduction and input validation.
        
        Args:
            max_duration: Maximum recording duration in seconds
            samplerate: Audio sample rate (Hz)
            threshold: Amplitude threshold for noise gate (0.0 to 1.0)
        """
        print("\nPress SPACE to start recording...")
        keyboard.wait('space')
        print("Recording... Press SPACE again to stop")
        
        audio_data = []
        recorded_frames = 0
        max_frames = int(max_duration * samplerate)
        
        def callback(indata, frames, time, status):
            if status:
                print(f"Status: {status}")
            
            # Convert to float32 for calculations
            float_data = indata.astype(np.float32)
            
            # Calculate RMS amplitude
            rms = np.sqrt(np.mean(float_data**2))
            
            # Noise gate with hysteresis
            if rms > threshold:
                # Apply noise gate
                gate_mask = abs(float_data) > (threshold * 0.5)
                processed_data = float_data * gate_mask
                
                # Convert back to int16 for storage
                audio_data.extend(processed_data.astype(np.int16))
            
            nonlocal recorded_frames
            recorded_frames += len(indata)
            if recorded_frames >= max_frames:
                raise sd.CallbackStop()
        
        try:
            # Configure input stream
            stream = sd.InputStream(
                samplerate=samplerate,
                channels=1,
                dtype=np.int16,
                callback=callback,
                blocksize=1024,  # Smaller blocks for better responsiveness
                latency='low'    # Lower latency for better timing
            )
            
            with stream:
                keyboard.wait('space')  # Wait for stop signal
            
            if len(audio_data) < samplerate:  # Less than 1 second of audio
                print("Recording too short or no audio detected")
                return None
            
            # Convert to numpy array and apply final processing
            audio_array = np.array(audio_data)
            
            # Additional noise reduction
            amplitude_threshold = threshold * np.iinfo(np.int16).max
            noise_mask = abs(audio_array) < amplitude_threshold
            audio_array[noise_mask] = 0
            
            # Trim silence from start and end
            non_zero = np.nonzero(audio_array)[0]
            if len(non_zero) > 0:
                audio_array = audio_array[non_zero[0]:non_zero[-1]]
            
            # Save to temporary file
            temp_wav = tempfile.NamedTemporaryFile(delete=False, suffix=".wav")
            wav.write(temp_wav.name, samplerate, audio_array)
            
            print(f"Recording saved ({len(audio_array)/samplerate:.1f} seconds)")
            return temp_wav.name
            
        except Exception as e:
            print(f"Recording error: {str(e)}")
            return None
            
    @staticmethod
    def play_audio(audio_content: bytes) -> bool:
        temp_path = os.path.join(os.path.dirname(__file__), Config.TEMP_AUDIO_FILE)
        try:
            with open(temp_path, "wb") as f:
                f.write(audio_content)

            pygame.mixer.init()
            pygame.mixer.music.load(temp_path)
            pygame.mixer.music.play()

            while pygame.mixer.music.get_busy():
                pygame.time.Clock().tick(10)

            pygame.mixer.music.stop()
            pygame.mixer.music.unload()
            pygame.mixer.quit()
            return True

        except Exception as e:
            print(f"Audio playback error: {e}")
            return False
        finally:
            if os.path.exists(temp_path):
                time.sleep(0.5)
                try:
                    os.remove(temp_path)
                except Exception as e:
                    print(f"Error removing temp file: {e}")