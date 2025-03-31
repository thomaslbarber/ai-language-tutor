import sys
import os
from config import Config
from handlers.whisper_handler import WhisperHandler
from handlers.chatgpt_handler import ChatGPTHandler
from handlers.tts_handler import TTSHandler
from audio.audio_manager import AudioManager
from models.conversation import Conversation

if sys.stdout.encoding != 'utf-8':
    sys.stdout.reconfigure(encoding='utf-8')

os.environ["PYTHONIOENCODING"] = "utf-8"

class ChineseLanguageTutor:
    def __init__(self):
        self.whisper = WhisperHandler(Config.API_KEY)
        self.chatgpt = ChatGPTHandler(Config.API_KEY)
        self.tts = TTSHandler(Config.API_KEY)
        self.audio = AudioManager()
        self.conversation = Conversation(Config.TUTOR_BEHAVIOUR)

    def run(self):
        print("Press Ctrl+C to exit")
        response = self.chatgpt.get_response(self.conversation)
        print("Converting response to speech...")
        audio_content = self.tts.text_to_speech(response)
        if audio_content:
            self.audio.play_audio(audio_content)
        while True:
            try:
                print("\nReady for new conversation...")
                audio_file = self.audio.record_audio()
                if not audio_file:
                    continue

                print("Processing speech to text...")
                transcript = self.whisper.transcribe_audio(audio_file)
                if not transcript:
                    print("Audio transcript is empty - skipping...")
                    continue

                print(f"You said: {transcript}")
                print("Is this correct? (y/n)")

                while True:
                    user_input = input().strip().lower()
                    if user_input in ['y', 'n']:
                        break
                    print("Please enter 'y' for yes or 'n' for no:")
                
                if user_input == 'n':
                    print("Discarding incorrect transcription...")
                    continue


                self.conversation.add_message("user", transcript)
                print("Getting AI response...")
                response = self.chatgpt.get_response(self.conversation)
                if not response:
                    continue

                print("Converting response to speech...")
                audio_content = self.tts.text_to_speech(response)
                if audio_content:
                    self.audio.play_audio(audio_content)

            except KeyboardInterrupt:
                print("\nExiting program...")
                break
            except Exception as e:
                print(f"Error: {str(e)}")
                continue

def main():
    if not Config.API_KEY:
        print("Error: OPENAI_API_KEY environment variable not set")
        sys.exit(1)
        
    tutor = ChineseLanguageTutor()
    tutor.run()

if __name__ == "__main__":
    main()