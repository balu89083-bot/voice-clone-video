"""
Diagnostic script to check audio and video quality
"""
import wave
import os
import struct
import sys

# Fix encoding for Windows
if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

# File to check
audio_file = r"D:\voice-clone-video\temp\cloned_8fb96c36052741e7a3c8dad7ee87965b.wav"
video_file = r"D:\voice-clone-video\outputs\output_8fb96c36052741e7a3c8dad7ee87965b.mp4"

print("=" * 60)
print("🔍 AUDIO ANALYSIS")
print("=" * 60)

if os.path.exists(audio_file):
    # Load audio using wave module
    with wave.open(audio_file, 'rb') as wf:
        sr = wf.getframerate()
        n_frames = wf.getnframes()
        duration = n_frames / sr
        n_channels = wf.getnchannels()
        sample_width = wf.getsampwidth()
        
        print(f"✅ Audio file: {os.path.basename(audio_file)}")
        print(f"   Duration: {duration:.2f} seconds")
        print(f"   Sample rate: {sr} Hz")
        print(f"   Frames: {n_frames}")
        print(f"   Channels: {n_channels}")
        print(f"   Sample width: {sample_width} bytes")
        print(f"   File size: {os.path.getsize(audio_file)} bytes")
        
        # Read a sample to check levels
        wf.rewind()
        frames = wf.readframes(min(sr * 5, n_frames))  # Read first 5 seconds
        
        # Convert to samples
        if sample_width == 2:  # 16-bit
            samples = struct.unpack(f'{len(frames)//2}h', frames)
            max_val = 32768.0
        else:
            samples = []
            max_val = 1.0
        
        if samples:
            max_level = max(abs(s) for s in samples) / max_val
            
            print(f"\n📊 Audio Levels (first 5 seconds):")
            print(f"   Max level: {max_level:.4f}")
            
            if max_level < 0.1:
                print("   ⚠️ WARNING: Audio is very quiet!")
            elif max_level > 0.95:
                print("   ⚠️ WARNING: Audio might be clipping!")
            else:
                print("   ✅ Audio levels look good")
else:
    print(f"❌ Audio file not found: {audio_file}")

print("\n" + "=" * 60)
print("🎬 VIDEO FILE INFO")
print("=" * 60)

if os.path.exists(video_file):
    print(f"✅ Video file: {os.path.basename(video_file)}")
    print(f"   File size: {os.path.getsize(video_file) / 1024 / 1024:.2f} MB")
    print(f"   Path: {video_file}")
    print(f"\n💡 To check video, open it in a media player")
    print(f"   Or use VLC/Windows Media Player")
else:
    print(f"❌ Video file not found: {video_file}")

print("\n" + "=" * 60)
print("✅ Analysis Complete!")
print("=" * 60)
