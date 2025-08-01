#!/bin/bash

# Claude Labs - Setup Script
# This script automates the setup process for Claude Labs

set -e  # Exit on any error

echo "🚀 Claude Labs - Setup Script"
echo "=================================="

# Check if Python 3 is installed
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is not installed!"
    echo "💡 Please install Python 3.8 or higher and try again."
    exit 1
fi

echo "✅ Python 3 found: $(python3 --version)"

# Check if pip is installed
if ! command -v pip3 &> /dev/null; then
    echo "❌ pip3 is not installed!"
    echo "💡 Please install pip3 and try again."
    exit 1
fi

echo "✅ pip3 found: $(pip3 --version)"

# Create virtual environment
echo ""
echo "🐍 Creating virtual environment..."
if [ -d "venv" ]; then
    echo "⚠️  Virtual environment 'venv' already exists"
    read -p "Do you want to recreate it? (y/N): " -n 1 -r
    echo
    if [[ $REPLY =~ ^[Yy]$ ]]; then
        echo "🗑️  Removing existing virtual environment..."
        rm -rf venv
    else
        echo "✅ Using existing virtual environment"
    fi
fi

if [ ! -d "venv" ]; then
    python3 -m venv venv
    echo "✅ Virtual environment created successfully!"
fi

# Activate virtual environment
echo ""
echo "🔧 Activating virtual environment..."
source venv/bin/activate

# Upgrade pip in virtual environment
echo "⬆️  Upgrading pip..."
pip install --upgrade pip

# Install dependencies
echo ""
echo "📦 Installing dependencies..."
pip install -r requirements.txt

echo "✅ Dependencies installed successfully!"

# Check for API key
echo ""
echo "🔑 Setting up your Claude API key..."

if [ -z "$ANTHROPIC_API_KEY" ]; then
    echo "⚠️  ANTHROPIC_API_KEY not found in environment variables"
    echo ""
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
                # Set the API key for current session
                export ANTHROPIC_API_KEY="$api_key"
                echo "✅ API key set for current session!"
                echo "🔑 Key: ${api_key:0:10}...${api_key: -4}"
                
                # Ask if user wants to save it permanently
                echo ""
                read -p "💾 Save this API key permanently? (adds to ~/.bashrc or ~/.zshrc) (y/N): " -n 1 -r
                echo
                if [[ $REPLY =~ ^[Yy]$ ]]; then
                    # Detect shell and add to appropriate config file
                    if [ -n "$ZSH_VERSION" ]; then
                        echo "export ANTHROPIC_API_KEY='$api_key'" >> ~/.zshrc
                        echo "✅ API key saved to ~/.zshrc"
                    elif [ -n "$BASH_VERSION" ]; then
                        echo "export ANTHROPIC_API_KEY='$api_key'" >> ~/.bashrc
                        echo "✅ API key saved to ~/.bashrc"
                    else
                        echo "export ANTHROPIC_API_KEY='$api_key'" >> ~/.profile
                        echo "✅ API key saved to ~/.profile"
                    fi
                    echo "💡 Restart your terminal or run 'source ~/.bashrc' (or ~/.zshrc) to load the key"
                fi
            
            echo ""
            echo "🧪 Testing your API key..."
            if python test_setup.py; then
                echo "✅ API key test successful!"
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
                echo "4. Try running the test again:"
                echo "   source venv/bin/activate && python test_setup.py"
                echo ""
                echo "💡 You can still use the demo, but you'll need to fix the API key first."
            fi
        else
            echo "❌ No API key provided. You can set it later with:"
            echo "   export ANTHROPIC_API_KEY='your-api-key-here'"
        fi
    else
        echo ""
        echo "⏸️  No problem! You can set up your API key later:"
        echo ""
        echo "🔧 To set up your API key later:"
        echo "1. Get your key from: https://console.anthropic.com/"
        echo "2. Set it with: export ANTHROPIC_API_KEY='your-key-here'"
        echo "3. Test with: source venv/bin/activate && python test_setup.py"
        echo ""
        echo "💡 Or run this setup script again: ./setup.sh"
        echo ""
        echo "🔑 Or set it for this session only:"
        read -p "Would you like to set an API key for this session? (y/N): " -n 1 -r
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
                echo ""
                echo "🧪 Testing your API key..."
                if python test_setup.py; then
                    echo "✅ API key test successful!"
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
                    echo "4. Try running the test again:"
                    echo "   source venv/bin/activate && python test_setup.py"
                    echo ""
                    echo "💡 You can still use the demo, but you'll need to fix the API key first."
                fi
            else
                echo "❌ No API key provided."
            fi
        fi
    fi
else
    echo "✅ ANTHROPIC_API_KEY found in environment variables"
    echo ""
    echo "🧪 Testing your API key..."
    python test_setup.py
fi

echo ""
echo "🎉 Setup complete!"
echo ""
echo "🚀 To use the demo:"
echo "1. Activate the virtual environment:"
echo "   source venv/bin/activate"
echo ""
echo "2. Set your API key (if not done already):"
echo "   export ANTHROPIC_API_KEY='your-api-key-here'"
echo ""
echo "3. Try the demo:"
echo "   python main.py \"Your text to summarize here\""
echo ""
echo "📖 For more examples, see README.md"
echo ""
echo "💡 Remember to always activate the virtual environment before running the demo!"
echo "💡 If you need help, run: python test_setup.py" 