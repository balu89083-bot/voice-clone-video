"""
Simple Model Download with Clear Progress
"""

import sys
import os

# Set D drive BEFORE any imports
os.environ['TTS_HOME'] = 'D:\\tts_cache'
os.environ['COQUI_TOS_AGREED'] = '1'

print("="*70)
print("DOWNLOADING XTTS-V2 MODEL TO D DRIVE")
print("="*70)
print()
print("Location: D:\\tts_cache")
print("Size: ~2 GB")
print()

try:
    print("[1/4] Importing TTS library...")
    from TTS.api import TTS
    print("      SUCCESS!")
    print()
    
    print("[2/4] Checking system...")
    import torch
    print(f"      Device: CPU")
    print()
    
    print("[3/4] Downloading model (this takes 10-20 minutes)...")
    print("      Please wait, progress will show below:")
    print("-"*70)
    
    # This downloads and loads the model
    tts = TTS("tts_models/multilingual/multi-dataset/xtts_v2")
    
    print("-"*70)
    print()
    print("[4/4] Loading model into memory...")
    tts = tts.to("cpu")
    
    print()
    print("="*70)
    print("SUCCESS! MODEL READY!")
    print("="*70)
    print()
    print("Model saved to: D:\\tts_cache")
    print()
    print("Now run: START_APP_D_DRIVE.bat")
    print()
    
except KeyboardInterrupt:
    print()
    print("\nDownload cancelled by user")
    sys.exit(1)
    
except Exception as e:
    print()
    print("="*70)
    print("ERROR")
    print("="*70)
    print(f"\n{e}\n")
    
    if "memory" in str(e).lower() or "alloc" in str(e).lower():
        print("RAM ERROR: Not enough memory!")
        print()
        print("Solutions:")
        print("1. Restart computer and try again")
        print("2. Or use cloud solution (ElevenLabs)")
    else:
        print("Try:")
        print("1. Check internet connection")
        print("2. Run script again")
    
    print()
    sys.exit(1)
