@echo off
echo ============================================
echo Voice Cloning App - E Drive Setup
echo ============================================
echo.

echo Setting TTS cache to E drive...
set TTS_HOME=E:\tts_cache
set COQUI_TOS_AGREED=1

echo Activating Python 3.11 environment...
call venv311\Scripts\activate.bat

echo.
echo Starting Voice Cloning Server...
echo Model will load from E:\tts_cache
echo.
echo Open browser: http://localhost:5000
echo.
echo Press Ctrl+C to stop the server
echo.
python app.py
