@echo off
echo ============================================
echo Moving Voice Cloning Project to D Drive
echo ============================================
echo.

echo This will move the entire project to D:\voice-clone-video
echo.
echo Current location: C:\Users\balra\Documents\project\voice-clone-video
echo New location: D:\voice-clone-video
echo.
echo Press any key to continue or Ctrl+C to cancel...
pause >nul

echo.
echo Step 1: Creating D:\voice-clone-video directory...
mkdir "D:\voice-clone-video" 2>nul

echo.
echo Step 2: Copying all files to D drive...
echo This may take a few minutes...
echo.

xcopy "C:\Users\balra\Documents\project\voice-clone-video\*" "D:\voice-clone-video\" /E /H /I /Y

echo.
echo Step 3: Verifying copy...
echo.

if exist "D:\voice-clone-video\app.py" (
    echo ✓ Files copied successfully!
    echo.
    echo Step 4: Testing D drive location...
    cd /d D:\voice-clone-video
    echo ✓ Changed to D drive
    echo.
    echo ============================================
    echo SUCCESS! Project moved to D drive
    echo ============================================
    echo.
    echo New location: D:\voice-clone-video
    echo.
    echo Next steps:
    echo 1. Close this window
    echo 2. Open new Command Prompt
    echo 3. Run: cd /d D:\voice-clone-video
    echo 4. Run: RESTART_APP.bat
    echo.
    echo After confirming everything works, you can delete:
    echo C:\Users\balra\Documents\project\voice-clone-video
    echo.
) else (
    echo ✗ Copy failed! Please try again.
    echo.
)

pause
