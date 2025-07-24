# Sample Files for Testing

This directory contains sample text files for testing Claude Labs.

## 📄 Available Samples

### `document.txt` - Comprehensive AI Article
- **Size**: ~2,500 characters
- **Content**: Detailed analysis of AI's future, challenges, and ethical considerations
- **Use case**: Test summarization of longer, complex content
- **Command**: `python main.py --file samples/document.txt`

### `sample.txt` - AI Overview
- **Size**: ~1,000 characters  
- **Content**: Concise overview of AI and Machine Learning concepts
- **Use case**: Test summarization of shorter, focused content
- **Command**: `python main.py --file samples/sample.txt`

## 🎯 How to Use

1. **Activate your virtual environment**:
   ```bash
   source venv/bin/activate
   ```

2. **Test with any sample**:
   ```bash
   python main.py --file samples/document.txt
   python main.py --file samples/sample.txt
   ```

## 📝 Adding Your Own Samples

Feel free to add your own text files to this directory for testing:
- Plain text files (`.txt`) work best
- Files should be at least 10 characters long
- Large files (>50KB) will be automatically truncated

## 🔍 File Requirements

- **Format**: Plain text (UTF-8)
- **Minimum length**: 10 characters
- **Maximum length**: 50KB (auto-truncated)
- **Encoding**: UTF-8 recommended 