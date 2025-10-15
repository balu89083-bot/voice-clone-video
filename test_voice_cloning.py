"""
Test Real Voice Cloning
Quick test to verify Coqui TTS is working
"""

import os
import sys

print("="*60)
print("Testing Real Voice Cloning Setup")
print("="*60)

# Test 1: Check TTS installation
print("\n[Test 1] Checking TTS installation...")
try:
    import TTS
    print(f"✅ TTS installed successfully! Version: {TTS.__version__}")
except ImportError as e:
    print(f"❌ TTS not installed: {e}")
    sys.exit(1)

# Test 2: Check PyTorch
print("\n[Test 2] Checking PyTorch...")
try:
    import torch
    print(f"✅ PyTorch installed! Version: {torch.__version__}")
    print(f"   CUDA available: {torch.cuda.is_available()}")
except ImportError as e:
    print(f"❌ PyTorch not installed: {e}")
    sys.exit(1)

# Test 3: Initialize Voice Cloner
print("\n[Test 3] Initializing Voice Cloner...")
try:
    from TTS.api import TTS
    print("✅ TTS API imported successfully!")
    
    print("\n[Test 4] Loading XTTS-v2 model...")
    print("⏳ This may take a few minutes on first run (downloading ~2GB model)...")
    
    device = "cuda" if torch.cuda.is_available() else "cpu"
    print(f"   Using device: {device}")
    
    tts = TTS("tts_models/multilingual/multi-dataset/xtts_v2").to(device)
    print("✅ Model loaded successfully!")
    
    print("\n" + "="*60)
    print("🎉 SUCCESS! Real Voice Cloning is Ready!")
    print("="*60)
    print("\nYou can now:")
    print("1. Run: start_with_cloning.bat")
    print("2. Open: http://localhost:5000")
    print("3. Record your voice and clone it!")
    print("="*60)
    
except Exception as e:
    print(f"❌ Error: {e}")
    print("\nTroubleshooting:")
    print("1. Make sure C++ Build Tools are installed")
    print("2. Restart your computer")
    print("3. Run: install_dependencies.bat")
    sys.exit(1)
