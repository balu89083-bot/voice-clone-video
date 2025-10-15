"""
Download TTS Model to E Drive
"""

import sys
import os

# Fix encoding for Windows
if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

# Set TTS cache to E drive
os.environ['TTS_HOME'] = 'E:\\tts_cache'
os.environ['COQUI_TOS_AGREED'] = '1'

print("="*70)
print("🎤 Downloading XTTS-v2 Model to E Drive")
print("="*70)
print()
print(f"📁 Cache location: E:\\tts_cache")
print("📋 License: Non-commercial CPML")
print("✅ Auto-accepting license...")
print()
print("This will download ~2GB to E drive")
print("Please be patient!")
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
    
    print("Step 3: Downloading model to E drive...")
    print("⏳ This will take 10-20 minutes")
    print("📊 Download progress:")
    print("-"*70)
    
    # Download model to E drive
    tts = TTS("tts_models/multilingual/multi-dataset/xtts_v2", progress_bar=True).to(device)
    
    print("-"*70)
    print()
    print("="*70)
    print("🎉 SUCCESS! Model downloaded to E drive!")
    print("="*70)
    print()
    print(f"✅ Model location: E:\\tts_cache")
    print()
    print("Now run: START_APP.bat")
    print()
    
except KeyboardInterrupt:
    print()
    print("❌ Download cancelled")
    sys.exit(1)
    
except Exception as e:
    print()
    print("="*70)
    print("❌ ERROR")
    print("="*70)
    print(f"Error: {e}")
    print()
    
    if "not enough memory" in str(e).lower() or "alloc" in str(e).lower():
        print("⚠️  MEMORY ERROR!")
        print()
        print("Your system doesn't have enough RAM for XTTS-v2 model.")
        print("XTTS-v2 requires 4-6GB free RAM.")
        print()
        print("✅ SOLUTION: Use Edge TTS instead")
        print()
        print("Edge TTS:")
        print("  • No RAM required (cloud-based)")
        print("  • High quality voices")
        print("  • 400+ voices")
        print("  • Instant start")
        print("  • No model download")
        print()
        print("To use Edge TTS:")
        print("  1. Just run: python app.py")
        print("  2. Open: http://localhost:5000")
        print()
        print("Note: Edge TTS doesn't clone voices,")
        print("but provides excellent pre-built voices.")
    else:
        print("Possible solutions:")
        print("1. Check internet connection")
        print("2. Run script again")
        print("3. Or use Edge TTS (no download needed)")
    
    print()
    import traceback
    traceback.print_exc()
    sys.exit(1)
