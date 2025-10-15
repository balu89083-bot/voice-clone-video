"""
Download TTS Model to E Drive with Memory Optimization
"""

import sys
import os
import gc

# Fix encoding for Windows
if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

# Set TTS cache to E drive BEFORE importing TTS
os.environ['TTS_HOME'] = 'E:\\tts_cache'
os.environ['COQUI_TOS_AGREED'] = '1'

# Set environment variables for memory optimization
os.environ['PYTORCH_CUDA_ALLOC_CONF'] = 'max_split_size_mb:128'

print("="*70)
print("🎤 Downloading XTTS-v2 Model to E Drive")
print("="*70)
print()
print(f"📁 Cache location: E:\\tts_cache")
print(f"💾 This will save ~2GB on E drive")
print("📋 License: Non-commercial CPML")
print("✅ Auto-accepting license...")
print()
print("⚠️  IMPORTANT: Close other applications to free up RAM!")
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
    
    # Force CPU and optimize memory
    device = "cpu"
    torch.set_num_threads(2)  # Limit threads to save memory
    
    print(f"✅ Using device: {device}")
    print(f"✅ Memory optimization enabled")
    print()
    
    # Clear any cached memory
    gc.collect()
    
    print("Step 3: Downloading model to E drive...")
    print("⏳ This will take 10-20 minutes")
    print("📊 Download progress:")
    print("-"*70)
    
    # Download model to E drive
    tts = TTS("tts_models/multilingual/multi-dataset/xtts_v2", progress_bar=True)
    
    print("-"*70)
    print()
    
    # Try to load model with minimal memory
    print("Step 4: Loading model (this needs RAM)...")
    print("⏳ Please wait...")
    
    tts = tts.to(device)
    
    print()
    print("="*70)
    print("🎉 SUCCESS! Model downloaded and loaded!")
    print("="*70)
    print()
    print(f"✅ Model location: E:\\tts_cache")
    print()
    print("Now run: START_APP_E_DRIVE.bat")
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
        print("⚠️  RAM MEMORY ERROR!")
        print()
        print("Your system doesn't have enough RAM.")
        print("XTTS-v2 requires 4-6GB free RAM to load.")
        print()
        print("🔧 SOLUTIONS:")
        print()
        print("Option 1: Free up RAM")
        print("  1. Close Chrome/Edge browsers")
        print("  2. Close other applications")
        print("  3. Restart computer")
        print("  4. Run this script again")
        print()
        print("Option 2: Use lighter alternative")
        print("  • Use Edge TTS (no RAM needed)")
        print("  • Run: python app.py")
        print()
        print("Option 3: Upgrade RAM")
        print("  • Add more RAM to your system")
        print("  • XTTS-v2 needs 4-6GB free")
    else:
        print("Possible solutions:")
        print("1. Check internet connection")
        print("2. Close other applications")
        print("3. Restart computer and try again")
    
    print()
    sys.exit(1)
