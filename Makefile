# Claude Labs - Makefile
# Common development tasks for easy project management

.PHONY: help install test demo clean setup venv activate

# Default target
help:
	@echo "🚀 Claude Labs - Available Commands"
	@echo "========================================"
	@echo "make venv       - Create virtual environment"
	@echo "make activate   - Activate virtual environment"
	@echo "make install    - Install dependencies (creates venv if needed)"
	@echo "make setup      - Run automated setup script"
	@echo "make test       - Run setup verification tests"
	@echo "make demo       - Run the demo with example text"
	@echo "make web        - Launch the Streamlit web app"
	@echo "make web-direct - Launch Streamlit app directly"
	@echo "make clean      - Clean up Python cache files"
	@echo "make help       - Show this help message"

# Create virtual environment
venv:
	@echo "🐍 Creating virtual environment..."
	python3 -m venv venv
	@echo "✅ Virtual environment created!"
	@echo "💡 Activate it with: source venv/bin/activate"

# Activate virtual environment (informational)
activate:
	@echo "🔧 To activate the virtual environment, run:"
	@echo "   source venv/bin/activate"
	@echo ""
	@echo "💡 Or use the setup script: ./setup.sh"

# Install dependencies (creates venv if needed)
install: venv
	@echo "📦 Installing dependencies..."
	@source venv/bin/activate && pip install --upgrade pip
	@source venv/bin/activate && pip install -r requirements.txt
	@echo "✅ Dependencies installed!"

# Run automated setup
setup:
	@echo "🚀 Running automated setup..."
	@chmod +x setup.sh
	./setup.sh

# Run setup tests
test:
	@echo "🧪 Running setup verification tests..."
	@if [ ! -d "venv" ]; then \
		echo "❌ Virtual environment not found!"; \
		echo "💡 Run 'make install' or 'make setup' first"; \
		exit 1; \
	fi
	@source venv/bin/activate && python test_setup.py

# Run demo
demo:
	@echo "🎬 Running demo..."
	@if [ ! -d "venv" ]; then \
		echo "❌ Virtual environment not found!"; \
		echo "💡 Run 'make install' or 'make setup' first"; \
		exit 1; \
	fi
	@source venv/bin/activate && python demo.py

# Launch web app
web:
	@echo "🌐 Launching Claude Labs Web App..."
	@if [ ! -d "venv" ]; then \
		echo "❌ Virtual environment not found!"; \
		echo "💡 Run 'make install' or 'make setup' first"; \
		exit 1; \
	fi
	@source venv/bin/activate && python run_web_app.py

# Launch web app directly
web-direct:
	@echo "🌐 Launching Streamlit app directly..."
	@if [ ! -d "venv" ]; then \
		echo "❌ Virtual environment not found!"; \
		echo "💡 Run 'make install' or 'make setup' first"; \
		exit 1; \
	fi
	@source venv/bin/activate && streamlit run app.py --server.port 8501 --server.address localhost

# Clean up cache files
clean:
	@echo "🧹 Cleaning up cache files..."
	find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
	find . -name "*.pyc" -delete 2>/dev/null || true
	find . -name "*.pyo" -delete 2>/dev/null || true
	@echo "✅ Cleanup complete!"

# Quick start (install + test)
quickstart: install test
	@echo "🎉 Quick start complete!"
	@echo "💡 Set your ANTHROPIC_API_KEY and run 'make demo' to try it out!"
	@echo "💡 Remember to activate the virtual environment: source venv/bin/activate" 