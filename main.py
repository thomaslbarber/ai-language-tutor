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

class LanguageTutor:
    SUPPORTED_LANGUAGES = {
        '1': {'name': 'Mandarin Chinese', 'code': 'zh', 'voice': 'nova'},
        '2': {'name': 'German', 'code': 'de', 'voice': 'onyx'},
        '3': {'name': 'Japanese', 'code': 'ja', 'voice': 'nova'},
        '4': {'name': 'Korean', 'code': 'ko', 'voice': 'nova'},
        '5': {'name': 'Spanish', 'code': 'es', 'voice': 'bella'},
        '6': {'name': 'French', 'code': 'fr', 'voice': 'alloy'}
    }
    
    def __init__(self):
        self.whisper = WhisperHandler(Config.API_KEY)
        self.chatgpt = ChatGPTHandler(Config.API_KEY)
        self.tts = TTSHandler(Config.API_KEY)
        self.audio = AudioManager()

    def _select_language(self) -> dict:
        """Prompt user to select a language from the supported list."""
        while True:
            print("\nAvailable languages:")
            for key, lang in self.SUPPORTED_LANGUAGES.items():
                print(f"{key}. {lang['name']}")
            
            choice = input("\nSelect a language (1-6): ").strip()
            
            if choice in self.SUPPORTED_LANGUAGES:
                selected = self.SUPPORTED_LANGUAGES[choice]
                Config.set_language(selected['name'])
                Config.set_tts_voice(selected['voice'])
                self.conversation = Conversation(Config.get_tutor_behaviour())

                print(f"\nSelected: {selected['name']}")
                return selected
            
            print("Invalid selection. Please try again.")

    def run(self):
        print("Starting Language Tutor...")
        print("Press Ctrl+C to exit")
        self._select_language()
        print(f"Starting {Config.get_language()} lesson...")
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
        
    tutor = LanguageTutor()
    tutor.run()

if __name__ == "__main__":
    main()