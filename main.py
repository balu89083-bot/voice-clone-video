"""
Voice Cloning and Video Integration
Complete pipeline for cloning voice and adding to video
"""

import os
import argparse
from pathlib import Path
from voice_cloner import VoiceCloner
from video_processor import VideoProcessor


def main():
    """Main pipeline"""
    parser = argparse.ArgumentParser(description='Voice Cloning and Video Integration')
    parser.add_argument('--text', type=str, required=True, help='Text to convert to speech')
    parser.add_argument('--reference-audio', type=str, required=True, help='Reference audio file for voice cloning')
    parser.add_argument('--video', type=str, required=True, help='Input video file')
    parser.add_argument('--output', type=str, default='output/final_video.mp4', help='Output video file')
    parser.add_argument('--language', type=str, default='en', 
                       help='Language code (en, hi, ur, es, fr, de, it, pt, pl, tr, ru, nl, cs, ar, zh-cn, ja, hu, ko)')
    parser.add_argument('--replace-audio', action='store_true', help='Replace existing audio (default: True)')
    parser.add_argument('--audio-start-time', type=float, default=0, help='Audio start time in seconds')
    parser.add_argument('--temp-audio', type=str, default='temp/cloned_audio.wav', help='Temporary audio file path')
    
    args = parser.parse_args()
    
    print("=" * 60)
    print("Voice Cloning and Video Integration Pipeline")
    print("=" * 60)
    
    # Step 1: Clone voice and generate audio
    print("\n[Step 1/2] Cloning voice and generating audio...")
    cloner = VoiceCloner()
    
    audio_path = cloner.clone_voice(
        text=args.text,
        reference_audio_path=args.reference_audio,
        output_path=args.temp_audio,
        language=args.language
    )
    
    # Step 2: Add audio to video
    print("\n[Step 2/2] Adding audio to video...")
    processor = VideoProcessor()
    
    output_video = processor.add_audio_to_video(
        video_path=args.video,
        audio_path=audio_path,
        output_path=args.output,
        replace_audio=args.replace_audio,
        audio_start_time=args.audio_start_time
    )
    
    print("\n" + "=" * 60)
    print("✓ Pipeline completed successfully!")
    print(f"✓ Output video: {output_video}")
    print("=" * 60)


def simple_usage():
    """Simple usage without command line arguments"""
    print("=" * 60)
    print("Voice Cloning and Video Integration - Simple Mode")
    print("=" * 60)
    
    # Configuration
    text = "Hello, this is a test of voice cloning technology."
    reference_audio = "reference_voice.wav"  # Your reference audio (6-10 seconds)
    input_video = "input_video.mp4"  # Your input video
    output_video = "output/final_video.mp4"
    language = "en"  # Change to "hi" for Hindi, "ur" for Urdu
    
    # For Hindi/Urdu example:
    # text = "यह एक टेस्ट है वॉइस क्लोनिंग का"
    # language = "hi"
    
    print(f"\nText: {text}")
    print(f"Reference Audio: {reference_audio}")
    print(f"Input Video: {input_video}")
    print(f"Language: {language}")
    
    # Step 1: Clone voice
    print("\n[Step 1/2] Cloning voice...")
    cloner = VoiceCloner()
    temp_audio = "temp/cloned_audio.wav"
    
    audio_path = cloner.clone_voice(
        text=text,
        reference_audio_path=reference_audio,
        output_path=temp_audio,
        language=language
    )
    
    # Step 2: Add to video
    print("\n[Step 2/2] Adding audio to video...")
    processor = VideoProcessor()
    
    processor.add_audio_to_video(
        video_path=input_video,
        audio_path=audio_path,
        output_path=output_video,
        replace_audio=True
    )
    
    print("\n" + "=" * 60)
    print("✓ Done! Check your output video.")
    print("=" * 60)


if __name__ == "__main__":
    import sys
    
    if len(sys.argv) > 1:
        # Command line mode
        main()
    else:
        # Simple mode - edit the simple_usage() function above
        print("\nNo arguments provided. Using simple mode.")
        print("Edit the simple_usage() function in main.py to configure your settings.\n")
        simple_usage()
