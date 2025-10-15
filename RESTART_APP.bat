@echo off
echo ============================================
echo Restarting Voice Cloning App
echo ============================================
echo.

echo Setting environment for D drive...
set TTS_HOME=D:\tts_cache
set COQUI_TOS_AGREED=1

echo.
echo Activating Python environment...
call venv311\Scripts\activate.bat

echo.
echo Starting app with fixes...
echo - Fixed encoding errors
echo - Fixed progress updates
echo.
echo Open browser: http://localhost:5000
echo.
python app.py
