#!/bin/bash

echo "🚀 Setting up Hello Claude Demo on Replit..."

# Install dependencies
echo "📦 Installing dependencies..."
pip install -r requirements.txt

# Check if API key is set
if [ -z "$ANTHROPIC_API_KEY" ]; then
    echo ""
    echo "🔑 API Key Setup Required"
    echo "========================="
    echo "To use this demo, you need an Anthropic API key:"
    echo ""
    echo "1. Visit: https://console.anthropic.com/"
    echo "2. Sign up/login and get your API key"
    echo "3. Set it as a Replit secret:"
    echo "   - Go to 'Tools' → 'Secrets'"
    echo "   - Add: ANTHROPIC_API_KEY = your-key-here"
    echo ""
    echo "💡 Or set it manually in the shell:"
    echo "   export ANTHROPIC_API_KEY='your-key-here'"
    echo ""
    echo "🎯 Once you have your API key, click 'Run' to test the demo!"
else
    echo "✅ API key found! Ready to run."
    echo ""
    echo "🎯 Click 'Run' to test the demo with the Anthropic article!"
fi

echo ""
echo "📖 Available commands:"
echo "  python main.py --url https://www.anthropic.com/news/introducing-claude"
echo "  python main.py --file document.txt"
echo "  python main.py 'Your text here'"
echo "" 