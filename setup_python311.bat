@echo off
echo ============================================
echo Voice Cloning Setup - Python 3.11
echo ============================================
echo.

echo Step 1: Checking Python 3.11...
py -3.11 --version
if errorlevel 1 (
    echo.
    echo ERROR: Python 3.11 not found!
    echo.
    echo Please install Python 3.11 from:
    echo https://www.python.org/downloads/release/python-3110/
    echo.
    pause
    exit /b 1
)

echo.
echo Step 2: Creating virtual environment with Python 3.11...
py -3.11 -m venv venv311

echo.
echo Step 3: Activating virtual environment...
call venv311\Scripts\activate.bat

echo.
echo Step 4: Upgrading pip...
python -m pip install --upgrade pip

echo.
echo Step 5: Installing Coqui TTS and dependencies...
echo This will take 5-10 minutes...
pip install TTS==0.22.0
pip install torch torchaudio --index-url https://download.pytorch.org/whl/cpu
pip install Flask==3.0.0 Werkzeug==3.0.1
pip install moviepy pydub numpy scipy

echo.
echo ============================================
echo Installation Complete!
echo ============================================
echo.
echo To use REAL voice cloning:
echo 1. Activate environment: venv311\Scripts\activate
echo 2. Copy voice_cloner_coqui.py to voice_cloner.py
echo 3. Run: python app.py
echo.
pause
