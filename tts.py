import requests
from bs4 import BeautifulSoup
import base64
from datetime import datetime
import os
from typing import Dict

class TTS_ISSAI:
    def __init__(self):
        self.url = "https://issai.nu.edu.kz/ru/tts2-rus/"
        self.headers = {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            "Accept-Language": "en-US,en;q=0.5",
            "Connection": "keep-alive",
            "Content-Type": "application/x-www-form-urlencoded",
            "Host": "issai.nu.edu.kz",
            "Origin": "https://issai.nu.edu.kz",
            "Referer": "https://issai.nu.edu.kz/ru/tts2-rus/"
        }
        
        # Available speakers
        self.speakers: Dict[str, str] = {
            "1": "Iseke",
            "2": "Raya",
            "3": "Asel",
            "4": "Duman",
            "5": "Gulzhanat"
        }
        
        # Get actual text limit
        self.MAX_TEXT_LENGTH = 271

    def get_speakers(self) -> Dict[str, str]:
        """Returns list of available speakers"""
        return self.speakers
    
    def validate_text(self, text: str) -> tuple[bool, str]:
        """Validates text length and returns (is_valid, error_message)"""
        if not text:
            return False, "Text cannot be empty"
        
        if len(text) > self.MAX_TEXT_LENGTH:
            return False, f"Text is too long (maximum {self.MAX_TEXT_LENGTH} characters)"
            
        return True, ""
    
    def convert_to_speech(self, text, speaker_id="4") -> str:
        """Converts text to audio file and returns filepath"""
        # Validate text first
        is_valid, error = self.validate_text(text)
        if not is_valid:
            print(f"Text validation error: {error}")
            return None

        data = {
            "sentence": text,
            "value": speaker_id,
        }
        
        try:
            response = requests.post(self.url, headers=self.headers, data=data)
            response.raise_for_status()
            
            soup = BeautifulSoup(response.text, 'html.parser')
            audio_source_tag = soup.select_one('#audioContainer audio source')
            
            if audio_source_tag and audio_source_tag.get('src'):
                audio_src = audio_source_tag.get('src')
                base64_prefix = "data:audio/mp3;base64,"
                
                if audio_src.startswith(base64_prefix):
                    base64_data = audio_src[len(base64_prefix):]
                    audio_content = base64.b64decode(base64_data)
                    
                    output_filename = f"output_{datetime.now().strftime('%Y%m%d_%H%M%S')}.mp3"
                    with open(output_filename, "wb") as f:
                        f.write(audio_content)
                    
                    if os.path.getsize(output_filename) > 0:
                        return output_filename
                    else:
                        os.remove(output_filename)
                        
            return None
            
        except Exception as e:
            print(f"An error occurred: {e}")
            return None

# Usage example:
if __name__ == "__main__":
    converter = TTS_ISSAI()
    
    print("Available speakers:")
    for id, name in converter.get_speakers().items():
        print(f"ID: {id} - {name}")
    
    text = "Hello, this is a test"
    filename = converter.convert_to_speech(text, speaker_id="4")
    if filename:
        print(f"Audio file created: {filename}")