# ⚡ Quick Start Guide

> **Get Hello Claude Demo running in under 2 minutes!**

## 🚀 Super Quick Start

### Option 1: Automated Setup (Recommended)
```bash
git clone https://github.com/yourusername/hello-claude.git
cd hello-claude
./setup.sh
```

The setup script will guide you through everything, including getting your API key!

### Option 2: Manual Setup
```bash
git clone https://github.com/yourusername/hello-claude.git
cd hello-claude

# Create and activate virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Get your API key
export ANTHROPIC_API_KEY='your-key-here'

# Try it
python main.py "Your text to summarize here"
```

### Option 3: Using Make
```bash
git clone https://github.com/yourusername/hello-claude.git
cd hello-claude
make install
export ANTHROPIC_API_KEY='your-key-here'
make demo
```

## 🎯 One-Liner Setup

```bash
git clone https://github.com/yourusername/hello-claude.git && cd hello-claude && python3 -m venv venv && source venv/bin/activate && pip install -r requirements.txt && export ANTHROPIC_API_KEY='your-key' && python main.py "Test text"
```

## 🧪 Test Your Setup

```bash
source venv/bin/activate
python test_setup.py
```

## 🔑 Set API Key (if needed)

```bash
# Set API key manually (recommended)
export ANTHROPIC_API_KEY='your-api-key-here'

# Or use the setup script
./setup.sh
```

## 🎬 Run Demo

```bash
source venv/bin/activate
python demo.py
```

## 📁 File Input

```bash
source venv/bin/activate
python main.py --file document.txt
```

## 🌐 URL Input

```bash
source venv/bin/activate
python main.py --url https://www.anthropic.com/news/introducing-claude
```

## 🛠️ Make Commands

```bash
make venv       # Create virtual environment
make install    # Install dependencies (creates venv if needed)
make test       # Test setup
make demo       # Run demo
make help       # Show all commands
```

## 🔧 Virtual Environment

**Always activate the virtual environment before running the demo:**
```bash
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

**To deactivate:**
```bash
deactivate
```

## ❓ Need Help?

- Check the main [README.md](README.md) for detailed instructions
- Run `python main.py --help` for usage options
- See troubleshooting section in README.md

---

**That's it! You should be up and running in under 2 minutes.** 🎉 