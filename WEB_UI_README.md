# Voice Cloning Web UI - Complete Guide

Beautiful web interface for voice cloning and video integration with built-in voice recorder!

## 🎨 Features

### ✨ Modern UI
- Beautiful gradient design
- Responsive layout (works on mobile & desktop)
- Step-by-step guided process
- Real-time progress tracking
- Animated visualizations

### 🎤 Voice Recording
- **Built-in Voice Recorder** - Record directly in browser
- **Audio Visualizer** - See your voice in real-time
- **Recording Timer** - Track recording duration
- **Audio Preview** - Listen before processing
- **Upload Option** - Or upload existing audio files

### 📝 Text Input
- Multi-language support (18+ languages)
- Character counter
- Large text area for long content
- Support for Hindi, Urdu, English, and more

### 🎬 Video Upload
- Drag & drop video upload
- Video preview player
- Video information display (duration, FPS, size)
- Multiple format support (MP4, AVI, MOV, etc.)

### ⚙️ Advanced Options
- Replace or mix audio
- Set audio start time
- Language selection
- Real-time validation

## 🚀 Quick Start

### Step 1: Install Dependencies

```bash
cd C:\Users\balra\Documents\project\voice-clone-video
pip install -r requirements.txt
```

### Step 2: Run the Web Server

```bash
python app.py
```

### Step 3: Open in Browser

Open your browser and go to:
```
http://localhost:5000
```

## 📖 How to Use

### Method 1: Record Voice (Recommended)

1. **Step 1 - Reference Voice:**
   - Click "Start Recording" button
   - Speak clearly for 6-10 seconds
   - Click "Stop Recording"
   - Preview your recording
   - (Or upload an existing audio file)

2. **Step 2 - Text to Speech:**
   - Select language (English, Hindi, Urdu, etc.)
   - Type or paste your text
   - Use proper punctuation for natural pauses

3. **Step 3 - Video Upload:**
   - Click "Upload Video"
   - Select your video file
   - Preview will show automatically
   - Choose audio options (replace/mix)
   - Set audio start time if needed

4. **Generate:**
   - Click "Generate Video with Cloned Voice"
   - Wait for processing (progress bar shows status)
   - Download your final video!

### Method 2: Upload Audio File

1. In Step 1, instead of recording, click "Upload Audio File"
2. Select a 6-10 second audio file from your computer
3. Continue with Steps 2 and 3 as above

## 🌍 Supported Languages

The web UI supports 18+ languages:

| Language | Code | Example |
|----------|------|---------|
| English | en | Hello, this is a test |
| Hindi | hi | नमस्ते, यह एक टेस्ट है |
| Urdu | ur | یہ ایک ٹیسٹ ہے |
| Spanish | es | Hola, esto es una prueba |
| French | fr | Bonjour, ceci est un test |
| German | de | Hallo, das ist ein Test |
| Italian | it | Ciao, questo è un test |
| Portuguese | pt | Olá, este é um teste |
| Polish | pl | Cześć, to jest test |
| Turkish | tr | Merhaba, bu bir test |
| Russian | ru | Привет, это тест |
| Dutch | nl | Hallo, dit is een test |
| Czech | cs | Ahoj, toto je test |
| Arabic | ar | مرحبا، هذا اختبار |
| Chinese | zh-cn | 你好，这是一个测试 |
| Japanese | ja | こんにちは、これはテストです |
| Hungarian | hu | Helló, ez egy teszt |
| Korean | ko | 안녕하세요, 이것은 테스트입니다 |

## 🎯 Tips for Best Results

### Recording Quality:
- ✅ Use a quiet environment
- ✅ Speak clearly and naturally
- ✅ Record 6-10 seconds (ideal length)
- ✅ Keep consistent volume
- ❌ Avoid background noise
- ❌ Don't speak too fast or slow

### Text Input:
- Use proper punctuation (. , ! ?)
- Break long sentences naturally
- Match language with reference audio
- Check spelling and grammar

