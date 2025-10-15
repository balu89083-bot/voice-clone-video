"""
Download TTS Model with MAXIMUM Memory Optimization
For systems with limited RAM
"""

import sys
import os
import gc

# Fix encoding
if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

# Set E drive cache BEFORE any imports
os.environ['TTS_HOME'] = 'E:\\tts_cache'
os.environ['COQUI_TOS_AGREED'] = '1'

# Maximum memory optimization
os.environ['PYTORCH_CUDA_ALLOC_CONF'] = 'max_split_size_mb:32'
os.environ['OMP_NUM_THREADS'] = '1'
os.environ['MKL_NUM_THREADS'] = '1'

print("="*70)
print("🎤 Downloading XTTS-v2 with Memory Optimization")
print("="*70)
print()
print("💾 Location: E:\\tts_cache")
print("🧠 RAM: Using minimal memory mode")
print()
print("⚠️  NOTE: This will only DOWNLOAD the model")
print("   Loading will happen when you start the app")
print()
print("="*70)
print()

try:
    print("Step 1: Importing libraries...")
    from TTS.utils.manage import ModelManager
    print("✅ Libraries imported")
    print()
    
    print("Step 2: Setting up model manager...")
    manager = ModelManager()
    print("✅ Manager ready")
    print()
    
    print("Step 3: Downloading model to E drive...")
    print("📊 Progress:")
    print("-"*70)
    
    # Just download, don't load
    model_path = manager.download_model("tts_models/multilingual/multi-dataset/xtts_v2")
    
    print("-"*70)
    print()
    print("="*70)
    print("🎉 SUCCESS! Model Downloaded!")
    print("="*70)
    print()
    print(f"✅ Location: {model_path}")
    print()
    print("⚠️  Model is downloaded but NOT loaded yet")
    print("   It will load when you start the app")
    print()
    print("Next: Run START_APP_E_DRIVE.bat")
    print()
    
except Exception as e:
    print()
    print("="*70)
    print("❌ ERROR")
    print("="*70)
    print(f"Error: {e}")
    print()
    
    if "not enough memory" in str(e).lower():
        print("⚠️  Still not enough RAM")
        print()
        print("Your system has 8GB RAM but only ~2.7GB free")
        print("XTTS-v2 needs 4-6GB free to load")
        print()
        print("🔧 Options:")
        print()
        print("1. Restart computer (frees RAM)")
        print("2. Close all browsers and apps")
        print("3. Use Edge TTS (no RAM needed)")
        print()
    else:
        print("Try:")
        print("1. Check internet connection")
        print("2. Run again")
    
    print()
    import traceback
    traceback.print_exc()
    sys.exit(1)
