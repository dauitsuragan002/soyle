from tts import TTS_ISSAI

# Initialize converter
converter = TTS_ISSAI()

# Convert text to MP3 file
text = "Сәлем балапан!"
filename = converter.convert_to_speech(text, speaker_id="1")
if filename:
    print(f"Audio file created: {filename}")