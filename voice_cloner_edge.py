"""
Voice Cloning using Edge TTS (Microsoft Edge Text-to-Speech)
Compatible with Python 3.13+
High-quality voices with natural speech
"""

import asyncio
import edge_tts
import os
from pathlib import Path


class VoiceCloner:
    """
    Voice synthesis using Microsoft Edge TTS
    Supports 400+ voices in 100+ languages
    """
    
    def __init__(self):
        """Initialize the voice cloner"""
        print("Voice Cloner initialized (Edge TTS)")
        self.available_voices = None
    
    async def _get_voices(self):
        """Get available voices"""
        if self.available_voices is None:
            self.available_voices = await edge_tts.list_voices()
        return self.available_voices
    
    async def _clone_voice_async(self, text, voice, output_path, rate="+0%", pitch="+0Hz"):
        """
        Generate speech asynchronously
        
        Args:
            text (str): Text to convert to speech
            voice (str): Voice name (e.g., 'en-US-AriaNeural', 'hi-IN-SwaraNeural')
            output_path (str): Path to save audio
            rate (str): Speech rate (e.g., "+0%", "+20%", "-20%")
            pitch (str): Pitch adjustment (e.g., "+0Hz", "+50Hz", "-50Hz")
        """
        # Ensure output directory exists
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        
        # Create TTS communicator
        communicate = edge_tts.Communicate(text, voice, rate=rate, pitch=pitch)
        
        # Save audio
        await communicate.save(output_path)
    
    def clone_voice(self, text, reference_audio_path=None, output_path="output.mp3", 
                   language="en", voice_name=None, rate="+0%", pitch="+0Hz"):
        """
        Generate speech from text
        
        Args:
            text (str): Text to convert to speech
            reference_audio_path (str): Not used in Edge TTS (kept for compatibility)
            output_path (str): Path to save generated audio
            language (str): Language code (en, hi, ur, etc.)
            voice_name (str): Specific voice name (optional)
            rate (str): Speech rate adjustment
            pitch (str): Pitch adjustment
        
        Returns:
            str: Path to generated audio file
        """
        print(f"\nGenerating speech...")
        print(f"Text: '{text[:50]}...'")
        print(f"Language: {language}")
        
        # Map language codes to default voices
        voice_map = {
            'en': 'en-US-AriaNeural',      # English (US) - Female
            'hi': 'hi-IN-SwaraNeural',     # Hindi - Female
            'ur': 'ur-PK-UzmaNeural',      # Urdu - Female
            'es': 'es-ES-ElviraNeural',    # Spanish - Female
            'fr': 'fr-FR-DeniseNeural',    # French - Female
            'de': 'de-DE-KatjaNeural',     # German - Female
            'it': 'it-IT-ElsaNeural',      # Italian - Female
            'pt': 'pt-BR-FranciscaNeural', # Portuguese - Female
            'pl': 'pl-PL-ZofiaNeural',     # Polish - Female
            'tr': 'tr-TR-EmelNeural',      # Turkish - Female
            'ru': 'ru-RU-SvetlanaNeural',  # Russian - Female
            'nl': 'nl-NL-ColetteNeural',   # Dutch - Female
            'cs': 'cs-CZ-VlastaNeural',    # Czech - Female
            'ar': 'ar-SA-ZariyahNeural',   # Arabic - Female
            'zh-cn': 'zh-CN-XiaoxiaoNeural', # Chinese - Female
            'ja': 'ja-JP-NanamiNeural',    # Japanese - Female
            'hu': 'hu-HU-NoemiNeural',     # Hungarian - Female
            'ko': 'ko-KR-SunHiNeural'      # Korean - Female
        }
        
        # Select voice
        voice = voice_name if voice_name else voice_map.get(language, 'en-US-AriaNeural')
        
        print(f"Using voice: {voice}")
        
        # Run async function
        asyncio.run(self._clone_voice_async(text, voice, output_path, rate, pitch))
        
        print(f"✓ Audio generated successfully: {output_path}")
        return output_path
    
    def clone_voice_batch(self, texts, reference_audio_path=None, output_dir="output", 
                         language="en", voice_name=None):
        """
        Generate speech for multiple texts
        
        Args:
            texts (list): List of texts to convert
            reference_audio_path (str): Not used (kept for compatibility)
            output_dir (str): Directory to save generated audios
            language (str): Language code
            voice_name (str): Specific voice name (optional)
        
        Returns:
            list: Paths to generated audio files
        """
        os.makedirs(output_dir, exist_ok=True)
        output_paths = []
        
        for i, text in enumerate(texts):
            output_path = os.path.join(output_dir, f"speech_{i+1}.mp3")
            self.clone_voice(text, None, output_path, language, voice_name)
            output_paths.append(output_path)
        
        return output_paths
    
    async def _list_voices_async(self, language=None):
        """List available voices"""
        voices = await self._get_voices()
        
        if language:
            # Filter by language
            voices = [v for v in voices if v['Locale'].startswith(language)]
        
        return voices
    
    def list_voices(self, language=None):
        """
        List available voices
        
        Args:
            language (str): Filter by language code (e.g., 'en', 'hi')
        
        Returns:
            list: Available voices
        """
        return asyncio.run(self._list_voices_async(language))


def main():
    """Example usage"""
    cloner = VoiceCloner()
    
    # Example 1: English
    print("\n" + "="*60)
    print("Example 1: English Speech")
    print("="*60)
    cloner.clone_voice(
        text="Hello, this is a demonstration of text to speech technology.",
        output_path="output/english_speech.mp3",
        language="en"
    )
    
    # Example 2: Hindi
    print("\n" + "="*60)
    print("Example 2: Hindi Speech")
    print("="*60)
    cloner.clone_voice(
        text="नमस्ते, यह टेक्स्ट टू स्पीच टेक्नोलॉजी का एक उदाहरण है।",
        output_path="output/hindi_speech.mp3",
        language="hi"
    )
    
    # Example 3: List available voices
    print("\n" + "="*60)
    print("Example 3: List Hindi Voices")
    print("="*60)
    voices = cloner.list_voices('hi')
    for voice in voices[:5]:  # Show first 5
        print(f"- {voice['ShortName']}: {voice['FriendlyName']}")


if __name__ == "__main__":
    main()
