@echo off
echo ============================================
echo Freeing RAM for Voice Cloning
echo ============================================
echo.

echo Closing Perplexity...
taskkill /F /IM Perplexity.exe 2>nul
if %errorlevel% equ 0 (echo   - Perplexity closed) else (echo   - Perplexity not running)

echo.
echo Closing Chrome...
taskkill /F /IM chrome.exe 2>nul
if %errorlevel% equ 0 (echo   - Chrome closed) else (echo   - Chrome not running)

echo.
echo Closing Edge...
taskkill /F /IM msedge.exe 2>nul
if %errorlevel% equ 0 (echo   - Edge closed) else (echo   - Edge not running)

echo.
echo ============================================
echo RAM Freed!
echo ============================================
echo.
echo Checking free RAM...
powershell -Command "$free = (Get-WmiObject Win32_OperatingSystem).FreePhysicalMemory / 1MB; Write-Host 'Free RAM:' $([math]::Round($free, 2)) 'GB'"
echo.
echo Now you can try running voice cloning!
echo Run: START_APP_D_DRIVE.bat
echo.
pause
