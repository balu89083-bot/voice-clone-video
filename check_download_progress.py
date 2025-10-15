"""
Check TTS Model Download Progress
Run this in a separate terminal to see download status
"""

import os
import sys
from pathlib import Path

# Fix encoding for Windows
if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

# TTS models are downloaded to this location
tts_cache = Path.home() / ".local" / "share" / "tts"

print("="*60)
print("TTS Model Download Status")
print("="*60)

if not tts_cache.exists():
    print("\n❌ Model cache directory not found yet")
    print("   Download hasn't started or is in progress...")
    print(f"\n   Cache location: {tts_cache}")
else:
    print(f"\n✅ Cache directory exists: {tts_cache}")
    
    # Check for XTTS-v2 model
    xtts_path = tts_cache / "tts_models--multilingual--multi-dataset--xtts_v2"
    
    if xtts_path.exists():
        print("\n✅ XTTS-v2 model found!")
        
        # Calculate total size
        total_size = 0
        file_count = 0
        
        for file in xtts_path.rglob("*"):
            if file.is_file():
                total_size += file.stat().st_size
                file_count += 1
        
        size_mb = total_size / (1024 * 1024)
        size_gb = size_mb / 1024
        
        print(f"   Files: {file_count}")
        print(f"   Size: {size_mb:.2f} MB ({size_gb:.2f} GB)")
        
        if size_gb > 1.5:
            print("\n🎉 Model fully downloaded! (~2GB)")
            print("   Server should start soon...")
        else:
            print(f"\n⏳ Download in progress... ({size_gb:.2f} GB / ~2 GB)")
            print("   Please wait...")
    else:
        print("\n⏳ XTTS-v2 model not found yet")
        print("   Download in progress or hasn't started...")

print("\n" + "="*60)
print("\nTo monitor in real-time:")
print("1. Check the terminal where app.py is running")
print("2. Look for download progress messages")
print("3. Or run this script again in a few minutes")
print("="*60)
