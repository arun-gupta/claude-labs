@echo off
REM Claude Labs - Windows Virtual Environment Activation
REM Run this script to activate the virtual environment on Windows

echo 🚀 Claude Labs - Windows Setup
echo ====================================

REM Check if virtual environment exists
if not exist "venv\Scripts\activate.bat" (
    echo ❌ Virtual environment not found!
    echo.
    echo 🔧 Creating virtual environment...
    python -m venv venv
    if errorlevel 1 (
        echo ❌ Failed to create virtual environment!
        echo 💡 Make sure Python is installed and in your PATH
        pause
        exit /b 1
    )
    echo ✅ Virtual environment created!
)

REM Activate virtual environment
echo 🔧 Activating virtual environment...
call venv\Scripts\activate.bat

REM Check if dependencies are installed
python -c "import anthropic" 2>nul
if errorlevel 1 (
    echo 📦 Installing dependencies...
    pip install -r requirements.txt
    if errorlevel 1 (
        echo ❌ Failed to install dependencies!
        pause
        exit /b 1
    )
    echo ✅ Dependencies installed!
) else (
    echo ✅ Dependencies already installed!
)

REM Check for API key
if "%ANTHROPIC_API_KEY%"=="" (
    echo ⚠️  ANTHROPIC_API_KEY not found in environment variables
    echo.
    echo 🔧 To complete setup:
    echo 1. Get your API key from: https://console.anthropic.com/
    echo 2. Set it as an environment variable:
    echo    set ANTHROPIC_API_KEY=your-api-key-here
    echo.
    echo 💡 Pro tip: Add this to your system environment variables for persistence
) else (
    echo ✅ ANTHROPIC_API_KEY found in environment variables
)

echo.
echo 🎉 Setup complete!
echo.
echo 🚀 To use the demo:
echo    python main.py "Your text to summarize here"
echo.
echo 📖 For more examples, see README.md
echo.
echo 💡 The virtual environment is now active in this terminal!
echo    To deactivate, run: deactivate
echo.
pause 