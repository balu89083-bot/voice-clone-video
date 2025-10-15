@echo off
echo ============================================
echo FFmpeg Installation Helper
echo ============================================
echo.

echo This script will help you install FFmpeg
echo.

echo Step 1: Download FFmpeg
echo ============================================
echo.
echo Opening download page in browser...
echo.
echo Download this file:
echo   ffmpeg-master-latest-win64-gpl.zip
echo.
start https://github.com/BtbN/FFmpeg-Builds/releases
echo.
echo Press any key after download completes...
pause >nul

echo.
echo Step 2: Extract FFmpeg
echo ============================================
echo.
echo Please extract the downloaded ZIP to: C:\ffmpeg
echo.
echo Make sure you have: C:\ffmpeg\bin\ffmpeg.exe
echo.
echo Press any key after extraction...
pause >nul

echo.
echo Step 3: Add to PATH
echo ============================================
echo.
echo Adding C:\ffmpeg\bin to PATH...
echo.

setx PATH "%PATH%;C:\ffmpeg\bin"

echo.
echo ✓ PATH updated!
echo.
echo Step 4: Verify Installation
echo ============================================
echo.
echo Please close this window and open a NEW Command Prompt
echo Then run: ffmpeg -version
echo.
echo If it shows FFmpeg version, installation is successful!
echo.
echo Then run: RESTART_APP.bat
echo.
echo ============================================
echo Installation Complete!
echo ============================================
echo.
pause
