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
        print("\n\033[33mPress SPACE to start recording...\033[0m")
        keyboard.wait('space')
        print("\033[31mRecording... Press SPACE again to stop\033[0m")
        
        audio_data = []
        recorded_frames = 0
        max_frames = int(max_duration * samplerate)
        
        def callback(indata, frames, time, status):
            if status:
                print(f"Status: {status}")
            
            float_data = indata.astype(np.float32)
            
            rms = np.sqrt(np.mean(float_data**2))
            
            if rms > threshold:
                gate_mask = abs(float_data) > (threshold * 0.5)
                processed_data = float_data * gate_mask
                
                audio_data.extend(processed_data.astype(np.int16))
            
            nonlocal recorded_frames
            recorded_frames += len(indata)
            if recorded_frames >= max_frames:
                raise sd.CallbackStop()
        
        try:
            stream = sd.InputStream(
                samplerate=samplerate,
                channels=1,
                dtype=np.int16,
                callback=callback,
                blocksize=1024,
                latency='low'
            )
            
            with stream:
                keyboard.wait('space')
            
            if len(audio_data) < samplerate:
                print("Recording too short or no audio detected")
                return None
            
            audio_array = np.array(audio_data)
            
            amplitude_threshold = threshold * np.iinfo(np.int16).max
            noise_mask = abs(audio_array) < amplitude_threshold
            audio_array[noise_mask] = 0
            
            non_zero = np.nonzero(audio_array)[0]
            if len(non_zero) > 0:
                audio_array = audio_array[non_zero[0]:non_zero[-1]]
            
            temp_wav = tempfile.NamedTemporaryFile(delete=False, suffix=".wav")
            wav.write(temp_wav.name, samplerate, audio_array)
            
            print(f"\033[33mRecording saved ({len(audio_array)/samplerate:.1f} seconds)\033[30m")
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