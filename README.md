# ai-language-tutor 🎓
An interactive language learning tool powered by OpenAI's GPT-4, Whisper, and Text-to-Speech APIs. Train your conversational skills by having natural voice conversations with an AI language tutor, who determines the speaker's level and converses at a suitable level, correcting any mistakes in grammar or pronunciation.

## Features 🌟
<ul>
  <li><b>Voice Recognition</b>: Speak in your target language and get real-time transcription</li>
  <li><b>Intelligent Responses</b>: Context-aware conversations with a virtual tutor</li>
  <li><b>Text-to-Speech</b>: Hear correct pronunciation of phrases in your target language</li>
  <li><b>Conversation History</b>: Maintains context for natural dialogue flow</li>
  <li><b>Noise Reduction</b>: Advanced audio processing for clear voice capture</li>
  <li><b>Preconfigured Target Languages</b>: Includes six preconfigured target languages and allows users to easily add new ones
    <ul>
      <li>Preconfigured for: Mandarin Chinese, German, Japanese, Korean, Spanish, French</li>
    </ul>
  </li>
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
<ul>
<li>Clone the repository:</li>
  
```bash
git clone https://github.com/yourusername/ai-language-tutor.git
cd ai-language-tutor
```
<li>Install required packages:</li>

```bash
pip install -r requirements.txt
```
  <li>Set your OpenAI API key in your environment variables as 'OPENAI_API_KEY'</li>
  <li>If your target is not one of the preconfigured languages (Mandarin Chinese, German, Japanese, Korean, Spanish, French), add a new entry in SUPPORTED_LANGUAGES with the following attributes:
    <ul>
  <li><i>id</i>: Unique identifier when choosing the language in the command line.</li>
  <li><i>name</i>: A string representation of the language Used to inform OpenAI what language to expect.</li>
  <li><i>code</i>: The ISO 639 representation for the language, used when parsing the text to ensure characters in the target language are ouput correctly in the command line.</li>
  <li><i>voice</i>: The voice for the Tutor. <a href="https://platform.openai.com/docs/guides/text-to-speech#voice-options">Choose one from the list of available voices in the OpenAI documentation</a>.</li>
    </ul>
    </li>
</ul>


## Usage 💡
### Conversation
<ul>
  <li>Follow the on-screen prompts to select a target language to converse in.</li>
  <li>Listen to the dialogue from the Tutor. This is audible, as well as visible in the console output.</li>
  <li>When prompted, press SPACE to record your response. Press SPACE again to stop the recording.</li>
  <li>The audio will be parsed to speech and sent to the Tutor for processing, who will continue the conversation at your level.</li>
  <li>Repeat to engage in conversational practice. The conversation maintains at all times the latest two student and two tutor responses to ensure a level of contextual understanding without excessive API usage. </li>
  <img src="docs/README_Overview.PNG"/>
</ul>

### Teaching the User
The tutor parses the input and provides corrections on any grammatical or pronunciation errors.
<img src="docs/README_CorrectingUser.PNG"/>

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
This project is licensed under the MIT License.

## Contact 📧
Feel free to contact me with any issues.

Project Link: https://github.com/yourusername/ai-language-tutor
