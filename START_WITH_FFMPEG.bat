@echo off
echo ============================================
echo Voice Cloning App - D Drive with FFmpeg
echo ============================================
echo.

echo Setting up environment...
set PATH=%PATH%;D:\voice-clone-video\ffmpeg-master-latest-win64-gpl-shared\ffmpeg-master-latest-win64-gpl-shared\bin
set TTS_HOME=D:\tts_cache
set COQUI_TOS_AGREED=1

echo Activating Python environment...
call venv311\Scripts\activate.bat

echo.
echo Starting Voice Cloning Server...
echo FFmpeg: Ready
echo TTS Model: D:\tts_cache
echo.
echo Open browser: http://localhost:5000
echo.
echo Press Ctrl+C to stop the server
echo.
python app.py
