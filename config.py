import os

OPENAI_API_BASE = "https://api.openai.com/v1"

class Config:
    WHISPER_ENDPOINT = f"{OPENAI_API_BASE}/audio/transcriptions"
    CHATGPT_ENDPOINT = f"{OPENAI_API_BASE}/chat/completions"
    TTS_ENDPOINT = f"{OPENAI_API_BASE}/audio/speech"
    MODEL = "gpt-4o-mini"
    SAMPLE_RATE = 44100
    MAX_DURATION = 30
    AUDIO_THRESHOLD = 0.02
    TEMP_AUDIO_FILE = "temp_audio.mp3"
    API_KEY = os.getenv("OPENAI_API_KEY")
    MAX_MESSAGES = 6

    _language = "Simplified Mandarin Chinese"
    _tts_voice = "nova"
    _code = "zh"

    @classmethod
    def get_language(cls) -> str:
        return cls._language

    @classmethod
    def set_language(cls, value: str) -> None:
        cls._language = value

    @classmethod
    def get_code(cls) -> str:
        return cls._code

    @classmethod
    def set_code(cls, value: str) -> None:
        cls._code = value

    @classmethod
    def get_tts_voice(cls) -> str:
        return cls._tts_voice

    @classmethod
    def set_tts_voice(cls, value: str) -> None:
        cls._tts_voice = value

    @classmethod
    def get_tutor_behaviour(cls) -> str:
        return f"""You are a {cls._language} language tutor. 
        You will engage in conversations with the user and remain at their conversational level.
        You should be the driving force of the conversation, asking questions and providing feedback.
        You will initiate the conversation and guide the user through it.
        You have the role 'assistant' and 'user' is your student.
        Correct any pronunciation or grammar mistakes the student makes.
        Format your responses like this:
        Provide the language like so: '{cls._language}:', followed by your dialogue text in {cls._language}.
        At the end of your response, provide the English translation of your message in the following:
        English: [translation]"""

    CODE = property(get_code, set_code)
    LANGUAGE = property(get_language, set_language)
    TTS_VOICE = property(get_tts_voice, set_tts_voice)
    TUTOR_BEHAVIOUR = property(get_tutor_behaviour)