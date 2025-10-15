# 📥 FFmpeg Installation Guide

## 🎯 Download FFmpeg

### **Step 1: Download**

**Link:** https://github.com/BtbN/FFmpeg-Builds/releases

**Download this file:**
- `ffmpeg-master-latest-win64-gpl.zip`

**Or direct link:**
https://github.com/BtbN/FFmpeg-Builds/releases/download/latest/ffmpeg-master-latest-win64-gpl.zip

---

## 📂 Step 2: Extract

1. Download the ZIP file
2. Right-click → Extract All
3. Extract to: `C:\ffmpeg`

**Result:** You should have `C:\ffmpeg\bin\ffmpeg.exe`

---

## 🔧 Step 3: Add to PATH

### **Option A: Automatic (Run this script)**

I'll create a script for you!

### **Option B: Manual**

1. Press `Win + X` → System
2. Click "Advanced system settings"
3. Click "Environment Variables"
4. Under "System variables", find "Path"
5. Click "Edit"
6. Click "New"
7. Add: `C:\ffmpeg\bin`
8. Click OK on all windows
9. **Restart Command Prompt**

---

## ✅ Step 4: Verify

**Open new Command Prompt and run:**
```bash
ffmpeg -version
```

**Should show:** FFmpeg version info ✅

---

## 🚀 Step 5: Restart App

After FFmpeg is installed:

```bash
cd C:\Users\balra\Documents\project\voice-clone-video
RESTART_APP.bat
```

---

## 📝 Quick Summary

1. **Download:** https://github.com/BtbN/FFmpeg-Builds/releases/download/latest/ffmpeg-master-latest-win64-gpl.zip
2. **Extract to:** `C:\ffmpeg`
3. **Add to PATH:** `C:\ffmpeg\bin`
4. **Verify:** `ffmpeg -version`
5. **Restart app:** `RESTART_APP.bat`

---

## 💡 Alternative: Chocolatey (Easiest)

**If you have Chocolatey:**
```bash
choco install ffmpeg
```

**Don't have Chocolatey? Install it:**
```powershell
Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))
```

Then:
```bash
choco install ffmpeg
```

---

## 🎊 After Installation

**FFmpeg will enable:**
- ✅ Perfect audio conversion
- ✅ All audio formats supported
- ✅ Better video processing
- ✅ No more format errors!

**Then voice cloning will work perfectly!** 🎤✨
