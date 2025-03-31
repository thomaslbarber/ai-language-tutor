from handlers.api_handler import OpenAIHandler
from typing import Optional
from config import Config
import requests

class ChatGPTHandler(OpenAIHandler):
    def get_response(self, conversation: 'Conversation') -> Optional[str]:
        data = {
            "model": Config.MODEL,
            "messages": conversation.get_messages(),
            "temperature": 0.7
        }
        
        response = self._make_request(Config.CHATGPT_ENDPOINT, data)
        if not response:
            return None
            
        try:
            full_reply = response["choices"][0]["message"]["content"]
            print("\033[36m""The Tutor said: ")
            print(full_reply.strip().encode('utf-8').decode('utf-8') + "\033[0m")
            return self._extract_chinese_text(full_reply, conversation)
        except Exception as e:
            print(f"Error processing their response: {e}")
            return None

    @staticmethod
    def _extract_chinese_text(text: str, conversation: 'Conversation') -> Optional[str]:
        try:
            chinese_start = text.find(":")
            chinese_end = text.find("English:")
            if chinese_end == -1:
                chinese_end = len(text)
            if chinese_start != -1 and chinese_end > -1:
                extract = text[chinese_start:chinese_end]
                conversation.add_message("assistant", extract)
                return extract
            print("Could not find Chinese text in response")
            return None
        except Exception as e:
            print(f"Error extracting Chinese text: {e}")
            return None