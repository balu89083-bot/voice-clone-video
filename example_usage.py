"""
Example Usage Scripts
Different ways to use the voice cloning and video integration
"""

from voice_cloner import VoiceCloner
from video_processor import VideoProcessor


def example_1_basic_usage():
    """
    Example 1: Basic usage - Clone voice and add to video
    """
    print("\n" + "="*60)
    print("Example 1: Basic Voice Cloning and Video Integration")
    print("="*60)
    
    # Initialize
    cloner = VoiceCloner()
    processor = VideoProcessor()
    
    # Step 1: Clone voice
    text = "Hello, this is a demonstration of voice cloning technology."
    cloner.clone_voice(
        text=text,
        reference_audio_path="reference_voice.wav",
        output_path="temp/cloned_audio.wav",
        language="en"
    )
    
    # Step 2: Add to video
    processor.add_audio_to_video(
        video_path="input_video.mp4",
        audio_path="temp/cloned_audio.wav",
        output_path="output/example1_output.mp4",
        replace_audio=True
    )
    
    print("\n✓ Example 1 completed!")


def example_2_hindi_urdu():
    """
    Example 2: Hindi/Urdu voice cloning
    """
    print("\n" + "="*60)
    print("Example 2: Hindi/Urdu Voice Cloning")
    print("="*60)
    
    cloner = VoiceCloner()
    processor = VideoProcessor()
    
    # Hindi example
    hindi_text = "नमस्ते, यह वॉइस क्लोनिंग टेक्नोलॉजी का एक उदाहरण है।"
    cloner.clone_voice(
        text=hindi_text,
        reference_audio_path="reference_voice.wav",
        output_path="temp/hindi_audio.wav",
        language="hi"
    )
    
    # Add to video
    processor.add_audio_to_video(
        video_path="input_video.mp4",
        audio_path="temp/hindi_audio.wav",
        output_path="output/example2_hindi.mp4",
        replace_audio=True
    )
    
    print("\n✓ Example 2 completed!")


def example_3_mix_audio():
    """
    Example 3: Mix cloned voice with existing video audio
    """
    print("\n" + "="*60)
    print("Example 3: Mix Audio (Keep Original + Add Cloned Voice)")
    print("="*60)
    
    cloner = VoiceCloner()
    processor = VideoProcessor()
    
    # Clone voice
    text = "This audio will be mixed with the original video audio."
    cloner.clone_voice(
        text=text,
        reference_audio_path="reference_voice.wav",
        output_path="temp/cloned_audio.wav",
        language="en"
    )
    
    # Mix with existing audio (don't replace)
    processor.add_audio_to_video(
        video_path="input_video.mp4",
        audio_path="temp/cloned_audio.wav",
        output_path="output/example3_mixed.mp4",
        replace_audio=False  # Keep original audio and mix
    )
    
    print("\n✓ Example 3 completed!")


def example_4_delayed_audio():
    """
    Example 4: Add audio at specific time in video
    """
    print("\n" + "="*60)
    print("Example 4: Add Audio at Specific Time")
    print("="*60)
    
    cloner = VoiceCloner()
    processor = VideoProcessor()
    
    # Clone voice
    text = "This audio will start at 5 seconds into the video."
    cloner.clone_voice(
        text=text,
        reference_audio_path="reference_voice.wav",
        output_path="temp/cloned_audio.wav",
        language="en"
    )
    
    # Add audio starting at 5 seconds
    processor.add_audio_to_video(
        video_path="input_video.mp4",
        audio_path="temp/cloned_audio.wav",
        output_path="output/example4_delayed.mp4",
        replace_audio=True,
        audio_start_time=5.0  # Start at 5 seconds
    )
    
    print("\n✓ Example 4 completed!")


def example_5_batch_processing():
    """
    Example 5: Process multiple texts
    """
    print("\n" + "="*60)
    print("Example 5: Batch Processing Multiple Texts")
    print("="*60)
    
    cloner = VoiceCloner()
    
    # Multiple texts
    texts = [
        "This is the first sentence.",
        "This is the second sentence.",
        "This is the third sentence."
    ]
    
    # Clone all voices
    audio_paths = cloner.clone_voice_batch(
        texts=texts,
        reference_audio_path="reference_voice.wav",
        output_dir="temp/batch",
        language="en"
    )
    
    print(f"\n✓ Generated {len(audio_paths)} audio files!")
    for i, path in enumerate(audio_paths):
        print(f"  {i+1}. {path}")


def example_6_replace_segment():
    """
    Example 6: Replace specific segment of video audio
    """
    print("\n" + "="*60)
    print("Example 6: Replace Audio Segment")
    print("="*60)
    
    cloner = VoiceCloner()
    processor = VideoProcessor()
    
    # Clone voice
    text = "This will replace audio from 2 to 7 seconds."
    cloner.clone_voice(
        text=text,
        reference_audio_path="reference_voice.wav",
        output_path="temp/cloned_audio.wav",
        language="en"
    )
    
    # Replace audio segment
    processor.replace_audio_segment(
        video_path="input_video.mp4",
        audio_path="temp/cloned_audio.wav",
        output_path="output/example6_segment.mp4",
        start_time=2.0,  # Start at 2 seconds
        end_time=7.0     # End at 7 seconds
    )
    
    print("\n✓ Example 6 completed!")


def example_7_video_info():
    """
    Example 7: Get video information
    """
    print("\n" + "="*60)
    print("Example 7: Get Video Information")
    print("="*60)
    
    processor = VideoProcessor()
    
    info = processor.get_video_info("input_video.mp4")
    
    print("\nVideo Information:")
    print(f"  Duration: {info['duration']:.2f} seconds")
    print(f"  FPS: {info['fps']}")
    print(f"  Size: {info['size']}")
    print(f"  Has Audio: {info['has_audio']}")
    
    print("\n✓ Example 7 completed!")


def main():
    """Run all examples"""
    print("\n" + "="*60)
    print("Voice Cloning and Video Integration - Examples")
    print("="*60)
    print("\nAvailable Examples:")
    print("1. Basic usage - Clone voice and add to video")
    print("2. Hindi/Urdu voice cloning")
    print("3. Mix audio (keep original + add cloned)")
    print("4. Add audio at specific time")
    print("5. Batch processing multiple texts")
    print("6. Replace specific audio segment")
    print("7. Get video information")
    
    choice = input("\nEnter example number (1-7) or 'all' to run all: ")
    
    examples = {
        '1': example_1_basic_usage,
        '2': example_2_hindi_urdu,
        '3': example_3_mix_audio,
        '4': example_4_delayed_audio,
        '5': example_5_batch_processing,
        '6': example_6_replace_segment,
        '7': example_7_video_info
    }
    
    if choice.lower() == 'all':
        for func in examples.values():
            try:
                func()
            except Exception as e:
                print(f"\n❌ Error: {e}")
    elif choice in examples:
        try:
            examples[choice]()
        except Exception as e:
            print(f"\n❌ Error: {e}")
    else:
        print("\n❌ Invalid choice!")


if __name__ == "__main__":
    main()
