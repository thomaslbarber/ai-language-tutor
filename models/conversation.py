class Conversation:
    def __init__(self, system_prompt: str):
        self.messages = [{"role": "system", "content": system_prompt}]
    
    def add_message(self, role: str, content: str):
        self.messages.append({"role": role, "content": content})
    
    def get_messages(self):
        return self.messages