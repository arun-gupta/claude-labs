# 🐍 Virtual Environment Guide

> **Why virtual environments matter and how to use them with Claude Labs**

## 🤔 Why Virtual Environments?

Virtual environments are isolated Python environments that prevent dependency conflicts between projects. Here's why they're important:

- **🔒 Isolation**: Each project has its own dependencies
- **🧹 Clean**: No conflicts with system Python packages
- **📦 Reproducible**: Same environment across different machines
- **🛡️ Safe**: Won't break other Python projects on your system

## 🚀 Quick Virtual Environment Setup

### Option 1: Automated (Recommended)
```bash
./setup.sh
```

### Option 2: Manual
```bash
# Create virtual environment
python3 -m venv venv

# Activate it
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### Option 3: Using Make
```bash
make install  # Creates venv and installs dependencies
```

## 🔧 Virtual Environment Commands

### Activation
```bash
# Unix/macOS
source venv/bin/activate

# Windows
venv\Scripts\activate
```

### Deactivation
```bash
deactivate
```

### Check if Active
```bash
# Look for (venv) in your prompt
# Or run:
which python  # Should show path to venv/bin/python
```

## 📁 Project Structure with Virtual Environment

```
claude-labs/
├── main.py              # Main application
├── requirements.txt     # Dependencies list
├── venv/               # Virtual environment (created during setup)
│   ├── bin/            # Python executables
│   ├── lib/            # Installed packages
│   └── ...
├── setup.sh            # Automated setup script
├── Makefile            # Development commands
└── ...
```

## 🛠️ Development Workflow

### 1. First Time Setup
```bash
git clone https://github.com/arun-gupta/claude-labs.git
cd claude-labs
./setup.sh
```

### 2. Daily Usage
```bash
# Activate virtual environment
source venv/bin/activate

# Run the demo
python main.py "Your text here"

# Deactivate when done
deactivate
```

### 3. Adding New Dependencies
```bash
source venv/bin/activate
pip install new-package
pip freeze > requirements.txt  # Update requirements
```

## 🚨 Common Issues & Solutions

### ❌ "Command not found: python"
**Solution**: Activate the virtual environment first:
```bash
source venv/bin/activate
```

### ❌ "Module not found"
**Solution**: Install dependencies in the virtual environment:
```bash
source venv/bin/activate
pip install -r requirements.txt
```

### ❌ "Permission denied"
**Solution**: Make sure the virtual environment is owned by your user:
```bash
chmod -R 755 venv/
```

### ❌ "Virtual environment not found"
**Solution**: Recreate the virtual environment:
```bash
rm -rf venv/
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## 🎯 Best Practices

### ✅ Do This
- Always activate the virtual environment before running the demo
- Use `requirements.txt` to track dependencies
- Deactivate when switching between projects
- Commit `requirements.txt` to version control

### ❌ Don't Do This
- Install packages globally with `pip install`
- Modify the virtual environment manually
- Commit the `venv/` directory to version control
- Run Python scripts without activating the environment

## 🔄 Updating Dependencies

```bash
# Activate virtual environment
source venv/bin/activate

# Update a specific package
pip install --upgrade anthropic

# Update all packages
pip install --upgrade -r requirements.txt

# Save new requirements
pip freeze > requirements.txt
```

## 🧹 Cleanup

### Remove Virtual Environment
```bash
deactivate  # If active
rm -rf venv/
```

### Clean Python Cache
```bash
make clean
# or manually:
find . -name "__pycache__" -delete
find . -name "*.pyc" -delete
```

## 🌍 Cross-Platform Support

### Unix/macOS
```bash
source venv/bin/activate
```

### Windows
```bash
venv\Scripts\activate
# or use the provided activate.bat script
```

### PowerShell
```bash
venv\Scripts\Activate.ps1
```

## 📚 Additional Resources

- [Python Virtual Environments Documentation](https://docs.python.org/3/tutorial/venv.html)
- [pip User Guide](https://pip.pypa.io/en/stable/user_guide/)
- [Python Packaging User Guide](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

---

**💡 Pro Tip**: Always check if your virtual environment is active by looking for `(venv)` in your terminal prompt! 