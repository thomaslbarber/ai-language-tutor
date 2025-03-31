from handlers.api_handler import OpenAIHandler
from typing import Optional
from config import Config
import requests
import pygame
import time

class TTSHandler(OpenAIHandler):
    def text_to_speech(self, text: str) -> Optional[bytes]:
        try:
            headers = {
                "Authorization": f"Bearer {self.api_key}",
                "Content-Type": "application/json"
            }
            
            data = {
                "model": "gpt-4o-mini-tts",
                "input": text,
                "voice": Config.TTS_VOICE,
                "response_format": "mp3"
            }

            response = requests.post(
                Config.TTS_ENDPOINT,
                headers=headers,
                json=data
            )

            if response.status_code == 200:
                return response.content
            else:
                print(f"TTS API error: {response.status_code} - {response.text}")
                return None

        except Exception as e:
            print(f"TTS error: {str(e)}")
            return None