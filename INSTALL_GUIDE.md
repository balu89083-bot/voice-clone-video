# 🎤 Real Voice Cloning Installation Guide

## ⚠️ Important: Python Version Required

**Real voice cloning (Coqui TTS) requires Python 3.9, 3.10, or 3.11**

You currently have Python 3.13 (Microsoft Store version), which won't work with Coqui TTS.

## 📥 Step-by-Step Installation

### **Step 1: Download Python 3.11**

1. Go to: https://www.python.org/downloads/release/python-3110/
2. Scroll down to **"Files"** section
3. Download: **Windows installer (64-bit)**
   - File name: `python-3.11.0-amd64.exe`

### **Step 2: Install Python 3.11**

1. **Run the installer**
2. ✅ **IMPORTANT:** Check **"Add Python 3.11 to PATH"**
3. ✅ Check **"Install for all users"** (optional)
4. Click **"Install Now"**
5. Wait for installation to complete

**Note:** Python 3.11 will install alongside Python 3.13 - both can coexist!

### **Step 3: Verify Installation**

Open **new** PowerShell/Command Prompt and run:

```bash
py --list
```

You should see:
```
-3.13-64 *
-3.11-64
```

### **Step 4: Run Setup Script**

```bash
cd C:\Users\balra\Documents\project\voice-clone-video
setup_python311.bat
```

This will:
- Create virtual environment with Python 3.11
- Install Coqui TTS
- Install all dependencies
- Takes 5-10 minutes

### **Step 5: Activate & Use**

```bash
# Activate Python 3.11 environment
venv311\Scripts\activate

# Your prompt will change to show (venv311)

# Copy the real voice cloner
copy voice_cloner_coqui.py voice_cloner.py

# Start the app
python app.py
```

## 🎯 Two Versions Available

### **Version 1: Edge TTS (Current - Python 3.13)**
- ❌ No real voice cloning
- ✅ Pre-built high-quality voices
- ✅ Easy setup
- ✅ Fast processing
- Use: Current setup (already working)

### **Version 2: Coqui TTS (Real Cloning - Python 3.11)**
- ✅ **REAL voice cloning**
- ✅ Clone any voice from 6-10 sec audio
- ✅ Excellent quality
- ❌ Requires Python 3.11
- ❌ Longer setup time
- Use: Follow this guide

## 🔄 Switching Between Versions

### **Use Edge TTS (No Cloning):**
```bash
# Use Python 3.13 (default)
python app.py
```

### **Use Coqui TTS (Real Cloning):**
```bash
# Activate Python 3.11 environment
venv311\Scripts\activate

# Copy real voice cloner
copy voice_cloner_coqui.py voice_cloner.py

# Run app
python app.py
```

## 📊 Comparison

| Feature | Edge TTS | Coqui TTS |
|---------|----------|-----------|
| **Voice Cloning** | ❌ No | ✅ **Yes** |
| **Python Version** | 3.13 ✅ | 3.11 only |
| **Setup Time** | 2 min | 10 min |
| **Model Download** | No | Yes (~2GB) |
| **Reference Audio** | Not used | **Required** |
| **Quality** | Excellent | Excellent |
| **Internet** | Required | Not required |
| **Use Case** | Quick TTS | **Real cloning** |

## 🎤 How Real Voice Cloning Works

1. **Record reference audio** (6-10 seconds of your voice)
2. **Upload to app** via web UI
3. **Type your text**
4. **App clones your voice** and generates speech
5. **Adds to video**

## 🆘 Troubleshooting

### Python 3.11 not found after installation?
```bash
# Restart PowerShell/Terminal
# Then check again
py --list
```

### Setup script fails?
```bash
# Manual installation:
py -3.11 -m venv venv311
venv311\Scripts\activate
pip install TTS==0.22.0
pip install torch torchaudio
pip install Flask moviepy pydub
```

### Model download is slow?
- First run downloads ~2GB model
- This is one-time only
- Be patient (5-10 minutes)

## ✅ Quick Commands Reference

```bash
# Check Python versions
py --list

# Create Python 3.11 environment
py -3.11 -m venv venv311

# Activate environment
venv311\Scripts\activate

# Install Coqui TTS
pip install TTS==0.22.0

# Run app with real voice cloning
python app.py
```

## 🎉 After Installation

Once setup is complete:

1. Open browser: http://localhost:5000
2. **Record your voice** (6-10 seconds)
3. **Type text** you want to say
4. **Upload video**
5. **Generate** - Your cloned voice will be in the video!

## 💡 Recommendation

**For real voice cloning:** Install Python 3.11 and use Coqui TTS
**For quick TTS:** Use current Edge TTS setup (already working)

Choose based on your needs! 🎤
