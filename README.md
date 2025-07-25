# Claude Labs 🚀

> **Comprehensive Claude API showcase with interactive web interface** - Get started in under 5 minutes!

A comprehensive showcase of Claude's capabilities designed for immediate developer delight. This lab demonstrates how to build practical GenAI applications with minimal setup and maximum clarity, featuring interactive web interface, multiple input methods, and real-world use cases.

## ✨ Features

- **⚡ Lightning-fast setup** - From zero to working in under 5 minutes (or 30 seconds with cloud platforms!)
- **🌐 Beautiful web interface** - Interactive Streamlit app with chat, file upload, and more
- **🎯 Real-world use cases** - Chat, document analysis, web content processing, and more
- **🛡️ Bulletproof error handling** - Helpful messages that guide you to success
- **📖 Clean, well-commented code** - Easy to understand and modify
- **🔧 Multiple input methods** - Command line, file input, URL input, or stdin
- **📊 Smart analytics** - See compression ratios and character counts
- **🐍 Virtual environment** - Isolated dependencies for clean development

## 🚀 Quick Start (5 minutes or less!)

### 🌐 **Option 1: Cloud Platforms (Recommended!)**

**Zero setup, instant access to Claude's capabilities!**

**✨ Cloud Platform Benefits:**
- **🚀 Zero Setup** - Works immediately, no installation required
- **⚡ Instant Access** - Start using Claude in under 30 seconds
- **🌐 No Local Dependencies** - No Python, venv, or API key setup needed
- **💻 Full Development Environment** - VS Code, extensions, and tools included
- **🔒 Secure** - API keys managed securely by the platform

