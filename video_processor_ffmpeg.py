"""
Video Processor using FFmpeg directly
More reliable than moviepy for audio replacement
"""

import os
import subprocess
import json


class VideoProcessor:
    """
    Process videos and add audio using FFmpeg
    """
    
    def __init__(self, ffmpeg_path=None):
        """Initialize video processor"""
        if ffmpeg_path is None:
            # Use FFmpeg from project folder
            self.ffmpeg_path = r"D:\voice-clone-video\ffmpeg-master-latest-win64-gpl-shared\ffmpeg-master-latest-win64-gpl-shared\bin\ffmpeg.exe"
        else:
            self.ffmpeg_path = ffmpeg_path
    
    def add_audio_to_video(self, video_path, audio_path, output_path, 
                          replace_audio=True, audio_start_time=0):
        """
        Add audio to video using FFmpeg
        
        Args:
            video_path (str): Path to input video
            audio_path (str): Path to audio file to add
            output_path (str): Path to save output video
            replace_audio (bool): If True, replace existing audio. If False, mix with existing audio
            audio_start_time (float): Time in seconds when audio should start in video
        
        Returns:
            str: Path to output video
        """
        print(f"\nProcessing video with FFmpeg: {video_path}")
        print(f"Adding audio: {audio_path}")
        
        # Ensure output directory exists
        os.makedirs(os.path.dirname(output_path) if os.path.dirname(output_path) else '.', exist_ok=True)
        
        try:
            if replace_audio:
                # Replace audio completely
                if audio_start_time > 0:
                    # Delay audio start
                    cmd = [
                        self.ffmpeg_path,
                        '-i', video_path,
                        '-itsoffset', str(audio_start_time),
                        '-i', audio_path,
                        '-c:v', 'copy',
                        '-map', '0:v:0',
                        '-map', '1:a:0',
                        '-shortest',
                        '-y',
                        output_path
                    ]
                else:
                    # Audio replacement with enhancement (noise removal + volume boost)
                    print("🎙️ Applying audio enhancements:")
                    print("   - Noise reduction (highpass filter)")
                    print("   - Volume normalization")
                    print("   - Clarity enhancement")
                    
                    # Audio filter chain for better quality
                    audio_filters = [
                        'highpass=f=200',           # Remove low-frequency noise/rumble
                        'lowpass=f=3000',           # Remove high-frequency noise (keep voice clarity)
                        'afftdn=nf=-25',            # Noise reduction (FFT denoiser)
                        'volume=3.5',               # Boost volume by 3.5x (LOUD!)
                        'loudnorm=I=-14:TP=-1:LRA=11',  # Normalize loudness (louder broadcast level)
                        'acompressor=threshold=0.089:ratio=9:attack=200:release=1000'  # Gentle compression
                    ]
                    
                    filter_string = ','.join(audio_filters)
                    
                    cmd = [
                        self.ffmpeg_path,
                        '-i', video_path,
                        '-i', audio_path,
                        '-c:v', 'copy',
                        '-map', '0:v:0',
                        '-map', '1:a:0',
                        '-af', filter_string,       # Apply audio filters
                        '-c:a', 'aac',              # Encode audio as AAC
                        '-b:a', '192k',             # High quality audio bitrate
                        '-shortest',
                        '-y',
                        output_path
                    ]
            else:
                # Mix audio with existing
                cmd = [
                    self.ffmpeg_path,
                    '-i', video_path,
                    '-i', audio_path,
                    '-filter_complex', f'[0:a][1:a]amix=inputs=2:duration=first[aout]',
                    '-map', '0:v',
                    '-map', '[aout]',
                    '-c:v', 'copy',
                    '-c:a', 'aac',
                    '-y',
                    output_path
                ]
            
            # Run FFmpeg
            print("Running FFmpeg...")
            result = subprocess.run(
                cmd,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
                encoding='utf-8',
                errors='replace'
            )
            
            if result.returncode == 0:
                print(f"✅ Video saved successfully: {output_path}")
                return output_path
            else:
                error_msg = result.stderr
                print(f"❌ FFmpeg error: {error_msg}")
                raise Exception(f"FFmpeg failed: {error_msg}")
                
        except Exception as e:
            print(f"❌ Error processing video: {e}")
            raise
    
    def get_video_info(self, video_path):
        """
        Get video information using FFprobe
        
        Args:
            video_path (str): Path to video
        
        Returns:
            dict: Video information
        """
        ffprobe_path = self.ffmpeg_path.replace('ffmpeg.exe', 'ffprobe.exe')
        
        cmd = [
            ffprobe_path,
            '-v', 'quiet',
            '-print_format', 'json',
            '-show_format',
            '-show_streams',
            video_path
        ]
        
        try:
            result = subprocess.run(
                cmd,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True
            )
            
            if result.returncode == 0:
                data = json.loads(result.stdout)
                
                # Extract video stream info
                video_stream = next((s for s in data['streams'] if s['codec_type'] == 'video'), None)
                audio_stream = next((s for s in data['streams'] if s['codec_type'] == 'audio'), None)
                
                info = {
                    'duration': float(data['format'].get('duration', 0)),
                    'size': (
                        int(video_stream.get('width', 0)),
                        int(video_stream.get('height', 0))
                    ) if video_stream else (0, 0),
                    'fps': eval(video_stream.get('r_frame_rate', '0/1')) if video_stream else 0,
                    'has_audio': audio_stream is not None
                }
                
                return info
            else:
                return {
                    'duration': 0,
                    'size': (0, 0),
                    'fps': 0,
                    'has_audio': False
                }
                
        except Exception as e:
            print(f"Error getting video info: {e}")
            return {
                'duration': 0,
                'size': (0, 0),
                'fps': 0,
                'has_audio': False
            }


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
        replace_audio=True
    )


if __name__ == "__main__":
    main()
