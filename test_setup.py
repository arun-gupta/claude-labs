#!/usr/bin/env python3
"""
Test Setup Script for Hello Claude Demo

Run this script to verify your setup before using the main demo.
This will check your API key and test a simple Claude API call.
"""

import os
import sys

def test_api_key():
    """Test if API key is properly configured."""
    print("🔑 Testing API key configuration...")
    
    api_key = os.getenv('ANTHROPIC_API_KEY')
    if not api_key:
        print("❌ ANTHROPIC_API_KEY not found!")
        print("\n🔧 To fix this:")
        print("1. Get your API key from: https://console.anthropic.com/")
        print("2. Set it as an environment variable:")
        print("   export ANTHROPIC_API_KEY='your-api-key-here'")
        return False
    
    if not api_key.startswith('sk-ant-'):
        print("❌ API key format looks incorrect!")
        print("💡 Anthropic API keys should start with 'sk-ant-'")
        return False
    
    print("✅ API key found and format looks correct!")
    return True

def test_dependencies():
    """Test if required dependencies are installed."""
    print("\n📦 Testing dependencies...")
    
    try:
        import anthropic
        print("✅ anthropic library is installed!")
        return True
    except ImportError:
        print("❌ anthropic library not found!")
        print("\n🔧 To fix this:")
        print("pip install -r requirements.txt")
        return False

def test_api_connection():
    """Test actual API connection with a simple call."""
    print("\n🌐 Testing API connection...")
    
    try:
        import anthropic
        api_key = os.getenv('ANTHROPIC_API_KEY')
        client = anthropic.Anthropic(api_key=api_key)
        
        # Simple test call
        response = client.messages.create(
            model="claude-3-sonnet-20240229",
            max_tokens=50,
            messages=[{"role": "user", "content": "Say 'Hello from Claude!' and nothing else."}]
        )
        
        result = response.content[0].text.strip()
        if "Hello from Claude" in result:
            print("✅ API connection successful!")
            print(f"🤖 Claude says: {result}")
            return True
        else:
            print("❌ Unexpected response from Claude")
            return False
            
    except Exception as e:
        print(f"❌ API connection failed: {e}")
        print("\n💡 Common issues:")
        print("- Check your internet connection")
        print("- Verify your API key is correct")
        print("- Ensure you have API credits available")
        return False

def main():
    """Run all tests and provide summary."""
    print("🧪 Hello Claude Demo - Setup Test")
    print("=" * 40)
    
    tests = [
        ("API Key Configuration", test_api_key),
        ("Dependencies", test_dependencies),
        ("API Connection", test_api_connection)
    ]
    
    results = []
    for test_name, test_func in tests:
        try:
            result = test_func()
            results.append((test_name, result))
        except Exception as e:
            print(f"❌ {test_name} test failed with error: {e}")
            results.append((test_name, False))
    
    # Summary
    print("\n" + "=" * 40)
    print("📊 Test Results Summary:")
    
    all_passed = True
    for test_name, passed in results:
        status = "✅ PASS" if passed else "❌ FAIL"
        print(f"  {test_name}: {status}")
        if not passed:
            all_passed = False
    
    print("\n" + "=" * 40)
    if all_passed:
        print("🎉 All tests passed! You're ready to use the Hello Claude demo.")
        print("\n🚀 Try it out:")
        print("python main.py \"Your text to summarize here\"")
    else:
        print("⚠️  Some tests failed. Please fix the issues above before proceeding.")
        print("\n💡 Need help? Check the README.md for detailed setup instructions.")
    
    return 0 if all_passed else 1

if __name__ == "__main__":
    sys.exit(main()) 