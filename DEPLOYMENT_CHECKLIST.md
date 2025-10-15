# ✅ Render.com Deployment Checklist

## 🎯 Quick Start (15 Minutes Total)

---

## Part 1: GitHub Setup (5 minutes)

### Option A: Use Batch File (Easiest!)
```
1. Double-click: deploy_to_github.bat
2. Follow prompts
3. Done! ✅
```

### Option B: Manual Commands
```bash
cd D:\voice-clone-video
git init
git add .
git commit -m "Deploy to Render"
```

**Create GitHub Repo:**
1. Go to https://github.com
2. Click "+" → "New repository"
3. Name: `voice-clone-video`
4. Keep **Public**
5. Click "Create repository"

**Push Code:**
```bash
git remote add origin https://github.com/YOUR_USERNAME/voice-clone-video.git
git branch -M main
git push -u origin main
```

✅ **Done!** Code is on GitHub

---

## Part 2: Render.com Deploy (10 minutes)

### Step 1: Sign Up
- [ ] Go to https://render.com
- [ ] Click "Get Started"
- [ ] Sign up with GitHub
- [ ] Authorize Render

### Step 2: Create Service
- [ ] Click "New +" → "Web Service"
- [ ] Find `voice-clone-video` repo
- [ ] Click "Connect"

### Step 3: Configure
- [ ] **Name:** voice-clone-video
- [ ] **Branch:** main
- [ ] **Runtime:** Python 3
- [ ] **Build Command:** `pip install -r requirements.txt`
- [ ] **Start Command:** `python app.py`
- [ ] **Plan:** Free

### Step 4: Deploy
- [ ] Click "Create Web Service"
- [ ] Wait 5-10 minutes
- [ ] Watch logs

### Step 5: Success!
- [ ] See "Your service is live!" message
- [ ] Copy your URL
- [ ] Open in browser
- [ ] Test upload & generate

✅ **Done!** App is live!

---

## 🎊 Your Live URL:
```
https://voice-clone-video-XXXX.onrender.com
```

---

## 📋 Quick Reference:

### Update App Later:
```bash
git add .
git commit -m "Update"
git push
```
(Auto-deploys on Render!)

### View Logs:
Render Dashboard → Your Service → Logs

### Custom Domain:
Render Dashboard → Settings → Custom Domain

---

## ⚠️ Troubleshooting:

### Build Failed?
- Check logs in Render dashboard
- Most common: Out of memory
- Solution: Already using lightweight edge-tts ✅

### App Not Loading?
- Wait 1-2 minutes (first request wakes it up)
- Free tier sleeps after 15 min inactivity

### Can't Push to GitHub?
- Check GitHub username/password
- Or use Personal Access Token
- See GitHub docs

---

## 🎯 Success Criteria:

✅ Code on GitHub
✅ Render service created
✅ Build successful
✅ App running
✅ URL accessible
✅ Can upload files
✅ Can generate video

**All done? Congratulations! 🎉**

---

## 📞 Need Help?

- **Render Docs:** https://render.com/docs
- **GitHub Docs:** https://docs.github.com
- **Check:** RENDER_DEPLOY_STEPS.md (detailed guide)

---

**Start Now: Run `deploy_to_github.bat` or follow Part 1!** 🚀
