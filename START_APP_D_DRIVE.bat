@echo off
echo ============================================
echo Voice Cloning App - D Drive Setup
echo ============================================
echo.

echo Setting TTS cache to D drive...
set TTS_HOME=D:\tts_cache
set COQUI_TOS_AGREED=1

echo Activating Python 3.11 environment...
call venv311\Scripts\activate.bat

echo.
echo Starting Voice Cloning Server...
echo Model location: D:\tts_cache
echo.
echo Open browser: http://localhost:5000
echo.
echo Press Ctrl+C to stop the server
echo.
python app.py
