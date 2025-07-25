#!/bin/bash

# Claude Labs - Web App Launcher
# Simple shell script to launch the Streamlit web interface

echo "🌐 Claude Labs - Web App"
echo "=============================="

# Check if app.py exists
if [ ! -f "app.py" ]; then
    echo "❌ app.py not found!"
    echo "Make sure you're in the correct directory."
    exit 1
fi

# Check if virtual environment exists and activate it
if [ -d "venv" ]; then
    echo "🐍 Activating virtual environment..."
    source venv/bin/activate
    
    # Check if streamlit is installed
    if ! python -c "import streamlit" 2>/dev/null; then
        echo "📦 Installing dependencies..."
        pip install -r requirements.txt
    fi
else
    echo "🐍 Creating virtual environment..."
    python3 -m venv venv
    source venv/bin/activate
    echo "📦 Installing dependencies..."
    pip install -r requirements.txt
fi

# Check API key
if [ -z "$ANTHROPIC_API_KEY" ]; then
    echo "⚠️  ANTHROPIC_API_KEY not found in environment"
    echo ""
    echo "🔧 Quick Setup:"
    echo "1. Get your API key from: https://console.anthropic.com/"
    echo "2. Set it for this session:"
    echo "   export ANTHROPIC_API_KEY='your-api-key-here'"
    echo "3. Or set it permanently:"
    echo "   echo 'export ANTHROPIC_API_KEY=\"your-api-key-here\"' >> ~/.bashrc"
    echo "   source ~/.bashrc"
    echo ""
    echo "💡 You can also set it in the web app sidebar"
    echo ""
    echo "❌ Please set your API key before starting the web app"
    exit 1
else
    echo "✅ API key found!"
fi

echo ""
echo "🚀 Starting web app..."
echo "📱 Opening in browser: http://localhost:8501"
echo "💡 Press Ctrl+C to stop"
echo ""

# Debug: print Python and Streamlit version
python -c "import sys; print('Python:', sys.executable); import streamlit; print('Streamlit:', streamlit.__version__)"

# Launch Streamlit
python -m streamlit run app.py --server.port 8501 --server.address localhost 