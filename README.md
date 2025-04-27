# Qazaq TTS

A simple utility for converting text to speech in Kazakh language using [ISSAI](https://issai.nu.edu.kz) TTS service.

## Installation

```bash
# Install required modules
pip install requests beautifulsoup4
```

## Usage

### Using as a module
```python
from tts import TTS_ISSAI

# Initialize converter
converter = TTS_ISSAI()

# Get available speakers
speakers = converter.get_speakers()
print("Available speakers:", speakers)

# Convert text to MP3 file
text = "Сәлем, балапан!"
filename = converter.convert_to_speech(text, speaker_id="4")
if filename:
    print(f"Audio file created: {filename}")
```

### Using from console
```bash
python app.py
```

## Features

- 5 different voices:
  - Iseke (ID: 1)
  - Raya (ID: 2)
  - Asel (ID: 3)
  - Duman (ID: 4)
  - Gulzhanat (ID: 5)
- Text length up to 271 characters
- MP3 file generation
- Simple API

## TODO

- [x] Increase text length limit (271 characters)
- [ ] Add support for longer texts
  - [ ] Split long text into smaller chunks
- [x] Add error handling
- [x] Add text validation
- [ ] Add subtitle maker
  - [ ] Generate SRT files
  - [ ] Support multiple timestamp formats
  - [ ] Add subtitle preview
- [ ] Add caching for frequently used phrases
- [ ] Add batch processing support

## Examples

```python
# With default parameters (Duman's voice)
filename = converter.convert_to_speech("Сәлем, балапан!")

# With different speaker (Raya's voice)
filename = converter.convert_to_speech("Сәлем, балапан!", speaker_id="2")
```

## Credits

- ISSAI DEMO TTS service - [ISSAI](https://issai.nu.edu.kz/ru/tts2-rus/)
- Python wrapper - [My Telegram channel](https://t.me/davidsurgan)
