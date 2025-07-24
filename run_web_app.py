#!/usr/bin/env python3
"""
Hello Claude Demo - Web App Launcher
Launches the Streamlit web interface for the Hello Claude Demo
"""

import os
import sys
import subprocess
from pathlib import Path

def check_api_key():
    """Check if API key is set"""
    api_key = os.getenv('ANTHROPIC_API_KEY')
    if not api_key:
        print("❌ ANTHROPIC_API_KEY environment variable not found!")
        print("\n🔧 Quick Setup:")
        print("1. Get your API key from: https://console.anthropic.com/")
        print("2. Set it as an environment variable:")
        print("   export ANTHROPIC_API_KEY='your-api-key-here'")
        print("\n💡 Or set it in the web app sidebar!")
        return False
    return True

def check_dependencies():
    """Check if required packages are installed"""
    try:
        import streamlit
        import anthropic
        import requests
        return True
    except ImportError as e:
        print(f"❌ Missing dependency: {e}")
        print("\n🔧 Install dependencies:")
        print("   pip install -r requirements.txt")
        return False

def main():
    """Main launcher function"""
    print("🚀 Hello Claude Demo - Web App Launcher")
    print("=" * 50)
    
    # Check dependencies
    if not check_dependencies():
        sys.exit(1)
    
    # Check API key (optional - can be set in web app)
    api_key_status = check_api_key()
    if api_key_status:
        print("✅ API key found!")
    else:
        print("⚠️  API key not found - you can set it in the web app sidebar")
    
    # Check if app.py exists
    app_path = Path("app.py")
    if not app_path.exists():
        print("❌ app.py not found!")
        print("Make sure you're in the correct directory.")
        sys.exit(1)
    
    print("\n🌐 Starting Streamlit web app...")
    print("📱 The app will open in your browser automatically")
    print("🔗 If it doesn't open, go to: http://localhost:8501")
    print("\n💡 Tips:")
    print("- Use Ctrl+C to stop the web app")
    print("- The app will automatically reload when you make changes")
    print("- Set your API key in the sidebar if not already set")
    
    try:
        # Start Streamlit app
        subprocess.run([
            sys.executable, "-m", "streamlit", "run", "app.py",
            "--server.port", "8501",
            "--server.address", "localhost",
            "--browser.gatherUsageStats", "false"
        ])
    except KeyboardInterrupt:
        print("\n👋 Web app stopped. Goodbye!")
    except Exception as e:
        print(f"❌ Error starting web app: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main() 