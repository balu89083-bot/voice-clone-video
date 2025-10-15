# 🚀 Free Hosting Deployment Guide

## 📋 Prerequisites:
- GitHub account
- Your voice-clone-video project

---

## Option 1: Render.com (Easiest) ⭐

### Step 1: Prepare Files

Create `render.yaml`:
```yaml
services:
  - type: web
    name: voice-clone-video
    env: python
    buildCommand: pip install -r requirements.txt
    startCommand: python app.py
    envVars:
      - key: PYTHON_VERSION
        value: 3.11.0
      - key: PORT
        value: 5000
```

### Step 2: Deploy
1. Go to https://render.com
2. Sign up (free)
3. Click "New" → "Web Service"
4. Connect GitHub repo
5. Select your repo
6. Click "Create Web Service"
7. Wait 5-10 minutes
8. Done! ✅

**Free Tier:**
- 750 hours/month
- Sleeps after 15 min inactivity
- 512 MB RAM

---

## Option 2: Railway.app ⭐

### Step 1: Deploy
1. Go to https://railway.app
2. Sign up with GitHub
3. Click "New Project"
4. Select "Deploy from GitHub repo"
5. Choose your repo
6. Railway auto-detects Python
7. Done! ✅

**Free Tier:**
- $5 credit/month
- ~500 hours
- No sleep mode

---

## Option 3: Hugging Face Spaces (Best for AI) ⭐⭐⭐

### Step 1: Convert to Gradio

Create `app_gradio.py`:
```python
import gradio as gr
from voice_cloner import VoiceCloner
from video_processor_ffmpeg import VideoProcessor

def process_video(video, audio, text, language):
    # Your existing logic
    cloner = VoiceCloner()
    processor = VideoProcessor()
    
    # Clone voice
    cloned_audio = cloner.clone_voice(text, audio, "output.wav", language)
    
    # Add to video
    output = processor.add_audio_to_video(video, cloned_audio, "output.mp4")
    
    return output

# Gradio interface
interface = gr.Interface(
    fn=process_video,
    inputs=[
        gr.Video(label="Upload Video"),
        gr.Audio(label="Reference Voice", type="filepath"),
        gr.Textbox(label="Text to Speak"),
        gr.Dropdown(["en", "hi", "ur"], label="Language")
    ],
    outputs=gr.Video(label="Output Video"),
    title="🎙️ Voice Clone Video Generator",
    description="Clone any voice and add it to your video!"
)

interface.launch()
```

### Step 2: Deploy
1. Go to https://huggingface.co/spaces
2. Click "Create new Space"
3. Choose "Gradio"
4. Upload your code
5. Add `requirements.txt`
6. Done! ✅

**Free Tier:**
- Unlimited usage
- GPU support (free!)
- No sleep mode
- Perfect for AI apps

---

## Option 4: PythonAnywhere (Simple)

### Step 1: Deploy
1. Go to https://www.pythonanywhere.com
2. Sign up (free)
3. Upload files via Files tab
4. Install requirements: `pip install -r requirements.txt`
5. Configure web app
6. Done! ✅

**Free Tier:**
- Always on
- Limited CPU
- 512 MB storage

---

## 🎯 Recommendation:

### For Quick Deploy:
**Use Render.com** - Easiest, 5 minutes

### For AI/ML Apps:
**Use Hugging Face Spaces** - Free GPU, perfect for TTS

### For Always-On:
**Use Railway.app** - No sleep mode

---

## ⚠️ Important Notes:

### 1. Model Size Issue:
XTTS-v2 model is ~2GB. Free hosting may have issues.

**Solution:**
- Use model caching
- Or use lighter model
- Or use edge-tts (already in requirements.txt)

### 2. FFmpeg Requirement:
Most platforms don't have FFmpeg pre-installed.

**Solution:**
Add to `requirements.txt`:
```
ffmpeg-python
```

Or use buildpack for Render/Railway.

### 3. Memory Limits:
Free tiers have 512MB-1GB RAM limit.

**Solution:**
- Use CPU mode (already set)
- Clear memory after each request
- Limit concurrent users

---

## 📦 Files Needed for Deployment:

1. **requirements.txt** ✅ (Already exists)
2. **Procfile** (for Render/Railway)
3. **render.yaml** (for Render)
4. **runtime.txt** (Python version)

Let me create these files for you!
