# Hello Claude Demo 🚀

> **Lightning-fast text summarization with Claude API** - Get started in under 5 minutes!

A clean, elegant demonstration of Claude's text summarization capabilities designed for immediate developer delight. This demo showcases how to build practical GenAI applications with minimal setup and maximum clarity.

## ✨ Features

- **⚡ Lightning-fast setup** - From zero to working in under 5 minutes
- **🎯 Real-world use case** - Practical text summarization that actually works
- **🛡️ Bulletproof error handling** - Helpful messages that guide you to success
- **📖 Clean, well-commented code** - Easy to understand and modify
- **🔧 Multiple input methods** - Command line, file input, URL input, or stdin
- **📊 Smart analytics** - See compression ratios and character counts
- **🐍 Virtual environment** - Isolated dependencies for clean development

## 🚀 Quick Start (5 minutes or less!)

### 🌐 Option 1: Try on Replit (Easiest!)
<div align="center">

<a href="https://replit.com" target="_blank">
<img src="https://img.shields.io/badge/🚀_Open_Replit-00D4FF?style=for-the-badge&logo=replit&logoColor=white&labelColor=00D4FF&color=00D4FF" alt="Open Replit" />
</a>

</div>

**📋 Copy this URL:** `https://github.com/arun-gupta/hello-claude`

1. Click the "Open Replit" button above
2. Click **"Import code or design"** → **"GitHub"**
3. Paste the URL above: `https://github.com/arun-gupta/hello-claude`
4. Set your API key: **Tools** → **Secrets** (scroll down to find it)
5. Click "Run" to test the demo!

### 💻 Option 2: Automated Setup (Local)
```bash
git clone https://github.com/yourusername/hello-claude.git
cd hello-claude
./setup.sh
```

The setup script will:
- ✅ Create a virtual environment
- ✅ Install dependencies
- ✅ Guide you through getting your API key
- ✅ Help you set up the API key securely
- ✅ Test your setup automatically

**API Key Options:**
- **Session Only**: Set for current terminal session (temporary)
- **Permanent**: Save to shell config file (persistent)
- **Skip**: Set up later using `./set_api_key.sh`

### Option 2: Manual Setup
```bash
git clone https://github.com/yourusername/hello-claude.git
cd hello-claude

# Create and activate virtual environment
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Get your API key
export ANTHROPIC_API_KEY='your-api-key-here'

# Try it out!
python main.py "This is a long text that needs to be summarized into a concise version that captures the key points and main ideas."
```

### Option 3: Using Make
```bash
git clone https://github.com/yourusername/hello-claude.git
cd hello-claude
make install
export ANTHROPIC_API_KEY='your-api-key-here'
make demo
```

## 🔑 Get Your API Key

