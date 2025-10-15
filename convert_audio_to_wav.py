"""
Convert any audio file to WAV format for voice cloning
"""

import sys
import os

def convert_to_wav(input_file, output_file=None):
    """Convert audio to WAV format"""
    
    if output_file is None:
        output_file = input_file.rsplit('.', 1)[0] + '_converted.wav'
    
    print(f"Converting {input_file} to WAV format...")
    
    try:
        import librosa
        import soundfile as sf
        
        # Load audio
        print("Loading audio...")
        audio_data, sample_rate = librosa.load(input_file, sr=22050, mono=True)
        
        # Save as WAV
        print(f"Saving as WAV: {output_file}")
        sf.write(output_file, audio_data, sample_rate)
        
        print(f"✅ Success! Converted to: {output_file}")
        print(f"\nNow use this file in the web app!")
        return output_file
        
    except Exception as e:
        print(f"❌ Error: {e}")
        print("\nPlease make sure the audio file is valid.")
        return None

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python convert_audio_to_wav.py <audio_file>")
        print("\nExample:")
        print("  python convert_audio_to_wav.py my_voice.mp3")
        print("  python convert_audio_to_wav.py my_voice.m4a")
        sys.exit(1)
    
    input_file = sys.argv[1]
    
    if not os.path.exists(input_file):
        print(f"❌ File not found: {input_file}")
        sys.exit(1)
    
    convert_to_wav(input_file)
