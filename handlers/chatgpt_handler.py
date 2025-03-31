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
            print("ChatGPT:", full_reply.encode('utf-8').decode('utf-8'))
            return self._extract_chinese_text(full_reply)
        except Exception as e:
            print(f"Error processing ChatGPT response: {e}")
            return None

    @staticmethod
    def _extract_chinese_text(text: str) -> Optional[str]:
        try:
            chinese_start = text.find("Chinese:") + 8
            chinese_end = text.find("Pinyin:")
            if chinese_start > 7 and chinese_end > -1:
                return text[chinese_start:chinese_end].strip()
            print("Could not find Chinese text in response")
            return None
        except Exception as e:
            print(f"Error extracting Chinese text: {e}")
            return None