1. Visit [Anthropic Console](https://console.anthropic.com/)
2. Create an account and get your API key
3. Set it as an environment variable:
   ```bash
   export ANTHROPIC_API_KEY='your-api-key-here'
   ```

**💡 Important**: You need a valid API key with credits to use the demo. See [DEMO_OUTPUT.md](DEMO_OUTPUT.md) for examples of what the output looks like.

## 🌐 Replit Integration

This project is fully configured for Replit! 

### **On Replit:**
1. **Import**: Click "Import code or design" → "GitHub" → Paste repository URL
2. **Set API Key**: Go to Tools → Secrets (scroll down) → Add `ANTHROPIC_API_KEY`
3. **Run**: Click the Run button to test with the Anthropic article
4. **Customize**: Modify the `.replit` file to change the default command

### **Replit Features:**
- ✅ **Auto-install**: Dependencies installed automatically
- ✅ **Environment**: Python 3.9 with all required packages
- ✅ **Secrets**: Secure API key management
- ✅ **One-click run**: Pre-configured to test URL input
- ✅ **Live preview**: See results instantly

## 📖 Usage Examples

### 🌐 URL Input (Easiest!)
```bash
# Activate virtual environment first
source venv/bin/activate

# Then fetch and summarize any webpage
python main.py --url https://www.anthropic.com/news/introducing-claude
```

> 💡 **Try this URL**: Copy/paste the command above to test with a real article about Claude!

### 📄 File Input
```bash
source venv/bin/activate
python main.py --file document.txt
```

### 📝 Command Line Input
```bash
source venv/bin/activate
python main.py "Your text here"
```

### Interactive Mode
```bash
source venv/bin/activate
python main.py
# Then type your text and press Ctrl+D when done
```

### Pipeline Usage
```bash
source venv/bin/activate
echo "Your text here" | python main.py
```

## 📊 Expected Output

```
📊 Original text (89 characters):
--------------------------------------------------
This is a long text that needs to be summarized into a concise version that captures the key points and main ideas.
--------------------------------------------------

🤖 Summarizing with Claude...

✨ Summary:
==================================================
This text discusses the need to condense lengthy content into a brief summary that maintains the essential information and core concepts.
==================================================
📈 Summary length: 127 characters
📉 Compression ratio: 142.7%
```

## 🔧 Troubleshooting

### ❌ "ANTHROPIC_API_KEY environment variable not found!"
**Solution:** Set your API key as an environment variable:
```bash
export ANTHROPIC_API_KEY='your-api-key-here'
```

### ❌ "Virtual environment not found!"
**Solution:** Create and activate the virtual environment:
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### ❌ "Invalid API key!"
**Solution:** Check your API key at [Anthropic Console](https://console.anthropic.com/) and ensure it's correct.

### ❌ "Rate limit exceeded!"
**Solution:** Wait a moment and try again. Claude has rate limits to ensure fair usage.

### ❌ "File not found!"
**Solution:** Check the file path and ensure the file exists in the current directory.

### ❌ "Text is too short to summarize meaningfully!"
**Solution:** Provide at least 10 characters of text for meaningful summarization.

## 🏗️ Project Structure

```
hello-claude/
├── main.py              # Main application with comprehensive error handling
├── requirements.txt     # Minimal dependencies (just anthropic)
├── README.md           # This file - your guide to success
├── QUICKSTART.md       # Lightning-fast setup guide
├── setup.sh            # Automated setup script with virtual environment
├── test_setup.py       # Setup verification script
├── demo.py             # Showcase script with predefined example
├── Makefile            # Development workflow commands
├── sample.txt          # Sample text for testing
├── document.txt        # Sample document for testing
├── .replit             # Replit configuration
├── pyproject.toml      # Modern Python packaging

├── replit-setup.sh     # Replit-specific setup script
├── assets/             # Images and screenshots
│   └── replit-screenshots/  # Replit interface screenshots
├── venv/               # Virtual environment (created during setup)
├── .gitignore          # Prevents accidental commits of secrets
└── LICENSE             # Apache License 2.0 for maximum freedom

## 🛠️ Development Commands

### Using Make
```bash
make help       # Show all available commands
make venv       # Create virtual environment
make install    # Install dependencies (creates venv if needed)
make test       # Run setup verification tests
make demo       # Run the demo with example text
make clean      # Clean up Python cache files
```

### Using Setup Script
```bash
./setup.sh      # Automated setup with virtual environment
```

### API Key Management
```bash
# Option 1: Run script (API key only available in script)
./set_api_key.sh

# Option 2: Set manually (recommended)
export ANTHROPIC_API_KEY='your-api-key-here'

# Option 3: Use setup script with interactive API key setup
./setup.sh
```

### Manual Commands
```bash
# Create virtual environment
python3 -m venv venv

# Activate virtual environment
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run tests
python test_setup.py

# Run demo
python demo.py
```

## 🎯 Key Design Principles

This demo exemplifies excellent Developer Experience (DX) inspired by Claude's clarity and ease:

- **Virtual Environment** - Isolated dependencies for clean development
- **Minimal Dependencies** - Only essential packages
- **Clear Error Messages** - Helpful guidance when things go wrong
- **Multiple Input Methods** - Flexibility for different use cases
- **Comprehensive Documentation** - Everything you need to succeed
- **Clean Code** - Well-commented, easy to understand and modify
- **Immediate Feedback** - See results and analytics instantly

## 🔗 Resources

- [Anthropic Claude API Documentation](https://docs.anthropic.com/)
- [Anthropic Console](https://console.anthropic.com/) - Get your API key
- [Python Anthropic Library](https://github.com/anthropics/anthropic-sdk-python)
- [Python Virtual Environments](https://docs.python.org/3/tutorial/venv.html)

## 🚀 Try It Live!

[![Run on Replit](https://replit.com/badge/github/yourusername/hello-claude)](https://replit.com/github/yourusername/hello-claude)

Click the badge above to try this demo instantly in your browser - no setup required!

## 🤝 Contributing

This is a demo project designed to showcase excellent DX. Feel free to:
- Fork and modify for your own projects
- Submit issues for improvements
- Share with your team as a reference for good practices

## 📄 License

Apache License 2.0 - feel free to use this code in your own projects!

---

**Built with ❤️ for developers who appreciate clean, working code that just works.** 