**☁️ GitHub Codespaces - Full VS Code environment:**
<a href="https://github.com/codespaces/new?template_repository=arun-gupta/claude-labs" target="_blank">
<img src="https://img.shields.io/badge/☁️_Open_Codespaces-181717?style=for-the-badge&logo=github&logoColor=white&labelColor=181717&color=181717" alt="Open in Codespaces" />
</a>
([Detailed setup guide](#️-github-codespaces))

**🚀 Replit - One-click setup:**
<a href="https://replit.com/new/github/arun-gupta/claude-labs" target="_blank">
<img src="https://img.shields.io/badge/🚀_Open_Replit-00D4FF?style=for-the-badge&logo=replit&logoColor=white&labelColor=00D4FF&color=00D4FF" alt="Open in Replit" />
</a>
([Detailed setup guide](#-replit-integration))

**⚡ Gitpod - Cloud development environment:**
<a href="https://gitpod.io/#https://github.com/arun-gupta/claude-labs" target="_blank">
<img src="https://img.shields.io/badge/⚡_Open_Gitpod-FFAE33?style=for-the-badge&logo=gitpod&logoColor=white&labelColor=FFAE33&color=FFAE33" alt="Open in Gitpod" />
</a>
([Detailed setup guide](#-gitpod-integration))

> 💡 **Why cloud platforms?** Zero setup, instant access, pre-configured environment, and you can start coding immediately!

### 💻 **Option 2: Local Interactive Web App**

**Experience Claude with a beautiful, interactive web interface on your local machine!**

```bash
git clone https://github.com/arun-gupta/claude-labs.git
cd claude-labs
./setup.sh
./web.sh
```

**✨ Local Web App Features:**
- **💬 Real-time Chat** - Talk with Claude instantly
- **📄 File Upload** - Drag & drop documents for summarization
- **🌐 URL Processing** - Fetch and summarize web content
- **🎨 Beautiful UI** - Modern, responsive design
- **⚙️ Model Selection** - Choose between Claude models

### 💻 Option 3: CLI Setup (For Developers)
```bash
git clone https://github.com/arun-gupta/claude-labs.git
cd claude-labs
./setup.sh
export ANTHROPIC_API_KEY='your-api-key-here'
python main.py --url https://www.anthropic.com/news/introducing-claude
```

**🔧 Perfect for:**
- **Automation & Scripts** - Easy to integrate into other tools
- **Server Environments** - No GUI needed
- **Power Users** - Developers who prefer command line
- **CI/CD Pipelines** - Automated testing and processing
- **Learning** - See how to use the API programmatically

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

### 💻 Option 4: Manual Setup
```bash
git clone https://github.com/arun-gupta/claude-labs.git
cd claude-labs

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

### 🛠️ Option 5: Using Make
```bash
git clone https://github.com/arun-gupta/claude-labs.git
cd claude-labs
make install
export ANTHROPIC_API_KEY='your-api-key-here'
make demo
```



## 🔑 API Key Setup

**First, get your API key:**
1. Visit [Anthropic Console](https://console.anthropic.com/)
2. Create an account and get your API key
3. **Important**: You need credits in your account to use the API

### **Where to Set Your API Key:**

#### **🌐 Replit:**
- Go to **Tools** → **Secrets** (scroll down)
- Add new secret: `ANTHROPIC_API_KEY` = `your-api-key-here`

#### **☁️ GitHub Codespaces:**
- In the terminal: `export ANTHROPIC_API_KEY='your-api-key-here'`
- Or add to environment variables in VS Code settings

#### **⚡ Gitpod:**
- In the terminal: `export ANTHROPIC_API_KEY='your-api-key-here'`
- Or add to workspace environment variables in Gitpod settings

#### **💻 Local Development:**
- **Session only**: `export ANTHROPIC_API_KEY='your-api-key-here'`
- **Permanent**: Add to `~/.bashrc` or `~/.zshrc`
- **Windows**: `set ANTHROPIC_API_KEY=your-api-key-here`

## 🌐 Cloud Platform Integrations

This project is configured for multiple cloud development platforms!

### ☁️ **GitHub Codespaces**

<div align="center">

<a href="https://github.com/codespaces/new?template_repository=arun-gupta/claude-labs" target="_blank">
<img src="https://img.shields.io/badge/☁️_Open_Codespaces-181717?style=for-the-badge&logo=github&logoColor=white&labelColor=181717&color=181717" alt="Open GitHub Codespaces" />
</a>

</div>

**On GitHub Codespaces:**
1. **Click**: [![Open in Codespaces](https://img.shields.io/badge/☁️_Open_Codespaces-181717?style=for-the-badge&logo=github&logoColor=white&labelColor=181717&color=181717)](https://github.com/codespaces/new?template_repository=arun-gupta/claude-labs)
2. **Create**: Click "Create codespace on main" (defaults work fine)
3. **Set API Key**: In terminal: `export ANTHROPIC_API_KEY='your-api-key-here'`
4. **Run**: `./web.sh`
5. **Access Web App**: Go to **Ports** tab → Click **"Open in Browser"** next to port 8501

**Features:**
- ✅ **Full VS Code**: Complete development environment
- ✅ **Port Forwarding**: Web app accessible via Ports tab
- ✅ **Git Integration**: Direct access to repository
- ✅ **Environment Variables**: Easy API key management
- ✅ **Extensions**: Rich ecosystem of development tools
- ✅ **Auto-setup**: Dependencies installed automatically

### 🚀 **Replit Integration**

<div align="center">

<a href="https://replit.com/new/github/arun-gupta/claude-labs" target="_blank">
<img src="https://img.shields.io/badge/🚀_Open_Replit-00D4FF?style=for-the-badge&logo=replit&logoColor=white&labelColor=00D4FF&color=00D4FF" alt="Open Replit" />
</a>

</div>

**On Replit:**
1. **Click**: The "Open in Replit" button above
2. **Import**: Click "Import from GitHub" (one-click setup!)
3. **Set API Key**: Go to Tools → Secrets → Add `ANTHROPIC_API_KEY`
4. **Run**: Click the Run button to launch the web app
5. **Access Web App**: The web app opens automatically in the **Webview** tab above the terminal

**Features:**
- ✅ **Auto-install**: Dependencies installed automatically
- ✅ **Environment**: Python 3.9 with all required packages
- ✅ **Secrets**: Secure API key management
- ✅ **Webview Integration**: Web app opens automatically in Replit's Webview tab

### ⚡ **Gitpod Integration**

<div align="center">

<a href="https://gitpod.io/#https://github.com/arun-gupta/claude-labs" target="_blank">
<img src="https://img.shields.io/badge/⚡_Open_Gitpod-FFAE33?style=for-the-badge&logo=gitpod&logoColor=white&labelColor=FFAE33&color=FFAE33" alt="Open in Gitpod" />
</a>

</div>

**On Gitpod:**
1. **Click**: The "Open in Gitpod" button above
2. **Wait**: Gitpod will automatically set up the environment
3. **Set API Key**: In terminal: `export ANTHROPIC_API_KEY='your-api-key-here'`
4. **Run**: `./web.sh`
5. **Access Web App**: Go to **Ports** tab → Click **"Open in Browser"** next to port 8501

**Features:**
- ✅ **Instant Setup**: Pre-configured Python environment with all dependencies
- ✅ **Port Forwarding**: Web app accessible via Ports tab
- ✅ **VS Code Experience**: Full IDE with extensions and debugging
- ✅ **Development Tools**: Black, Flake8, isort, and Pylint pre-installed
- ✅ **Git Integration**: Direct access to repository and version control
- ✅ **Free Tier**: Generous free usage for development and testing
- ✅ **Auto-activation**: Virtual environment automatically activated

## 📊 **Priority 3: Monitoring & Analytics**

### **Analytics Dashboard:**
```bash
# View comprehensive analytics
python analytics.py

# Or use main.py with analytics flag
python main.py --analytics

# Export analytics to JSON
python main.py --export-analytics claude_analytics.json
```

### **Monitoring Features:**
- **📈 Real-time Metrics** - Token usage, response times, costs
- **🔍 Error Analysis** - Detailed error tracking with suggestions
- **⚡ Rate Limiting** - Intelligent retry logic and backoff
- **📊 Usage Analytics** - Model usage, success rates, performance insights
- **📝 Detailed Logging** - Complete request/response logs in `claude_labs.log`

### **Error Tracking:**
The system now provides intelligent error analysis with specific suggestions for:
- **Authentication errors** - API key issues and solutions
- **Rate limiting** - Wait times and optimization tips
- **Model errors** - Correct model names and usage
- **Network issues** - Connection troubleshooting

## 📖 Usage Examples

### 🌐 URL Input (Recommended!)
```bash
source venv/bin/activate
python main.py --url https://www.anthropic.com/news/introducing-claude
```

> 💡 **Try this URL**: Copy/paste the commands above to test with a real article about Claude!
> 
> **🎯 Perfect for testing**: This URL demonstrates the tool's ability to fetch and summarize real web content instantly!

### 📄 File Input
```bash
source venv/bin/activate
python main.py --file samples/document.txt
```

> 💡 **Try these sample files**: 
> - `samples/document.txt` - Comprehensive AI article (2,500+ characters)
> - `samples/sample.txt` - Shorter AI overview (1,000+ characters)

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

## 🌐 **Web Interface (Primary Experience!)**

Experience Claude with a beautiful, interactive web interface! This is the recommended way to explore Claude's capabilities.

### **Launch the Web App:**
```bash
# Option 1: Simple shell script (easiest)
./web.sh

# Option 2: Python script
python web.py

# Option 3: Direct Streamlit
streamlit run app.py

# Option 4: Using Make
make web
```

### **Web App Features:**
- **💬 Chat Interface** - Real-time conversation with Claude
- **📄 File Upload** - Drag & drop documents for summarization
- **🌐 URL Processing** - Fetch and summarize web content
- **📊 Analytics** - API status, model info, usage statistics
- **🎨 Beautiful UI** - Modern, responsive design
- **⚙️ Model Selection** - Choose between Claude models
- **🔑 Easy API Setup** - Set API key in the sidebar

### **Web App Screenshots:**
*Coming soon! The web interface provides a much more engaging way to interact with Claude.*

## 📊 Expected Output

**💡 See [DEMO_OUTPUT.md](DEMO_OUTPUT.md) for detailed examples with screenshots, different input methods, and real output samples.**

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

### ❌ "zsh: command not found: #" or "command not found" errors
**Solution:** You copied the comment lines! Only copy the actual commands:
```bash
# ❌ Don't copy this line (it's a comment)
source venv/bin/activate
python main.py --url https://www.anthropic.com/news/introducing-claude
```
Copy only the lines without `#` at the beginning.

### ❌ "Can't find Codespaces button" or "Codespaces not working"
**Solution:** Use the direct Codespaces link:
1. **Click**: [Open in Codespaces](https://github.com/codespaces/new?template_repository=arun-gupta/claude-labs)
2. **Alternative**: Use Replit integration instead

## 🏗️ Project Structure

```
claude-labs/
├── main.py              # Main application with comprehensive error handling
├── app.py               # Streamlit web interface
├── web.py               # Simple Python web app launcher
├── web.sh               # Simple shell script web app launcher
├── run_web_app.py       # Advanced web app launcher script
├── requirements.txt     # Python dependencies including Streamlit
├── README.md           # This file - your guide to success
├── QUICKSTART.md       # Lightning-fast setup guide
├── setup.sh            # Automated setup script with virtual environment
├── test_setup.py       # Setup verification script
├── demo.py             # Showcase script with predefined example
├── Makefile            # Development workflow commands
├── samples/            # Test documents and sample files
│   ├── document.txt    # Comprehensive AI article (2,500+ chars)
│   └── sample.txt      # Shorter AI overview (1,000+ chars)
├── .replit             # Replit configuration
├── .devcontainer/      # GitHub Codespaces configuration
│   └── devcontainer.json
├── .gitpod.yml         # Gitpod configuration
├── pyproject.toml      # Modern Python packaging

├── replit-setup.sh     # Replit-specific setup script
├── assets/             # Images and screenshots
│   ├── replit-output.png
│   └── codesapces-output.png
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
make web        # Launch the Streamlit web app
make web-direct # Launch Streamlit app directly
make clean      # Clean up Python cache files
```

### **Simple Web App Launch:**
```bash
./web.sh        # Shell script (easiest)
python web.py   # Python script
streamlit run app.py  # Direct Streamlit
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

This lab exemplifies excellent Developer Experience (DX) inspired by Claude's clarity and ease:

- **One-Click Deployment** - Replit integration for instant cloud execution
- **Zero Setup Friction** - Works immediately with minimal configuration
- **Cloud-First Design** - Optimized for cloud environments like Replit
- **Secure Secrets Management** - API keys handled safely via environment variables
- **Virtual Environment** - Isolated dependencies for clean development
- **Minimal Dependencies** - Only essential packages
- **Clear Error Messages** - Helpful guidance when things go wrong
- **Multiple Input Methods** - Flexibility for different use cases
- **Comprehensive Documentation** - Everything you need to succeed
- **Clean Code** - Well-commented, easy to understand and modify
- **Immediate Feedback** - See results and analytics instantly
- **Visual Documentation** - Screenshots and clear visual guides

## 🔗 Resources

- [Anthropic Claude API Documentation](https://docs.anthropic.com/)
- [Anthropic Console](https://console.anthropic.com/) - Get your API key
- [Python Anthropic Library](https://github.com/anthropics/anthropic-sdk-python)
- [Python Virtual Environments](https://docs.python.org/3/tutorial/venv.html)



## 🚀 Future Improvements (Claude-Style DX)

We're planning to enhance this lab with even better developer experience. Here's our roadmap:

### **🎯 Priority 1: Enhanced CLI & User Experience** ✅
- [x] **Rich terminal output** with colors, progress bars, and emojis
- [ ] **Interactive prompts** for API key setup and configuration
- [ ] **Real-time streaming** of Claude responses
- [ ] **File drag-and-drop** support for easier file input
- [ ] **Command-line autocomplete** for better discoverability

**🎉 Summary:** Transformed basic CLI into a beautiful, interactive experience with Rich library - featuring colorful panels, progress bars, formatted tables, and enhanced error handling for immediate developer delight.

### **🔧 Priority 2: Developer Tools & Quality**
- [ ] **Pre-commit hooks** for automated code quality checks
- [ ] **Type checking** with mypy for better code safety
- [ ] **Auto-formatting** with black/isort for consistent code style
- [ ] **Advanced linting** with ruff for comprehensive code analysis
- [ ] **Code coverage** reporting with pytest-cov

### **📊 Priority 3: Monitoring & Debugging** ✅
- [x] **Request/response logging** with detailed timestamps
- [x] **Performance metrics** (token usage, response time, cost tracking)
- [x] **Error tracking** with detailed stack traces and suggestions
- [x] **Rate limiting** and intelligent retry logic
- [x] **Usage analytics** dashboard

**🎉 Summary:** Implemented comprehensive production monitoring with detailed logging, performance metrics, intelligent error tracking, rate limiting, and analytics dashboard - providing full visibility into Claude API usage and system health.

### **🧪 Priority 4: Testing & Reliability**
- [ ] **Unit tests** with pytest for core functionality
- [ ] **Integration tests** for API calls with mocked responses
- [ ] **End-to-end tests** for complete user workflows
- [ ] **Performance benchmarks** for optimization tracking
- [ ] **Automated testing** in CI/CD pipeline

### **🎨 Priority 5: Modern UI/UX**
- [ ] **Web interface** with FastAPI/Streamlit for broader accessibility
- [ ] **Real-time chat interface** similar to Claude's web app
- [ ] **File upload interface** with drag-and-drop support
- [ ] **Response history** and conversation management
- [ ] **Dark/light theme** support

### **🔐 Priority 6: Security & Configuration**
- [ ] **Config file support** (.env, config.yaml, toml)
- [ ] **API key rotation** helpers and security best practices
- [ ] **Environment-specific** configurations (dev/staging/prod)
- [ ] **Secrets management** integration (AWS Secrets Manager, etc.)
- [ ] **Audit logging** for security compliance

### **📚 Priority 7: Documentation & Learning**
- [ ] **Interactive tutorials** with Jupyter notebooks
- [ ] **API documentation** with OpenAPI/Swagger specs
- [ ] **Video walkthroughs** embedded in README
- [ ] **Code examples** for different use cases
- [ ] **Best practices guide** for Claude API usage

### **⚡ Priority 8: Performance & Scalability**
- [ ] **Async support** for concurrent API requests
- [ ] **Caching layer** for repeated summaries
- [ ] **Batch processing** for multiple files
- [ ] **Memory optimization** for large documents
- [ ] **Load balancing** for high-traffic scenarios

### **🎯 Implementation Strategy**
1. **✅ Priority 1** - Enhanced CLI with Rich terminal output, beautiful panels, progress bars
2. **Add Priority 2** - Developer confidence and code quality
3. **Implement Priority 3** - Production readiness and monitoring
4. **Build Priority 4** - Reliability and testing foundation
5. **Enhance with Priorities 5-8** - Advanced features and scalability

---

## 🤝 Contributing

This is a lab project designed to showcase excellent DX. Feel free to:
- Fork and modify for your own projects
- Submit issues for improvements
- Share with your team as a reference for good practices
- **Help implement** any of the future improvements above!

## 📄 License

Apache License 2.0 - feel free to use this code in your own projects!

---

**Built with ❤️ for developers who appreciate clean, working code that just works.** 