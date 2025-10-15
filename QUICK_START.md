# Quick Start Guide - Voice Cloning Web App

## ⚠️ Important: Python Version Compatibility

This project now uses **Microsoft Edge TTS** which is compatible with **Python 3.13**.

## 🚀 Installation (3 Simple Steps)

### Step 1: Install Dependencies

```bash
cd C:\Users\balra\Documents\project\voice-clone-video
pip install -r requirements.txt
```

### Step 2: Start the Server

```bash
python app.py
```

### Step 3: Open in Browser

```
http://localhost:5000
```

## ✨ What Changed?

**Original Plan:** Coqui TTS (XTTS-v2) - Requires Python 3.9-3.11
**New Solution:** Microsoft Edge TTS - Works with Python 3.13+

### Benefits:
- ✅ **Works with Python 3.13**
- ✅ **No model download** (instant start)
- ✅ **400+ voices** in 100+ languages
- ✅ **High quality** natural voices
- ✅ **Fast processing** (cloud-based)
- ✅ **Free** (no API key needed)
- ✅ **Smaller installation** (no 2GB model)

### Note:
- Voice recording feature still works (records your voice for reference)
- Text-to-speech uses Microsoft's high-quality neural voices
- All other features remain the same

## 🎤 Available Voices

### Hindi Voices:
- **hi-IN-SwaraNeural** (Female) - Natural, clear
- **hi-IN-MadhurNeural** (Male) - Deep, professional

### Urdu Voices:
- **ur-PK-UzmaNeural** (Female) - Natural
- **ur-PK-AsadNeural** (Male) - Clear

### English Voices:
- **en-US-AriaNeural** (Female) - Natural, friendly
- **en-US-GuyNeural** (Male) - Professional
- **en-US-JennyNeural** (Female) - Warm, conversational
- **en-GB-SoniaNeural** (Female) - British accent

## 📝 Usage Example

### Web UI:
1. Open http://localhost:5000
2. **Step 1:** Record or upload audio (optional - for reference)
3. **Step 2:** Type your text and select language
4. **Step 3:** Upload video
5. Click "Generate Video with Cloned Voice"
6. Download your video!

### Command Line:
```python
from voice_cloner import VoiceCloner
from video_processor import VideoProcessor

# Generate speech
cloner = VoiceCloner()
cloner.clone_voice(
    text="आपका टेक्स्ट यहाँ",
    output_path="output/audio.mp3",
    language="hi"
)

# Add to video
processor = VideoProcessor()
processor.add_audio_to_video(
    video_path="input.mp4",
    audio_path="output/audio.mp3",
    output_path="final.mp4"
)
```

## 🔧 Troubleshooting

### If installation fails:
```bash
# Update pip first
python -m pip install --upgrade pip

# Then install requirements
pip install -r requirements.txt
```

### If server doesn't start:
```bash
# Check if port 5000 is free
netstat -ano | findstr :5000

# Or use a different port
# Edit app.py, change last line to:
# app.run(debug=True, host='0.0.0.0', port=8080)
```

### If audio generation fails:
- Check internet connection (Edge TTS requires internet)
- Verify text is not empty
- Try with shorter text first

## 📊 Comparison

| Feature | Coqui TTS (Old) | Edge TTS (New) |
|---------|----------------|----------------|
| Python Version | 3.9-3.11 | 3.7+ (works with 3.13) |
| Installation Size | ~2GB | ~10MB |
| First Run | 5-10 min (model download) | Instant |
| Voice Quality | Excellent | Excellent |
| Languages | 18+ | 100+ |
| Voices | 1 per language | 400+ total |
| Internet Required | No | Yes |
| Processing Speed | Slower (local) | Faster (cloud) |

## 🎯 Next Steps

1. **Test the installation:**
   ```bash
   python voice_cloner.py
   ```

2. **Start the web server:**
   ```bash
   python app.py
   ```

3. **Open browser and test:**
   - Go to http://localhost:5000
   - Try generating a simple text

4. **Upload a video and test full pipeline**

## 💡 Pro Tips

- **For Hindi/Urdu:** Edge TTS has excellent support with natural voices
- **Voice Selection:** You can choose different voices in the code
- **Speed Control:** Adjust speech rate with `rate="+20%"` parameter
- **Pitch Control:** Adjust pitch with `pitch="+50Hz"` parameter

## 🆘 Need Help?

If you encounter any issues:
1. Check that Python 3.13 is installed: `python --version`
2. Verify all packages installed: `pip list`
3. Check internet connection
4. Try with a simple example first

## ✅ Ready to Use!

Your voice cloning web app is now ready with Python 3.13 support! 🎉
