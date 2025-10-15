"""
Download TTS Model to D Drive with Memory Optimization
"""

import sys
import os
import gc

# Fix encoding
if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

# Set D drive cache BEFORE any imports
os.environ['TTS_HOME'] = 'D:\\tts_cache'
os.environ['COQUI_TOS_AGREED'] = '1'

# Memory optimization
os.environ['PYTORCH_CUDA_ALLOC_CONF'] = 'max_split_size_mb:32'
os.environ['OMP_NUM_THREADS'] = '1'

print("="*70)
print("🎤 Downloading XTTS-v2 to D Drive")
print("="*70)
print()
print("💾 Location: D:\\tts_cache")
print("📦 Size: ~2GB")
print("🧠 Memory: Optimized mode")
print()
print("⚠️  This will DOWNLOAD model only")
print("   Loading happens when you start the app")
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
    
    print("Step 3: Downloading model to D drive...")
    print("📊 Progress:")
    print("-"*70)
    
    # Download model to D drive
    model_path = manager.download_model("tts_models/multilingual/multi-dataset/xtts_v2")
    
    print("-"*70)
    print()
    print("="*70)
    print("🎉 SUCCESS! Model Downloaded to D Drive!")
    print("="*70)
    print()
    print(f"✅ Location: {model_path}")
    print(f"✅ Saved to: D:\\tts_cache")
    print()
    print("📝 Next Steps:")
    print("1. Restart your computer (to free RAM)")
    print("2. Run: START_APP_D_DRIVE.bat")
    print("3. Open: http://localhost:5000")
    print()
    
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
    print("3. Or use Edge TTS: python app.py")
    print()
    import traceback
    traceback.print_exc()
    sys.exit(1)
