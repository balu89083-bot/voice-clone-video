@echo off
echo ============================================
echo Moving TTS Cache to E Drive
echo ============================================
echo.

echo Creating TTS cache directory on E drive...
mkdir E:\tts_cache 2>nul

echo.
echo Setting environment variable...
setx TTS_HOME "E:\tts_cache"

echo.
echo ============================================
echo Done!
echo ============================================
echo.
echo TTS models will now be stored on E drive
echo Location: E:\tts_cache
echo.
echo Please RESTART your terminal/command prompt
echo Then run: download_model_e_drive.bat
echo.
pause
