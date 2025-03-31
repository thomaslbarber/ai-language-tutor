from typing import Optional
from handlers.api_handler import OpenAIHandler
from config import Config
from utils.text_converter import TextConverter
import os
import requests

class WhisperHandler(OpenAIHandler):
    def __init__(self, api_key: str):
        super().__init__(api_key)
        self.converter = TextConverter()

    def transcribe_audio(self, audio_file: str) -> Optional[str]:
        headers = {"Authorization": f"Bearer {Config.API_KEY}"}
        with open(audio_file, "rb") as f:
            files = { "file": f}
            prompt = f"This is a {Config.get_language()} language learning conversation. Transcribe speech into {Config.get_language()} unless it makes logical sense not to."
            data = {
                "model": "whisper-1",
                "language": Config.get_code(),
                "response_format": "json",
                "prompt": prompt,
                "temperature": 0.0
            }

            response = requests.post("https://api.openai.com/v1/audio/transcriptions", 
                                headers=headers, 
                                files=files, 
                                data=data)
        
        os.remove(audio_file)  
        
        if response.status_code == 200:
            transcript = response.json()["text"]
            print("You said:", transcript.encode('utf-8').decode('utf-8'))
            return transcript
        else:
            print("Error with Whisper API:", response.text)
            return None
