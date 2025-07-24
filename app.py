import streamlit as st
import anthropic
import requests
import os
from typing import Optional
import time
from datetime import datetime

# Page configuration
st.set_page_config(
    page_title="Hello Claude Demo",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better styling
st.markdown("""
<style>
    .main-header {
        font-size: 3rem;
        font-weight: bold;
        text-align: center;
        margin-bottom: 2rem;
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }
    .feature-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 1.5rem;
        border-radius: 10px;
        color: white;
        margin: 1rem 0;
    }
    .success-box {
        background-color: #d4edda;
        border: 1px solid #c3e6cb;
        border-radius: 5px;
        padding: 1rem;
        margin: 1rem 0;
    }
    .error-box {
        background-color: #f8d7da;
        border: 1px solid #f5c6cb;
        border-radius: 5px;
        padding: 1rem;
        margin: 1rem 0;
    }
    .info-box {
        background-color: #d1ecf1;
        border: 1px solid #bee5eb;
        border-radius: 5px;
        padding: 1rem;
        margin: 1rem 0;
    }
</style>
""", unsafe_allow_html=True)

# Initialize session state
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []
if 'api_key' not in st.session_state:
    st.session_state.api_key = None


def get_api_key() -> Optional[str]:
    """Get API key from environment or session state"""
    api_key = os.getenv('ANTHROPIC_API_KEY') or st.session_state.api_key
    return api_key

def initialize_client():
    """Initialize Anthropic client"""
    api_key = get_api_key()
    if not api_key:
        st.error("❌ ANTHROPIC_API_KEY not found! Please set it in the sidebar.")
        return None
    return anthropic.Anthropic(api_key=api_key)

def fetch_url_content(url: str) -> Optional[str]:
    """Fetch content from URL"""
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        return response.text
    except Exception as e:
        st.error(f"❌ Error fetching URL: {str(e)}")
        return None

def summarize_text(text: str, client: anthropic.Anthropic, model: str = "claude-3-5-haiku-20241022") -> Optional[str]:
    """Summarize text using Claude"""
    try:
        with st.spinner("🤖 Claude is thinking..."):
            response = client.messages.create(
                model=model,
                max_tokens=1000,
                messages=[
                    {
                        "role": "user",
                        "content": f"Please provide a concise summary of the following text:\n\n{text}"
                    }
                ]
            )
            return response.content[0].text
    except Exception as e:
        st.error(f"❌ Error calling Claude API: {str(e)}")
        return None

def chat_with_claude(message: str, client: anthropic.Anthropic, model: str = "claude-3-5-haiku-20241022") -> Optional[str]:
    """Chat with Claude"""
    try:
        with st.spinner("🤖 Claude is responding..."):
            response = client.messages.create(
                model=model,
                max_tokens=1000,
                messages=[
                    {
                        "role": "user",
                        "content": message
                    }
                ]
            )
            return response.content[0].text
    except Exception as e:
        st.error(f"❌ Error calling Claude API: {str(e)}")
        return None

# Main header
st.markdown('<h1 class="main-header">🤖 Hello Claude Demo</h1>', unsafe_allow_html=True)
st.markdown("### Lightning-fast AI interactions with Claude API")

# Sidebar for configuration
with st.sidebar:
    st.header("⚙️ Configuration")
    
    # API Key setup
    api_key = st.text_input(
        "🔑 ANTHROPIC_API_KEY",
        type="password",
        help="Get your API key from https://console.anthropic.com/"
    )
    
    if api_key:
        st.session_state.api_key = api_key
        st.success("✅ API key set!")
    
    # Model selection
    st.subheader("🤖 Model Selection")
    model = st.selectbox(
        "Choose Claude model:",
        [
            "claude-3-5-haiku-20241022",
            "claude-3-5-sonnet-20241022",
            "claude-3-opus-20240229"
        ],
        help="Haiku: Fast & Cheap (Recommended), Sonnet: Balanced, Opus: Most Capable"
    )
    
    # Features info
    st.subheader("✨ Features")
    st.markdown("""
    - 💬 **Chat Interface** - Talk with Claude
    - 📄 **File Upload** - Summarize documents
    - 🌐 **URL Processing** - Fetch & summarize web content
    - 📊 **Real-time Streaming** - See Claude think
    - 🎨 **Rich Output** - Beautiful formatting
    """)
    
    # Quick start
    st.subheader("🚀 Quick Start")
    st.markdown("""
    1. Set your API key above
    2. Choose a model
    3. Start chatting or uploading files!
    """)

# Main content area
tab1, tab2, tab3, tab4 = st.tabs(["💬 Chat", "📄 File Upload", "🌐 URL Processing", "📊 Analytics"])

# Tab 1: Chat Interface
with tab1:
    st.header("💬 Chat with Claude")
    st.markdown("Have a conversation with Claude! Ask questions, get help, or just chat.")
    
    # Display chat messages in real-time
    if st.session_state.chat_history:
        st.subheader("💭 Conversation")
        
        # Create a chat-like display
        for i, chat in enumerate(st.session_state.chat_history):
            # User message
            with st.chat_message("user"):
                st.write(chat["user"])
            
            # Assistant message
            with st.chat_message("assistant"):
                st.write(chat["assistant"])
        
        # Clear chat button
        if st.button("🗑️ Clear Chat"):
            st.session_state.chat_history = []
            st.rerun()
    
    # Chat input with form for auto-clear
    with st.form("chat_form", clear_on_submit=True):
        user_message = st.text_input(
            "Your message:",
            placeholder="Ask Claude anything... (Press Enter to send)",
            label_visibility="collapsed"
        )
        
        # Subtle submit button (Enter key will trigger this)
        col1, col2, col3 = st.columns([1, 0.1, 1])
        with col2:
            submitted = st.form_submit_button("→", type="secondary", use_container_width=False)
        
        # Handle form submission (Enter key or button click)
        if submitted and user_message.strip():
            client = initialize_client()
            if client:
                response = chat_with_claude(user_message, client, model)
                if response:
                    # Add to chat history
                    st.session_state.chat_history.append({
                        "user": user_message,
                        "assistant": response,
                        "timestamp": datetime.now()
                    })
                    st.rerun()

# Tab 2: File Upload
with tab2:
    st.header("📄 File Upload & Summarization")
    st.markdown("Upload a text file and let Claude summarize it for you.")
    
    uploaded_file = st.file_uploader(
        "Choose a text file:",
        type=['txt', 'md', 'py', 'js', 'html', 'css', 'json', 'csv'],
        help="Upload any text-based file for summarization"
    )
    
    if uploaded_file is not None:
        # Display file info
        file_details = {
            "Filename": uploaded_file.name,
            "File size": f"{uploaded_file.size} bytes",
            "File type": uploaded_file.type
        }
        st.json(file_details)
        
        # Read file content
        try:
            content = uploaded_file.read().decode('utf-8')
            st.subheader("📖 File Content Preview")
            st.text_area("Content:", content, height=200, disabled=True)
            
            if st.button("🤖 Summarize with Claude", type="primary"):
                client = initialize_client()
                if client:
                    # Show original stats
                    col1, col2, col3 = st.columns(3)
                    with col1:
                        st.metric("Original Length", f"{len(content)} characters")
                    with col2:
                        st.metric("Original Words", f"{len(content.split())} words")
                    with col3:
                        st.metric("File Size", f"{uploaded_file.size} bytes")
                    
                    # Get summary
                    summary = summarize_text(content, client, model)
                    if summary:
                        st.subheader("✨ Claude's Summary")
                        st.markdown(summary)
                        
                        # Show summary stats
                        col1, col2, col3 = st.columns(3)
                        with col1:
                            st.metric("Summary Length", f"{len(summary)} characters")
                        with col2:
                            st.metric("Summary Words", f"{len(summary.split())} words")
                        with col3:
                            compression = (1 - len(summary) / len(content)) * 100
                            st.metric("Compression", f"{compression:.1f}%")
        
        except Exception as e:
            st.error(f"❌ Error reading file: {str(e)}")

# Tab 3: URL Processing
with tab3:
    st.header("🌐 URL Processing")
    st.markdown("Enter a URL and let Claude fetch and summarize the content.")
    
    url = st.text_input(
        "Enter URL:",
        placeholder="https://example.com/article",
        help="Enter any web URL to fetch and summarize"
    )
    
    if url:
        if st.button("🌐 Fetch & Summarize", type="primary"):
            client = initialize_client()
            if client:
                # Fetch content
                with st.spinner("🌐 Fetching content from URL..."):
                    content = fetch_url_content(url)
                
                if content:
                    # Show original stats
                    col1, col2 = st.columns(2)
                    with col1:
                        st.metric("Content Length", f"{len(content)} characters")
                    with col2:
                        st.metric("Content Words", f"{len(content.split())} words")
                    
                    # Show content preview
                    st.subheader("📖 Content Preview")
                    preview = content[:1000] + "..." if len(content) > 1000 else content
                    st.text_area("Content:", preview, height=200, disabled=True)
                    
                    # Get summary
                    summary = summarize_text(content, client, model)
                    if summary:
                        st.subheader("✨ Claude's Summary")
                        st.markdown(summary)
                        
                        # Show summary stats
                        col1, col2, col3 = st.columns(3)
                        with col1:
                            st.metric("Summary Length", f"{len(summary)} characters")
                        with col2:
                            st.metric("Summary Words", f"{len(summary.split())} words")
                        with col3:
                            compression = (1 - len(summary) / len(content)) * 100
                            st.metric("Compression", f"{compression:.1f}%")

# Tab 4: Analytics
with tab4:
    st.header("📊 Analytics & Information")
    
    # API Status
    st.subheader("🔑 API Status")
    api_key = get_api_key()
    if api_key:
        st.success("✅ API key is configured")
        
        # Test API connection
        if st.button("🧪 Test API Connection"):
            client = initialize_client()
            if client:
                try:
                    with st.spinner("Testing API connection..."):
                        response = client.messages.create(
                            model=model,
                            max_tokens=50,
                            messages=[{"role": "user", "content": "Hello!"}]
                        )
                    st.success("✅ API connection successful!")
                    st.info(f"Response: {response.content[0].text}")
                except Exception as e:
                    st.error(f"❌ API connection failed: {str(e)}")
    else:
        st.error("❌ API key not configured")
    
    # Model Information
    st.subheader("🤖 Model Information")
    model_info = {
        "claude-3-5-sonnet-20241022": {
            "description": "Balanced performance and cost",
            "best_for": "General use, conversations, analysis",
            "speed": "Fast",
            "cost": "Medium"
        },
        "claude-3-5-haiku-20241022": {
            "description": "Fastest and most cost-effective",
            "best_for": "Quick tasks, simple queries",
            "speed": "Very Fast",
            "cost": "Low"
        },
        "claude-3-opus-20240229": {
            "description": "Most capable model",
            "best_for": "Complex reasoning, creative tasks",
            "speed": "Slower",
            "cost": "High"
        }
    }
    
    selected_model_info = model_info.get(model, {})
    if selected_model_info:
        st.json(selected_model_info)
    
    # Usage Statistics
    st.subheader("📈 Usage Statistics")
    if st.session_state.chat_history:
        st.metric("Total Conversations", len(st.session_state.chat_history))
        st.metric("Latest Chat", st.session_state.chat_history[-1]["timestamp"].strftime("%Y-%m-%d %H:%M:%S"))
    else:
        st.info("No conversations yet. Start chatting to see statistics!")

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: #666;'>
    <p>🤖 Hello Claude Demo - Built with Streamlit and Claude API</p>
    <p>Get your API key from <a href='https://console.anthropic.com/' target='_blank'>Anthropic Console</a></p>
</div>
""", unsafe_allow_html=True) 