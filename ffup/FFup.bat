@echo off

:: Check for git
git --version >nul 2>&1
if errorlevel 1 (
    echo Git is not found! Please ensure Git is installed and available in the system's PATH.
    pause
    exit /b
)

python FFup.py
pause