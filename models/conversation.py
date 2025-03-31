from typing import List, Dict
from collections import deque
from config import Config

class Conversation:    
    def __init__(self, system_prompt: str):
        """Initialize conversation with system prompt."""
        self.system_prompt = {"role": "system", "content": system_prompt}
        self.message_history = deque(maxlen=Config.MAX_MESSAGES)
    
    def add_message(self, role: str, content: str) -> None:
        """Add a new message to the conversation history.
        Automatically removes oldest message if limit is reached."""
        self.message_history.append({"role": role, "content": content})
    
    def get_messages(self) -> List[Dict[str, str]]:
        """Get all messages including system prompt."""
        return [self.system_prompt] + list(self.message_history)