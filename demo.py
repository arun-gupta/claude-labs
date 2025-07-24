#!/usr/bin/env python3
"""
Hello Claude Demo - Showcase Script

This script demonstrates the text summarization functionality
with a predefined example. Perfect for demos and testing!
"""

import os
import sys

# Add the current directory to the path so we can import main
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

def run_demo():
    """Run the demo with a predefined example."""
    
    # Example text about AI and machine learning
    demo_text = """
    Artificial Intelligence (AI) and Machine Learning (ML) represent one of the most transformative technological developments of our time. These technologies are fundamentally changing how we approach problem-solving, decision-making, and automation across virtually every industry and sector of society.

    Machine Learning, a subset of AI, focuses on developing algorithms that can learn patterns from data and make predictions or decisions without being explicitly programmed for each specific task. This approach has proven remarkably effective in areas such as computer vision, natural language processing, recommendation systems, autonomous vehicles, and medical diagnosis.

    The recent explosion in AI/ML capabilities has been driven by several key factors: the availability of massive datasets for training, exponential increases in computational power, and breakthroughs in neural network architectures, particularly deep learning. These advances have enabled AI systems to achieve human-level or even superhuman performance in many specialized domains.

    However, the rapid advancement of AI/ML also presents significant challenges that society must address. These include concerns about bias in training data that can perpetuate existing inequalities, privacy implications of data collection and processing, potential job displacement as automation increases, and the need for explainable AI systems that can justify their decisions in critical applications.

    Looking forward, AI and ML are expected to continue their rapid evolution, with applications spanning healthcare, education, transportation, finance, entertainment, and beyond. The key to successful and responsible implementation lies in thoughtful design, robust testing, ongoing collaboration between technologists and domain experts, and the development of appropriate regulatory frameworks to ensure these powerful tools serve humanity's best interests while minimizing potential harms.
    """
    
    print("🎬 Hello Claude Demo - Live Showcase")
    print("=" * 50)
    print("This demo will summarize a comprehensive text about AI and ML.")
    print("=" * 50)
    
    # Check if API key is available
    if not os.getenv('ANTHROPIC_API_KEY'):
        print("❌ ANTHROPIC_API_KEY not found!")
        print("\n🔧 To run this demo:")
        print("1. Get your API key from: https://console.anthropic.com/")
        print("2. Set it as an environment variable:")
        print("   export ANTHROPIC_API_KEY='your-api-key-here'")
        print("3. Run this script again")
        return
    
    # Import and use the main functionality
    try:
        from main import summarize_text, get_api_key
        
        api_key = get_api_key()
        
        print(f"\n📊 Original text ({len(demo_text)} characters):")
        print("-" * 50)
        print(demo_text[:200] + "...")
        print("-" * 50)
        
        print("\n🤖 Summarizing with Claude...")
        summary = summarize_text(demo_text, api_key)
        
        print("\n✨ Summary:")
        print("=" * 50)
        print(summary)
        print("=" * 50)
        print(f"📈 Summary length: {len(summary)} characters")
        print(f"📉 Compression ratio: {len(summary)/len(demo_text)*100:.1f}%")
        
        print("\n🎉 Demo completed successfully!")
        print("\n💡 Try your own text:")
        print("   python main.py \"Your text here\"")
        
    except ImportError:
        print("❌ Could not import main module!")
        print("💡 Make sure you're running this from the project directory")
    except Exception as e:
        print(f"❌ Demo failed: {e}")
        print("💡 Check your API key and internet connection")

if __name__ == "__main__":
    run_demo() 