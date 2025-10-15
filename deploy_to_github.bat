@echo off
echo ========================================
echo GitHub Deployment Script
echo ========================================
echo.

REM Check if git is initialized
if not exist .git (
    echo Initializing Git repository...
    git init
    echo.
)

REM Add all files
echo Adding all files...
git add .
echo.

REM Commit
echo Committing changes...
set /p commit_msg="Enter commit message (or press Enter for default): "
if "%commit_msg%"=="" set commit_msg=Deploy to Render

git commit -m "%commit_msg%"
echo.

REM Check if remote exists
git remote -v | find "origin" >nul
if errorlevel 1 (
    echo.
    echo ========================================
    echo IMPORTANT: Set up your GitHub repo
    echo ========================================
    echo 1. Go to https://github.com
    echo 2. Click + (top right) -^> New repository
    echo 3. Name: voice-clone-video
    echo 4. Keep it PUBLIC
    echo 5. DON'T initialize with README
    echo 6. Click Create repository
    echo.
    set /p github_url="Enter your GitHub repo URL (e.g., https://github.com/username/voice-clone-video.git): "
    
    git remote add origin !github_url!
    git branch -M main
    echo.
)

REM Push to GitHub
echo Pushing to GitHub...
git push -u origin main

if errorlevel 1 (
    echo.
    echo ========================================
    echo Push failed! Trying force push...
    echo ========================================
    git push -u origin main --force
)

echo.
echo ========================================
echo SUCCESS! Code pushed to GitHub
echo ========================================
echo.
echo Next steps:
echo 1. Go to https://render.com
echo 2. Sign up with GitHub
echo 3. New + -^> Web Service
echo 4. Connect your repo
echo 5. Click Deploy!
echo.
echo See RENDER_DEPLOY_STEPS.md for detailed instructions
echo.
pause
