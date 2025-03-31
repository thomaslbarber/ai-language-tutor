# ai-language-tutor 🎓
An interactive language learning tool powered by OpenAI's GPT-4, Whisper, and Text-to-Speech APIs.

## Features 🌟
<ul>
  <li>Voice Recognition: Speak in your target language and get real-time transcription</li>
  <li>Intelligent Responses: Context-aware conversations with a virtual tutor</li>
  <li>Text-to-Speech: Hear correct pronunciation of phrases in your target language</li>
  <li>Conversation History: Maintains context for natural dialogue flow</li>
  <li>Noise Reduction: Advanced audio processing for clear voice capture</li>
</ul>
 
## Prerequisites 📋
<ul>
  <li>Python 3.8 or higher</li>
  <li>An OpenAI API key</li>
  <li>Windows</li>
  <li>Microphone for voice input</li>
  <li>Speakers for audio output</li>
  <li>A console able to output Unicode characters if using a language with Unicode characters (e.g., Chinese)
      <ul>
        <li>(I use <a href="https://cmder.app/">Cmder</a>!)</li>
      </ul>
</ul>

## Installation 🔧
Clone the repository:
```bash
git clone https://github.com/yourusername/ai-language-tutor.git
cd ai-language-tutor
```
Install required packages:
```bash
pip install -r requirements.txt
```

Set up your OpenAI API key:
```bash
set OPENAI_API_KEY=your_api_key_here
```

Update the language to your target language - this is preconfigured to use Mandarin Chinese.
## Usage 💡
<ol>
  <li>Start the program:</li>
TODO.png
  
<li>Follow the on-screen prompts:</li>
</ol>

Project Structure 📁
```plaintext
ai-language-tutor/
├── audio/
│   └── audio_manager.py
├── handlers/
│   ├── api_handler.py
│   ├── whisper_handler.py
│   ├── chatgpt_handler.py
│   └── tts_handler.py
├── models/
│   └── conversation.py
├── utils/
│   └── text_converter.py
├── config.py
├── main.py
└── requirements.txt
```

## Contributing 🤝
<ol>
  <li>Fork the repository</li>
  <li>Create your feature branch (git checkout -b feature/amazing-feature)</li>
  <li>Commit your changes (git commit -m 'Add amazing feature')</li>
  <li>Push to the branch (git push origin feature/amazing-feature)</li>
  <li>Open a Pull Request</li>
  <li>I will aim to review any open PRs regularly and merge meaningful contributions</li>
</ol>

## License 📄
TODO

Troubleshooting 🔍


## Contact 📧
Feel free to contact me with any issues.

Project Link: https://github.com/yourusername/ai-language-tutor