### Video Upload:
- Supported formats: MP4, AVI, MOV, MKV, WEBM
- Max file size: 500MB
- Higher quality videos = better results

## 🔧 Advanced Features

### Audio Options:

**Replace Audio (Default):**
- Removes original video audio
- Adds only cloned voice
- Best for voiceovers

**Mix Audio:**
- Keeps original video audio
- Adds cloned voice on top
- Best for narration over music/effects

**Audio Start Time:**
- Set when cloned audio should start
- Measured in seconds
- Useful for syncing with video

## 📁 Project Structure

```
voice-clone-video/
├── app.py                  # Flask web server
├── voice_cloner.py         # Voice cloning module
├── video_processor.py      # Video processing module
├── templates/
│   └── index.html         # Web UI HTML
├── static/
│   ├── css/
│   │   └── style.css      # Beautiful styling
│   └── js/
│       └── app.js         # Frontend JavaScript
├── uploads/               # Uploaded files (auto-created)
├── outputs/               # Generated videos (auto-created)
└── temp/                  # Temporary files (auto-created)
```

## 🔒 Security & Privacy

- All processing happens locally on your machine
- No data sent to external servers
- Files stored temporarily during processing
- You can delete files after download

## 🐛 Troubleshooting

### Issue: Microphone not working
**Solution:** 
- Check browser permissions
- Allow microphone access when prompted
- Try a different browser (Chrome/Edge recommended)

### Issue: Video upload fails
**Solution:**
- Check file size (max 500MB)
- Ensure video format is supported
- Try converting to MP4 format

### Issue: Processing is slow
**Solution:**
- First run downloads model (~2GB) - one time only
- Video processing takes time (normal)
- Use shorter videos for testing
- GPU speeds up processing if available

### Issue: Page not loading
**Solution:**
- Check if server is running (`python app.py`)
- Try http://127.0.0.1:5000 instead
- Check firewall settings
- Restart the server

### Issue: Audio quality is poor
**Solution:**
- Use better quality reference audio
- Record in quiet environment
- Ensure 6-10 seconds of clear speech
- Remove background noise

## 💻 System Requirements

- **Python:** 3.8 or higher
- **RAM:** 4GB minimum (8GB recommended)
- **Storage:** 3GB for model and dependencies
- **Browser:** Chrome, Edge, Firefox, or Safari (latest versions)
- **Microphone:** Required for recording feature
- **GPU:** Optional (speeds up processing)

## 🎨 UI Features

### Visual Feedback:
- ✅ Step completion indicators
- ✅ Real-time character counter
- ✅ Audio waveform visualizer
- ✅ Video preview player
- ✅ Progress bar with percentage
- ✅ Status messages

### User Experience:
- Guided step-by-step process
- Clear instructions at each step
- Validation before processing
- Error messages if something goes wrong
- Download button after completion

## 🚀 Running on Network

To access from other devices on your network:

1. Find your local IP address:
```bash
ipconfig  # On Windows
```

2. Run the server:
```bash
python app.py
```

3. Access from other devices:
```
http://YOUR_IP_ADDRESS:5000
```

Example: `http://192.168.1.100:5000`

## 📱 Mobile Support

The web UI is fully responsive and works on:
- 📱 Smartphones
- 📱 Tablets
- 💻 Laptops
- 🖥️ Desktops

## 🎬 Example Workflow

1. **Record your voice** (6-10 seconds)
2. **Type your text** in Hindi/Urdu/English
3. **Upload your video**
4. **Click Generate**
5. **Wait 2-5 minutes** (depending on video length)
6. **Download** your final video!

## 🆘 Support

If you encounter any issues:

1. Check the console for error messages
2. Verify all files are uploaded correctly
3. Ensure text is not empty
4. Try with a shorter video first
5. Restart the server if needed

## 🎉 Enjoy!

You now have a professional voice cloning studio right in your browser!

**No API keys needed | Completely free | High quality results**
