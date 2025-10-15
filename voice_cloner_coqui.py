"""
REAL Voice Cloning using Coqui TTS XTTS-v2
Requires Python 3.9, 3.10, or 3.11
"""

import os
import torch
from TTS.api import TTS
from pathlib import Path
import warnings
warnings.filterwarnings('ignore')


class VoiceCloner:
    """
    Voice cloning using Coqui TTS XTTS-v2 model
    Free, high-quality REAL voice cloning
    """
    
    def __init__(self):
        """Initialize the TTS model"""
        print("Loading voice cloning model (XTTS-v2)...")
        print("This may take a few minutes on first run...")
        
        # Use XTTS-v2 for best quality voice cloning
        self.device = "cuda" if torch.cuda.is_available() else "cpu"
        print(f"Using device: {self.device}")
        
        # Initialize TTS with XTTS-v2 model
        self.tts = TTS("tts_models/multilingual/multi-dataset/xtts_v2").to(self.device)
        print("Model loaded successfully!")
    
    def clone_voice(self, text, reference_audio_path, output_path, language="en"):
        """
        Clone voice and generate speech
        
        Args:
            text (str): Text to convert to speech
            reference_audio_path (str): Path to reference audio file (6-10 seconds recommended)
            output_path (str): Path to save generated audio
            language (str): Language code (en, hi, ur, es, fr, de, it, pt, pl, tr, ru, nl, cs, ar, zh-cn, ja, hu, ko)
        
        Returns:
            str: Path to generated audio file
        """
        print(f"\n🎤 Cloning voice from: {reference_audio_path}")
        print(f"📝 Generating speech for: '{text[:50]}...'")
        print(f"🌍 Language: {language}")
        
        # Ensure output directory exists
        os.makedirs(os.path.dirname(output_path) if os.path.dirname(output_path) else '.', exist_ok=True)
        
        # Generate speech with cloned voice
        self.tts.tts_to_file(
            text=text,
            speaker_wav=reference_audio_path,
            language=language,
            file_path=output_path
        )
        
        print(f"✅ Audio generated successfully: {output_path}")
        return output_path
    
    def clone_voice_batch(self, texts, reference_audio_path, output_dir, language="en"):
        """
        Clone voice for multiple texts
        
        Args:
            texts (list): List of texts to convert
            reference_audio_path (str): Path to reference audio
            output_dir (str): Directory to save generated audios
            language (str): Language code
        
        Returns:
            list: Paths to generated audio files
        """
        os.makedirs(output_dir, exist_ok=True)
        output_paths = []
        
        for i, text in enumerate(texts):
            output_path = os.path.join(output_dir, f"cloned_audio_{i+1}.wav")
            self.clone_voice(text, reference_audio_path, output_path, language)
            output_paths.append(output_path)
        
        return output_paths


def main():
    """Example usage"""
    # Initialize voice cloner
    cloner = VoiceCloner()
    
    # Example: Clone voice
    text = "Hello, this is a test of REAL voice cloning technology. The quality is quite impressive!"
    reference_audio = "reference_voice.wav"  # Your reference audio file
    output_audio = "output/cloned_speech.wav"
    
    # For Hindi/Urdu, use language="hi" or language="ur"
    # text = "यह एक टेस्ट है वॉइस क्लोनिंग का"
    # language = "hi"
    
    cloner.clone_voice(
        text=text,
        reference_audio_path=reference_audio,
        output_path=output_audio,
        language="en"  # Change to "hi" for Hindi, "ur" for Urdu
    )


if __name__ == "__main__":
    main()
