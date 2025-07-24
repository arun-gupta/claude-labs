#!/bin/bash

# Claude Labs - API Key Setup Script (Sourceable Version)
# This script can be sourced to set API key in current shell
# Usage: source set_api_key_source.sh

# Check if virtual environment exists
if [ ! -d "venv" ]; then
    echo "❌ Virtual environment not found!"
    echo "💡 Please run the setup script first: ./setup.sh"
    return 1
fi

# Activate virtual environment
source venv/bin/activate

echo ""
echo "🔧 Setting up your Claude API key for this session..."
echo ""

# Check if API key is already set
if [ -n "$ANTHROPIC_API_KEY" ]; then
    echo "⚠️  ANTHROPIC_API_KEY is already set in this session"
    read -p "Do you want to change it? (y/N): " -n 1 -r
    echo
    if [[ ! $REPLY =~ ^[Yy]$ ]]; then
        echo "✅ Keeping existing API key"
        echo ""
        echo "🧪 Testing current API key..."
        if python test_setup.py; then
            echo "✅ API key is working correctly!"
        else
            echo "❌ Current API key test failed"
        fi
        return 0
    fi
fi

echo "🔧 Let's set up your API key:"
echo "1. Visit https://console.anthropic.com/"
echo "2. Create an account or sign in"
echo "3. Navigate to API Keys section"
echo "4. Create a new API key"
echo ""

read -p "Do you have your API key ready? (y/N): " -n 1 -r
echo
if [[ $REPLY =~ ^[Yy]$ ]]; then
    echo ""
    echo "📝 Enter your API key (it will be hidden for security):"
    read -s api_key
    echo ""
    
    if [ -n "$api_key" ]; then
        # Set the API key for current session only
        export ANTHROPIC_API_KEY="$api_key"
        echo "✅ API key set for current session!"
        echo "🔑 Key: ${api_key:0:10}...${api_key: -4}"
        echo ""
        echo "🧪 Testing your API key..."
        if python test_setup.py; then
            echo "✅ API key test successful!"
            echo ""
            echo "🎉 You're ready to use the demo!"
            echo ""
            echo "🚀 Try it out:"
            echo "   python main.py \"Your text to summarize here\""
        else
            echo ""
            echo "❌ API key test failed. This could be due to:"
            echo "   - Invalid API key format"
            echo "   - No API credits available"
            echo "   - Network connectivity issues"
            echo ""
            echo "🔧 Troubleshooting steps:"
            echo "1. Verify your API key at: https://console.anthropic.com/"
            echo "2. Check your internet connection"
            echo "3. Ensure you have API credits available"
            echo "4. Try running this script again: source set_api_key_source.sh"
        fi
    else
        echo "❌ No API key provided."
        echo "💡 Run this script again when you have your API key ready."
    fi
else
    echo ""
    echo "⏸️  No problem! You can set up your API key later:"
    echo ""
    echo "🔧 To set up your API key later:"
    echo "1. Get your key from: https://console.anthropic.com/"
    echo "2. Run this script again: source set_api_key_source.sh"
    echo "3. Or set it manually: export ANTHROPIC_API_KEY='your-key-here'"
fi

echo ""
echo "💡 Remember: This API key is only set for the current terminal session."
echo "   If you open a new terminal, you'll need to set it again."
echo "   To make it permanent, add it to your ~/.bashrc or ~/.zshrc file." 