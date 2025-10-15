# 🧹 Free Up RAM Before Installing

## ⚠️ Problem

XTTS-v2 model needs **4-6GB free RAM** to load.
Currently system doesn't have enough.

## ✅ How to Free RAM

### **Step 1: Close Browsers**
- Close Chrome
- Close Edge
- Close Firefox
- (Browsers use a LOT of RAM)

### **Step 2: Close Applications**
- Close VS Code (if open)
- Close any video players
- Close any games
- Close any other heavy apps

### **Step 3: Check RAM Usage**

**Open Task Manager:**
- Press `Ctrl + Shift + Esc`
- Click "Performance" tab
- Check "Memory" section
- You need **at least 4GB free**

### **Step 4: Restart Computer (Best)**

**Most effective way:**
1. Save all work
2. Restart computer
3. Don't open anything else
4. Run the download script immediately

## 📊 RAM Requirements

| Task | RAM Needed |
|------|-----------|
| Windows | 2-3GB |
| Chrome (multiple tabs) | 1-2GB |
| VS Code | 500MB-1GB |
| **XTTS-v2 Model** | **4-6GB** |
| **Total Needed** | **8-10GB** |

## 🎯 Recommended Steps

### **Option 1: Restart & Try (Best)**

```bash
1. Restart computer
2. Don't open browsers
3. Open terminal only
4. Run: venv311\Scripts\activate
5. Run: python download_to_e_drive.py
```

### **Option 2: Close Everything**

```bash
1. Close all browsers
2. Close all apps
3. Check Task Manager (need 4GB+ free)
4. Run: venv311\Scripts\activate
5. Run: python download_to_e_drive.py
```

## 🆘 If Still Not Enough RAM

### **Check Your Total RAM:**

1. Open Task Manager
2. Performance → Memory
3. Check total RAM

**If you have:**
- **4GB RAM** → XTTS-v2 won't work (not enough)
- **6GB RAM** → Might work if everything closed
- **8GB+ RAM** → Should work

### **If Less Than 8GB Total:**

**You have 2 options:**

**Option A: Upgrade RAM**
- Add more RAM to your system
- Recommended: 8GB minimum, 16GB ideal

**Option B: Use Edge TTS**
- No RAM needed (cloud-based)
- Excellent quality
- No voice cloning, but great voices
- Run: `python app.py`

## 💡 My Recommendation

### **If you have 8GB+ RAM:**
1. Restart computer
2. Close everything
3. Run download script
4. Should work!

### **If you have less than 8GB RAM:**
- XTTS-v2 won't work reliably
- Use Edge TTS instead
- Or upgrade your RAM

## 🎯 Next Steps

**After freeing RAM:**

```bash
cd C:\Users\balra\Documents\project\voice-clone-video
venv311\Scripts\activate
python download_to_e_drive.py
```

**This will:**
- Download model to E drive (saves C drive space)
- Try to load with memory optimization
- Show clear error if still not enough RAM

---

**Pehle RAM free karo, phir try karo!** 💪
