import os
from pathlib import Path

try:
    from moviepy.editor import VideoFileClip, AudioFileClip, CompositeAudioClip
except ImportError:
    # Try alternative import for newer moviepy versions
    try:
        from moviepy import VideoFileClip, AudioFileClip, CompositeAudioClip
    except ImportError:
        print("Warning: moviepy not properly installed. Video processing may not work.")
        VideoFileClip = None
        AudioFileClip = None
        CompositeAudioClip = None


class VideoProcessor:
    """
    Process videos and add audio
    """
    
    def __init__(self):
        """Initialize video processor"""
        pass
    
    def add_audio_to_video(self, video_path, audio_path, output_path, 
                          replace_audio=True, audio_start_time=0):
        """
        Add audio to video
        
        Args:
            video_path (str): Path to input video
            audio_path (str): Path to audio file to add
            output_path (str): Path to save output video
            replace_audio (bool): If True, replace existing audio. If False, mix with existing audio
            audio_start_time (float): Time in seconds when audio should start in video
        
        Returns:
            str: Path to output video
        """
        print(f"\n🎬 Processing video: {video_path}")
        print(f"🎵 Adding audio: {audio_path}")
        
        # Load video and audio
        video = VideoFileClip(video_path)
        audio = AudioFileClip(audio_path)
        
        # Get durations
        video_duration = video.duration
        audio_duration = audio.duration
        
        print(f"📊 Video duration: {video_duration:.2f} seconds")
        print(f"🎙️ Audio duration: {audio_duration:.2f} seconds")
        
        # Set audio start time
        if audio_start_time > 0:
            audio = audio.set_start(audio_start_time)
            print(f"⏰ Audio starts at: {audio_start_time:.2f} seconds")
        
        # Calculate final video duration
        audio_end_time = audio_start_time + audio_duration
        
        # Handle duration mismatch
        if audio_end_time > video_duration:
            # Audio is longer than video - extend video
            print(f"⚠️ Audio ({audio_end_time:.2f}s) is longer than video ({video_duration:.2f}s)")
            print(f"🔄 Extending video to match audio duration...")
            
            # Loop the video to match audio duration
            from moviepy.video.fx.loop import loop
            loops_needed = int(audio_end_time / video_duration) + 1
            video = loop(video, n=loops_needed)
            
            # Trim to exact audio end time
            video = video.subclip(0, audio_end_time)
            
            print(f"✅ Video extended to {audio_end_time:.2f} seconds")
            
        elif audio_end_time < video_duration:
            # Video is longer than audio - trim video to match audio
            print(f"⚠️ Video ({video_duration:.2f}s) is longer than audio ({audio_end_time:.2f}s)")
            print(f"✂️ Trimming video to match audio duration...")
            
            # Trim video to audio duration
            video = video.subclip(0, audio_end_time)
            
            print(f"✅ Video trimmed to {audio_end_time:.2f} seconds")
        else:
            # Perfect match
            print(f"✅ Video and audio durations match perfectly ({audio_end_time:.2f}s)")
        
        # Ensure output directory exists
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        
        if replace_audio:
            # Replace existing audio with new audio
            final_video = video.without_audio().set_audio(audio)
        else:
            # Mix new audio with existing audio
            if video.audio is not None:
                mixed_audio = CompositeAudioClip([video.audio, audio])
                final_video = video.without_audio().set_audio(mixed_audio)
            else:
                final_video = video.set_audio(audio)
        
        # Write output video
        print("💾 Writing output video...")
        final_video.write_videofile(
            output_path,
            codec='libx264',
            audio_codec='aac',
            temp_audiofile='temp-audio.m4a',
            remove_temp=True,
            fps=video.fps,
            preset='medium',
            threads=4
        )
        
        # Close clips
        video.close()
        audio.close()
        final_video.close()
        
        print(f"✅ Video saved successfully: {output_path}")
        print(f"📊 Final video duration: {audio_end_time:.2f} seconds")
        return output_path
    
    def replace_audio_segment(self, video_path, audio_path, output_path, 
                             start_time, end_time=None):
        """
        Replace a specific segment of video audio
        
        Args:
            video_path (str): Path to input video
            audio_path (str): Path to new audio
            output_path (str): Path to save output video
            start_time (float): Start time in seconds
            end_time (float): End time in seconds (None = until audio ends)
        
        Returns:
            str: Path to output video
        """
        print(f"\nReplacing audio segment from {start_time}s")
        
        video = VideoFileClip(video_path)
        new_audio = AudioFileClip(audio_path)
        
        if end_time is None:
            end_time = start_time + new_audio.duration
        
        # Get original audio
        original_audio = video.audio
        
        if original_audio is not None:
            # Split original audio into parts
            audio_before = original_audio.subclip(0, start_time) if start_time > 0 else None
            audio_after = original_audio.subclip(end_time, video.duration) if end_time < video.duration else None
            
            # Set timing for new audio
            new_audio = new_audio.set_start(start_time)
            
            # Combine audio parts
            audio_parts = [part for part in [audio_before, new_audio, audio_after] if part is not None]
            final_audio = CompositeAudioClip(audio_parts)
        else:
            final_audio = new_audio.set_start(start_time)
        
        # Create final video
        final_video = video.set_audio(final_audio)
        
        # Ensure output directory exists
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        
        # Write output
        print("Writing output video...")
        final_video.write_videofile(
            output_path,
            codec='libx264',
            audio_codec='aac',
            temp_audiofile='temp-audio.m4a',
            remove_temp=True,
            fps=video.fps
        )
        
        # Close clips
        video.close()
        new_audio.close()
        final_video.close()
        
        print(f"✓ Video saved successfully: {output_path}")
        return output_path
    
    def get_video_info(self, video_path):
        """
        Get video information
        
        Args:
            video_path (str): Path to video
        
        Returns:
            dict: Video information
        """
        video = VideoFileClip(video_path)
        info = {
            'duration': video.duration,
            'fps': video.fps,
            'size': video.size,
            'has_audio': video.audio is not None
        }
        video.close()
        return info


def main():
    """Example usage"""
    processor = VideoProcessor()
    
    # Example: Add audio to video
    video_path = "input_video.mp4"
    audio_path = "cloned_audio.wav"
    output_path = "output/final_video.mp4"
    
    processor.add_audio_to_video(
        video_path=video_path,
        audio_path=audio_path,
        output_path=output_path,
        replace_audio=True  # Set to False to mix with existing audio
    )


if __name__ == "__main__":
    main()
