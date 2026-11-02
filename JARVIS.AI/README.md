# JARVIS AI - Voice Controlled Desktop Assistant

A beginner-friendly Python voice assistant for Windows. JARVIS listens to voice commands, speaks responses, opens commonly used websites and Windows applications, controls system volume, plays YouTube music, looks up short Wikipedia summaries, and takes screenshots.

> **Project status:** Learning / personal project. This is a rule-based assistant, not a full conversational AI model. It does not currently send WhatsApp messages or control Instagram accounts.

## Features

- Speech input using `SpeechRecognition` and the Google Web Speech service.
- Text-to-speech responses using `pyttsx3`.
- Open websites: Google, YouTube, WhatsApp Web, Instagram, LinkedIn, Facebook, Gmail, ChatGPT, Google Maps and GitHub.
- Open Windows apps: Chrome, Notepad, Calculator, File Explorer and Settings.
- Tell the current time.
- Play a requested song/video on YouTube using `pywhatkit`.
- Get short Wikipedia summaries.
- Increase, decrease and mute system volume.
- Capture a screenshot in the project folder.
- Lock, restart or shut down Windows (power actions require typed confirmation).

## Tech stack

- Python 3.12 (recommended)
- SpeechRecognition
- PyAudio
- pyttsx3
- PyWhatKit
- Wikipedia
- PyAutoGUI

## Requirements

- Windows 10/11
- Python 3.12 recommended
- A working microphone and speakers/headphones
- Internet connection for speech recognition, Wikipedia, YouTube and websites
- Google Chrome installed if you want to use the `open chrome` command

## Setup

Open Command Prompt or the VS Code terminal in this project directory.

### 1. Create a virtual environment

```bash
py -3.12 -m venv .venv
```

### 2. Activate it (Windows Command Prompt)

```cmd
.venv\Scripts\activate
```

For PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

### 4. Test your microphone

```bash
python mic_test.py
```

Say a short sentence. The recognized text should appear in the terminal.

### 5. Run JARVIS

```bash
python ai.py
```

Say `stop`, `exit`, `quit`, or `goodbye` to close the assistant. You can also press `Ctrl+C` in the terminal.

## Voice command examples

| Say this | JARVIS action |
|---|---|
| `What time is it` | Speaks the current time |
| `Open Chrome` | Opens Google Chrome |
| `Open Google` | Opens Google |
| `Open WhatsApp` | Opens WhatsApp Web |
| `Open Instagram` | Opens Instagram |
| `Open YouTube` | Opens YouTube |
| `Open LinkedIn` | Opens LinkedIn |
| `Open Facebook` | Opens Facebook |
| `Open Gmail` | Opens Gmail |
| `Open ChatGPT` | Opens ChatGPT |
| `Open Maps` | Opens Google Maps |
| `Open GitHub` | Opens GitHub |
| `Play [song name]` | Searches and plays on YouTube |
| `Who is [person]` | Reads a short Wikipedia summary |
| `What is [topic]` | Reads a short Wikipedia summary |
| `Volume up` | Increases system volume |
| `Volume down` | Decreases system volume |
| `Mute` | Mutes system volume |
| `Open Notepad` | Opens Notepad |
| `Open Calculator` | Opens Calculator |
| `Open File Explorer` | Opens File Explorer |
| `Open Settings` | Opens Windows Settings |
| `Screenshot` | Saves a timestamped screenshot |
| `Lock computer` | Locks Windows |
| `Shutdown` / `Restart` | Asks for typed confirmation in the terminal |
| `Stop` / `Exit` | Closes JARVIS |

Speech recognition is configured for Indian English (`en-IN`). Change the `language` argument in `ai.py` and `mic_test.py` if needed.

## Troubleshooting

### `Could not find PyAudio` / microphone error

1. Activate the project's `.venv`.
2. Confirm that the terminal prompt starts with `(.venv)`.
3. Run:

   ```bash
   python -m pip install PyAudio==0.2.14
   ```

4. Test it:

   ```bash
   python -c "import pyaudio; print('PyAudio OK')"
   ```

If installation fails, check that you are using 64-bit Python 3.12 and that the correct virtual environment is active.

### `No Default Input Device Available`

Check Windows microphone permissions and select a working input device in **Settings → System → Sound → Input**.

### Speech recognition request error

Google speech recognition needs an internet connection. Check your connection and try again.

### JARVIS does not understand the command

Speak clearly, reduce background noise, and use one of the command phrases listed above. The current command matching is based on simple English keywords.

### `python` runs a different environment

Activate `.venv` first, then run `python ai.py`. Do not install packages into a different Python installation by mistake.

## Project structure

```text
JARVIS-AI/
├── ai.py                 # Main voice assistant
├── mic_test.py           # Microphone test utility
├── requirements.txt      # Python dependencies
├── README.md             # Project documentation
├── LICENSE               # MIT License
├── CHANGELOG.md          # Version history
├── CONTRIBUTING.md       # Contribution guidelines
├── CODE_OF_CONDUCT.md    # Community guidelines
├── SECURITY.md           # Security reporting guidance
├── .gitignore            # Files Git should ignore
└── .github/
    └── ISSUE_TEMPLATE/
        ├── bug_report.md
        └── feature_request.md
```

## Privacy and safety notes

- Audio is sent to Google's speech recognition service by `recognize_google`; this project is not fully offline.
- JARVIS opens websites in your default browser. You may need to sign in yourself.
- Do not commit passwords, API keys, tokens, personal screenshots, or private configuration files.
- Shutdown and restart commands require typing an explicit confirmation in the terminal. Save your work before testing them.
- Use automation features responsibly and respect the terms of services of websites.

## Future improvements

- Add a graphical user interface.
- Add configurable wake-word detection.
- Add offline speech recognition.
- Add Hindi and multilingual command support.
- Add a settings/configuration file for voice and command preferences.
- Add unit tests and structured logging.

## License

This project is licensed under the MIT License. See [LICENSE](LICENSE).

---

Made with Python and curiosity. ⭐ If you find this project useful, consider starring the repository!
