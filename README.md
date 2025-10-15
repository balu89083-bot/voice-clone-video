# Voice Cloning and Video Integration

Free, high-quality voice cloning using Coqui TTS (XTTS-v2) and automatic video integration.

## Features

- ✅ **Free & Open Source** - No API keys or paid services required
- ✅ **High Quality Voice Cloning** - Using state-of-the-art XTTS-v2 model
- ✅ **Multi-language Support** - English, Hindi, Urdu, and 15+ other languages
- ✅ **Quick Cloning** - Only needs 6-10 seconds of reference audio
- ✅ **Video Integration** - Automatically adds cloned audio to videos
- ✅ **Easy to Use** - Simple Python interface

## Installation

### Step 1: Install Dependencies

```bash
pip install -r requirements.txt
```

**Note:** First run will download the XTTS-v2 model (~2GB). This is one-time only.

### Step 2: Prepare Your Files

You need:
1. **Reference Audio** - 6-10 seconds of clear voice recording (WAV/MP3)
2. **Input Video** - The video where you want to add the cloned voice
3. **Text** - The text you want to convert to speech

## Usage

### Method 1: Simple Mode (Recommended for Beginners)

1. Edit `main.py` and update the `simple_usage()` function:

```python
text = "Your text here"
reference_audio = "path/to/reference_voice.wav"
input_video = "path/to/input_video.mp4"
language = "en"  # "hi" for Hindi, "ur" for Urdu
```

2. Run:

```bash
python main.py
```

### Method 2: Command Line Mode

```bash
python main.py --text "Your text here" \
               --reference-audio reference_voice.wav \
               --video input_video.mp4 \
               --output output/final_video.mp4 \
               --language en
```

### Method 3: Use Individual Modules

#### Voice Cloning Only:

```python
from voice_cloner import VoiceCloner

cloner = VoiceCloner()
cloner.clone_voice(
    text="Your text here",
    reference_audio_path="reference_voice.wav",
    output_path="output_audio.wav",
    language="en"
)
```

#### Add Audio to Video Only:

```python
from video_processor import VideoProcessor

processor = VideoProcessor()
processor.add_audio_to_video(
    video_path="input_video.mp4",
    audio_path="cloned_audio.wav",
    output_path="final_video.mp4",
    replace_audio=True
)
```

## Supported Languages

- **en** - English
- **hi** - Hindi (हिंदी)
- **ur** - Urdu (اردو)
- **es** - Spanish
- **fr** - French
- **de** - German
- **it** - Italian
- **pt** - Portuguese
- **pl** - Polish
- **tr** - Turkish
- **ru** - Russian
- **nl** - Dutch
- **cs** - Czech
- **ar** - Arabic
- **zh-cn** - Chinese
- **ja** - Japanese
- **hu** - Hungarian
- **ko** - Korean

## Examples

### Example 1: English Voice Cloning

```bash
python main.py --text "Hello, this is a test of voice cloning" \
               --reference-audio my_voice.wav \
               --video my_video.mp4 \
               --language en
```

### Example 2: Hindi Voice Cloning

```bash
python main.py --text "यह एक टेस्ट है वॉइस क्लोनिंग का" \
               --reference-audio my_voice.wav \
               --video my_video.mp4 \
               --language hi
```

### Example 3: Urdu Voice Cloning

```bash
python main.py --text "یہ وائس کلوننگ کا ٹیسٹ ہے" \
               --reference-audio my_voice.wav \
               --video my_video.mp4 \
               --language ur
```

## Tips for Best Results

### Reference Audio Quality:
- ✅ Use clear, noise-free audio
- ✅ 6-10 seconds is ideal
- ✅ Single speaker only
- ✅ Natural speaking pace
- ❌ Avoid background music
- ❌ Avoid multiple speakers

### Text Input:
- Use proper punctuation for natural pauses
- Break long texts into sentences
- Match the language of reference audio

## Command Line Arguments

| Argument | Required | Description |
|----------|----------|-------------|
| `--text` | Yes | Text to convert to speech |
| `--reference-audio` | Yes | Reference audio file path |
| `--video` | Yes | Input video file path |
| `--output` | No | Output video path (default: output/final_video.mp4) |
| `--language` | No | Language code (default: en) |
| `--replace-audio` | No | Replace existing audio (default: True) |
| `--audio-start-time` | No | Audio start time in seconds (default: 0) |

## Troubleshooting

### Issue: Model download fails
**Solution:** Check internet connection. Model is ~2GB and downloads on first run.

### Issue: CUDA out of memory
**Solution:** The model will automatically use CPU if GPU memory is insufficient.

### Issue: Poor voice quality
**Solution:** 
- Use higher quality reference audio
- Ensure reference audio is 6-10 seconds
- Remove background noise from reference audio

### Issue: Video processing is slow
**Solution:** This is normal. Video encoding takes time. Use shorter videos for testing.

## System Requirements

- **Python:** 3.8 or higher
- **RAM:** 4GB minimum (8GB recommended)
- **Storage:** 3GB for model and dependencies
- **GPU:** Optional (CUDA-compatible GPU speeds up processing)

## Project Structure

```
voice-clone-video/
├── main.py              # Main pipeline script
├── voice_cloner.py      # Voice cloning module
├── video_processor.py   # Video processing module
├── requirements.txt     # Python dependencies
├── README.md           # This file
├── temp/               # Temporary files (auto-created)
└── output/             # Output videos (auto-created)
```

## License

This project uses open-source libraries:
- Coqui TTS (Mozilla Public License 2.0)
- MoviePy (MIT License)

## Credits

- **Coqui TTS** - Voice cloning technology
- **XTTS-v2** - State-of-the-art voice cloning model
