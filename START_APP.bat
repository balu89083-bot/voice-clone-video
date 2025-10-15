@echo off
echo ============================================
echo Voice Cloning App - REAL Voice Cloning
echo ============================================
echo.

echo Activating Python 3.11 environment...
call venv311\Scripts\activate.bat

echo.
echo Starting Voice Cloning Server...
echo.
echo Open browser: http://localhost:5000
echo.
echo Press Ctrl+C to stop the server
echo.
python app.py
