"""
Force Download TTS Model
This will download the model and show clear progress
"""

import sys
import os

# Fix encoding for Windows
if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

print("="*70)
print("🎤 Downloading XTTS-v2 Voice Cloning Model")
print("="*70)
print()
print("This will download ~2GB model")
print("Please be patient and don't close this window!")
print()
print("="*70)
print()

try:
    print("Step 1: Importing TTS library...")
    from TTS.api import TTS
    print("✅ TTS library imported")
    print()
    
    print("Step 2: Checking PyTorch...")
    import torch
    device = "cuda" if torch.cuda.is_available() else "cpu"
    print(f"✅ Using device: {device}")
    print()
    
    print("Step 3: Downloading and loading XTTS-v2 model...")
    print("⏳ This will take 10-20 minutes on first run")
    print("📊 Download progress will be shown below:")
    print("-"*70)
    
    # This will download the model if not present
    tts = TTS("tts_models/multilingual/multi-dataset/xtts_v2").to(device)
    
    print("-"*70)
    print()
    print("="*70)
    print("🎉 SUCCESS! Model downloaded and loaded!")
    print("="*70)
    print()
    print("Now you can run: start_with_cloning.bat")
    print("It will start instantly!")
    print()
    
except KeyboardInterrupt:
    print()
    print("❌ Download cancelled by user")
    print("Run this script again to resume")
    sys.exit(1)
    
except Exception as e:
    print()
    print("="*70)
    print("❌ ERROR")
    print("="*70)
    print(f"Error: {e}")
    print()
    print("Possible solutions:")
    print("1. Check internet connection")
    print("2. Run script again")
    print("3. Or use Edge TTS (no download needed)")
    print()
    sys.exit(1)
