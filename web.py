#!/usr/bin/env python3
"""
Claude Labs - Web App
Simple launcher for the Streamlit web interface
"""

import os
import sys
import subprocess
from pathlib import Path

def main():
    """Launch the Streamlit web app"""
    print("🌐 Claude Labs - Web App")
    print("=" * 40)
    
    # Check if app.py exists
    if not Path("app.py").exists():
        print("❌ app.py not found!")
        print("Make sure you're in the correct directory.")
        sys.exit(1)
    
    # Check dependencies
    try:
        import streamlit
        import anthropic
        import requests
    except ImportError as e:
        print(f"❌ Missing dependency: {e}")
        print("\n🔧 Installing dependencies...")
        try:
            subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
            print("✅ Dependencies installed successfully!")
        except subprocess.CalledProcessError:
            print("❌ Failed to install dependencies")
            print("💡 Try manually: pip install -r requirements.txt")
            sys.exit(1)
    
    # Check API key
    api_key = os.getenv('ANTHROPIC_API_KEY')
    if not api_key:
        print("⚠️  ANTHROPIC_API_KEY not found in environment")
        print("")
        print("🔧 Quick Setup:")
        print("1. Get your API key from: https://console.anthropic.com/")
        print("2. Set it for this session:")
        print("   export ANTHROPIC_API_KEY='your-api-key-here'")
        print("3. Or set it permanently:")
        print("   echo 'export ANTHROPIC_API_KEY=\"your-api-key-here\"' >> ~/.bashrc")
        print("   source ~/.bashrc")
        print("")
        print("💡 You can also set it in the web app sidebar")
        print("")
        print("❌ Please set your API key before starting the web app")
        sys.exit(1)
    else:
        print("✅ API key found!")
    
    print("\n🚀 Starting web app...")
    print("📱 Opening in browser: http://localhost:8501")
    print("💡 Press Ctrl+C to stop")
    
    try:
        # Launch Streamlit
        subprocess.run([
            sys.executable, "-m", "streamlit", "run", "app.py",
            "--server.port", "8501",
            "--server.address", "localhost"
        ])
    except KeyboardInterrupt:
        print("\n👋 Web app stopped. Goodbye!")
    except Exception as e:
        print(f"❌ Error: {e}")
        print("💡 Try: pip install streamlit")

if __name__ == "__main__":
    main() 