# 🚀 Quick Deploy Guide - Free Hosting

## ✅ Files Created:
- `Procfile` - Tells server how to run app
- `runtime.txt` - Python version
- `render.yaml` - Render.com config
- `requirements.txt` - Already exists
- `app.py` - Updated for deployment

---

## 🎯 Easiest Option: Render.com (5 Minutes!)

### Step 1: Push to GitHub
```bash
cd D:\voice-clone-video
git init
git add .
git commit -m "Initial commit"
git remote add origin https://github.com/YOUR_USERNAME/voice-clone-video.git
git push -u origin main
```

### Step 2: Deploy on Render
1. Go to https://render.com
2. Sign up (free, use GitHub)
3. Click "New" → "Web Service"
4. Connect your GitHub repo
5. Render auto-detects settings from `render.yaml`
6. Click "Create Web Service"
7. Wait 5-10 minutes
8. **Done!** ✅

Your app will be live at: `https://voice-clone-video.onrender.com`

---

## ⚠️ Important: Model Size Issue

XTTS-v2 model is 2GB. Free hosting may fail to download it.

### Solution 1: Use Smaller Model (Recommended)
Already using edge-tts in requirements.txt - lightweight!

### Solution 2: Pre-download Model
Add to app.py startup:
```python
# Download model on first run
from TTS.api import TTS
tts = TTS("tts_models/multilingual/multi-dataset/xtts_v2")
```

### Solution 3: Use Hugging Face Spaces
They support large AI models better!

---

## 🎯 Alternative: Railway.app (Also Easy!)

### Step 1: Deploy
1. Go to https://railway.app
2. Sign up with GitHub
3. Click "New Project" → "Deploy from GitHub repo"
4. Select your repo
5. **Done!** ✅

Railway gives you $5 free credit/month (~500 hours)

---

## 🎯 Best for AI: Hugging Face Spaces

### Step 1: Create Space
1. Go to https://huggingface.co/spaces
2. Click "Create new Space"
3. Name: "voice-clone-video"
4. SDK: "Gradio"
5. Click "Create Space"

### Step 2: Upload Files
1. Upload all your files
2. Hugging Face will auto-deploy
3. **Done!** ✅

**Benefits:**
- Free GPU!
- No model size limits
- Perfect for AI apps
- Always on

---

## 📊 Comparison:

| Platform | Free Tier | Sleep Mode | GPU | Best For |
|----------|-----------|------------|-----|----------|
| **Render** | 750h/month | Yes (15min) | No | Quick deploy |
| **Railway** | $5 credit | No | No | Always-on |
| **HF Spaces** | Unlimited | No | Yes! | AI apps ⭐ |
| **PythonAnywhere** | Always on | No | No | Simple apps |

---

## 🎊 My Recommendation:

### For Quick Test:
**Render.com** - 5 minutes, easiest

### For Production:
**Hugging Face Spaces** - Free GPU, no limits, perfect for AI

### For Always-On:
**Railway.app** - No sleep mode, $5/month free

---

## 🔧 Troubleshooting:

### Issue: "Out of Memory"
**Solution:** Model too large for free tier
- Use edge-tts (already in requirements.txt)
- Or upgrade to paid tier
- Or use Hugging Face Spaces (supports large models)

### Issue: "FFmpeg not found"
**Solution:** Add buildpack
- Render: Add in dashboard → Settings → Build Command
- Railway: Auto-detects
- HF Spaces: Pre-installed

### Issue: "App sleeps after 15 min"
**Solution:** 
- Use Railway (no sleep)
- Or use HF Spaces (no sleep)
- Or upgrade Render to paid

---

## ✅ Next Steps:

1. **Push code to GitHub**
2. **Choose platform** (Render/Railway/HF Spaces)
3. **Deploy** (5-10 minutes)
4. **Test** your live app!
5. **Share** the URL!

---

## 🎯 Quick Commands:

### Push to GitHub:
```bash
git init
git add .
git commit -m "Ready for deployment"
git branch -M main
git remote add origin YOUR_REPO_URL
git push -u origin main
```

### Test Locally First:
```bash
python app.py
# Open http://localhost:5000
```

---

**Your app is ready to deploy!** 🚀
**Choose a platform and go live in 5 minutes!**
