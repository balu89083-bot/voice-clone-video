# 📦 Move Project to D Drive - Complete Guide

## 🎯 Why Move to D Drive?

- ✅ C drive full
- ✅ More space on D drive
- ✅ Better organization
- ✅ Keep all data together

## 🚀 Quick Move (Automatic)

### **Step 1: Run Move Script**

```bash
move_to_d_drive.bat
```

**This will:**
1. Create `D:\voice-clone-video`
2. Copy all files (code, models, uploads, outputs)
3. Verify copy
4. Show next steps

---

## 📝 Manual Move (Alternative)

### **Step 1: Copy Project**

**In Command Prompt:**
```bash
xcopy "C:\Users\balra\Documents\project\voice-clone-video" "D:\voice-clone-video\" /E /H /I /Y
```

### **Step 2: Verify**

```bash
cd /d D:\voice-clone-video
dir
```

**Should see:** app.py, voice_cloner.py, etc.

### **Step 3: Update Environment**

**Already set:** TTS_HOME=D:\tts_cache ✅

---

## 🔧 After Moving

### **Step 1: Go to New Location**

```bash
cd /d D:\voice-clone-video
```

### **Step 2: Start App**

```bash
RESTART_APP.bat
```

**Or:**
```bash
venv311\Scripts\activate
set TTS_HOME=D:\tts_cache
set COQUI_TOS_AGREED=1
python app.py
```

### **Step 3: Test**

Open: http://localhost:5000

**Test voice cloning to confirm everything works!**

---

## 🗑️ Clean Up Old Location

**After confirming D drive works:**

```bash
# Delete old C drive copy
rmdir /s "C:\Users\balra\Documents\project\voice-clone-video"
```

**Or manually delete the folder**

---

## 📊 What Gets Moved

**Everything:**
- ✅ Python code (app.py, voice_cloner.py, etc.)
- ✅ Virtual environment (venv311)
- ✅ Uploads folder
- ✅ Outputs folder
- ✅ Temp files
- ✅ All scripts and docs

**TTS Model:**
- Already on D drive: `D:\tts_cache` ✅

---

## 💡 New Folder Structure

```
D:\
├── voice-clone-video\          (Your project)
│   ├── app.py
│   ├── voice_cloner.py
│   ├── venv311\
│   ├── uploads\
│   ├── outputs\
│   └── ...
│
└── tts_cache\                  (TTS model - already here)
    └── tts_models\
```

---

## 🎯 Quick Commands After Move

### **Navigate to Project:**
```bash
cd /d D:\voice-clone-video
```

### **Start App:**
```bash
RESTART_APP.bat
```

### **Activate Environment:**
```bash
venv311\Scripts\activate
```

---

## ✅ Verification Checklist

After moving, check:

- [ ] Files exist: `D:\voice-clone-video\app.py`
- [ ] Virtual env works: `D:\voice-clone-video\venv311`
- [ ] TTS model accessible: `D:\tts_cache`
- [ ] App starts: `RESTART_APP.bat`
- [ ] Web UI opens: http://localhost:5000
- [ ] Voice cloning works

---

## 🔄 Update Shortcuts/Bookmarks

**Update any shortcuts to:**
```
D:\voice-clone-video
```

**VS Code / IDE:**
- Close old workspace
- Open: `D:\voice-clone-video`

---

## 🎊 Benefits After Move

- ✅ More space available
- ✅ C drive freed up
- ✅ Everything on D drive
- ✅ Faster access (if D is SSD)
- ✅ Better organization

---

## 📝 Summary

**To move:**
```bash
move_to_d_drive.bat
```

**To start after move:**
```bash
cd /d D:\voice-clone-video
RESTART_APP.bat
```

**To clean up:**
```bash
# After confirming D drive works
rmdir /s "C:\Users\balra\Documents\project\voice-clone-video"
```

---

**Ready to move? Run:** `move_to_d_drive.bat` 🚀
