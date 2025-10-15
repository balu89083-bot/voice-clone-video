@echo off
echo ============================================
echo Voice Cloning App - REAL Voice Cloning
echo ============================================
echo.

echo Activating Python 3.11 environment...
call venv311\Scripts\activate.bat

echo.
echo Copying real voice cloner...
copy /Y voice_cloner_coqui.py voice_cloner.py >nul

echo.
echo Starting server...
echo Open browser: http://localhost:5000
echo.
python app.py
