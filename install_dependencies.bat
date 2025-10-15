@echo off
echo ============================================
echo Installing Dependencies for Real Voice Cloning
echo ============================================
echo.
echo This will take 5-10 minutes...
echo Please be patient!
echo.

call venv311\Scripts\activate.bat

echo Step 1/5: Upgrading pip...
python -m pip install --upgrade pip

echo.
echo Step 2/5: Installing PyTorch (CPU version)...
pip install torch torchaudio --index-url https://download.pytorch.org/whl/cpu

echo.
echo Step 3/5: Installing Coqui TTS...
pip install TTS==0.22.0

echo.
echo Step 4/5: Installing web framework...
pip install Flask==3.0.0 Werkzeug==3.0.1

echo.
echo Step 5/5: Installing video processing...
pip install moviepy pydub numpy scipy

echo.
echo ============================================
echo Installation Complete!
echo ============================================
echo.
echo To start the app with REAL voice cloning:
echo   Run: start_with_cloning.bat
echo.
pause
