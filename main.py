#!/usr/bin/env python3
"""
Hello Claude Demo - Text Summarization with Claude API

A simple, elegant demonstration of Claude's text summarization capabilities.
Designed for lightning-fast onboarding and immediate developer delight.

Usage:
    python main.py "Your text to summarize here"
    python main.py --file input.txt
"""

import os
import sys
import argparse
from typing import Optional
import anthropic
from pathlib import Path
import requests
from urllib.parse import urlparse


def get_api_key() -> str:
    """
    Get Claude API key from environment variable with helpful error message.
    
    Returns:
        str: The API key
        
    Raises:
        SystemExit: If API key is not found with helpful setup instructions
    """
    api_key = os.getenv('ANTHROPIC_API_KEY')
    if not api_key:
        print("❌ Error: ANTHROPIC_API_KEY environment variable not found!")
        print("\n🔧 Quick Setup:")
        print("1. Get your API key from: https://console.anthropic.com/")
        print("2. Set it as an environment variable:")
        print("   export ANTHROPIC_API_KEY='your-api-key-here'")
        print("   # or on Windows:")
        print("   set ANTHROPIC_API_KEY=your-api-key-here")
        print("\n💡 Pro tip: Add this to your ~/.bashrc or ~/.zshrc for persistence")
        sys.exit(1)
    return api_key


def read_file_content(file_path: str) -> str:
    """
    Read content from a file with error handling.
    
    Args:
        file_path (str): Path to the file to read
        
    Returns:
        str: File content
        
    Raises:
        SystemExit: If file cannot be read with helpful error message
    """
    try:
        path = Path(file_path)
        if not path.exists():
            print(f"❌ Error: File '{file_path}' not found!")
            sys.exit(1)
        
        content = path.read_text(encoding='utf-8')
        if not content.strip():
            print(f"❌ Error: File '{file_path}' is empty!")
            sys.exit(1)
            
        return content
    except UnicodeDecodeError:
        print(f"❌ Error: Could not read '{file_path}' - encoding issue!")
        print("💡 Try saving the file as UTF-8")
        sys.exit(1)


def read_url_content(url: str) -> str:
    """
    Read content from a URL with error handling.
    
    Args:
        url (str): URL to fetch content from
        
    Returns:
        str: URL content
        
    Raises:
        SystemExit: If URL cannot be fetched with helpful error message
    """
    try:
        print(f"🌐 Fetching content from: {url}")
        
        # Validate URL format
        parsed_url = urlparse(url)
        if not parsed_url.scheme or not parsed_url.netloc:
            print("❌ Error: Invalid URL format!")
            print("💡 Please provide a valid URL (e.g., https://example.com)")
            sys.exit(1)
        
        # Fetch content with timeout and user agent
        headers = {
            'User-Agent': 'Hello-Claude-Demo/1.0 (https://github.com/arun-gupta/hello-claude)'
        }
        
        response = requests.get(url, headers=headers, timeout=30)
        response.raise_for_status()
        
        # Try to extract text content
        content = response.text
        
        # Basic content validation
        if not content.strip():
            print("❌ Error: No content found at the URL!")
            sys.exit(1)
        
        # Limit content size to prevent excessive API usage
        if len(content) > 50000:  # 50KB limit
            print("⚠️  Warning: Content is very large, truncating to first 50KB")
            content = content[:50000]
        
        print(f"✅ Successfully fetched {len(content)} characters")
        return content
        
    except requests.exceptions.RequestException as e:
        print(f"❌ Error fetching URL: {e}")
        print("💡 Please check the URL and your internet connection")
        sys.exit(1)
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        print("💡 Please try again or use a different URL")
        sys.exit(1)


def summarize_text(text: str, api_key: str) -> str:
    """
    Summarize text using Claude API with comprehensive error handling.
    
    Args:
        text (str): Text to summarize
        api_key (str): Anthropic API key
        
    Returns:
        str: Summarized text
        
    Raises:
        SystemExit: If API call fails with helpful error message
    """
    try:
        client = anthropic.Anthropic(api_key=api_key)
        
        # Claude prompt for summarization
        prompt = f"""Please provide a clear, concise summary of the following text. 
Focus on the key points and main ideas while maintaining accuracy.

Text to summarize:
{text}

Summary:"""
        
        response = client.messages.create(
            model="claude-3-haiku-20240307",
            max_tokens=1000,
            temperature=0.3,  # Lower temperature for more focused summaries
            messages=[{"role": "user", "content": prompt}]
        )
        
        return response.content[0].text.strip()
        
    except anthropic.AuthenticationError:
        print("❌ Error: Invalid API key!")
        print("💡 Please check your ANTHROPIC_API_KEY and try again")
        sys.exit(1)
    except anthropic.RateLimitError:
        print("❌ Error: Rate limit exceeded!")
        print("💡 Please wait a moment and try again")
        sys.exit(1)
    except anthropic.APIError as e:
        print(f"❌ API Error: {e}")
        print("💡 Please check your internet connection and try again")
        sys.exit(1)
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        print("💡 Please check the documentation or try again later")
        sys.exit(1)


def main():
    """Main function with argument parsing and user-friendly output."""
    parser = argparse.ArgumentParser(
        description="Hello Claude Demo - Text Summarization",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python main.py "This is a long text that needs to be summarized..."
  python main.py --file document.txt
  python main.py --url https://example.com/article
  echo "Your text here" | python main.py
        """
    )
    
    parser.add_argument(
        'text',
        nargs='?',
        help='Text to summarize (or use --file or --url for other input methods)'
    )
    parser.add_argument(
        '--file', '-f',
        help='Read text from file instead of command line argument'
    )
    parser.add_argument(
        '--url', '-u',
        help='Fetch text from URL instead of command line argument'
    )
    
    args = parser.parse_args()
    
    # Get input text
    if args.url:
        text = read_url_content(args.url)
    elif args.file:
        text = read_file_content(args.file)
        print(f"📄 Reading from file: {args.file}")
    elif args.text:
        text = args.text
    else:
        # Read from stdin if no arguments provided
        print("📝 Enter text to summarize (Ctrl+D when done):")
        text = sys.stdin.read().strip()
        if not text:
            print("❌ No text provided!")
            parser.print_help()
            sys.exit(1)
    
    # Validate input
    if len(text) < 10:
        print("❌ Text is too short to summarize meaningfully!")
        print("💡 Please provide at least 10 characters")
        sys.exit(1)
    
    print(f"\n📊 Original text ({len(text)} characters):")
    print("-" * 50)
    print(text[:200] + ("..." if len(text) > 200 else ""))
    print("-" * 50)
    
    # Get API key and summarize
    print("\n🤖 Summarizing with Claude...")
    api_key = get_api_key()
    
    try:
        summary = summarize_text(text, api_key)
        
        print("\n✨ Summary:")
        print("=" * 50)
        print(summary)
        print("=" * 50)
        print(f"📈 Summary length: {len(summary)} characters")
        print(f"📉 Compression ratio: {len(summary)/len(text)*100:.1f}%")
        
    except KeyboardInterrupt:
        print("\n\n⏹️  Operation cancelled by user")
        sys.exit(0)


if __name__ == "__main__":
    main() 