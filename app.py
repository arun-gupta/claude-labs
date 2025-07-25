
import streamlit as st
import anthropic
import requests
import os
from typing import Optional
import time
from datetime import datetime
import monitoring
import pathlib
import toml

# Remove theme-related code - not working reliably
LOG_PATH = pathlib.Path("claude_labs.log")

def tail_log(path, n=100):
    if not path.exists():
        return ["Log file not found."]
    with open(path, "r") as f:
        lines = f.readlines()
    return lines[-n:] if len(lines) > n else lines

# Page configuration
st.set_page_config(
    page_title="Claude Labs",
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
            # --- Monitoring integration ---
            input_tokens = getattr(getattr(response, 'usage', None), 'input_tokens', 0)
            output_tokens = getattr(getattr(response, 'usage', None), 'output_tokens', 0)
            monitoring.monitor.log_response(
                request_id=f"web_{int(time.time() * 1000)}",
                response=response,
                end_time=time.time(),
                input_tokens=input_tokens,
                output_tokens=output_tokens,
                model=model,
                success=True
            )
            # --- End monitoring ---
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
            # --- Monitoring integration ---
            input_tokens = getattr(getattr(response, 'usage', None), 'input_tokens', 0)
            output_tokens = getattr(getattr(response, 'usage', None), 'output_tokens', 0)
            monitoring.monitor.log_response(
                request_id=f"web_{int(time.time() * 1000)}",
                response=response,
                end_time=time.time(),
                input_tokens=input_tokens,
                output_tokens=output_tokens,
                model=model,
                success=True
            )
            # --- End monitoring ---
            return response.content[0].text
    except Exception as e:
        st.error(f"❌ Error calling Claude API: {str(e)}")
        return None

def format_cost(cost):
    if cost == 0:
        return "$0.00"
    elif abs(cost) < 0.000001:
        return f"${cost:.2e}"
    else:
        return f"${cost:.8f}".rstrip('0').rstrip('.')

# Main header
st.markdown('<h1 class="main-header">🤖 Claude Labs</h1>', unsafe_allow_html=True)
st.markdown("### Comprehensive Claude API showcase with interactive interface")

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
            label_visibility="collapsed",
            key="chat_input"
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
    
    # Usability tip for chat
    if st.session_state.chat_history:
        st.info("💡 **Tip:** Click in the chat box below to continue the conversation!")

# Tab 2: File Upload
with tab2:
    st.header("📄 File Upload & Summarization")
    st.markdown("Upload a text file and let Claude summarize it for you.")
    
    # Demo file download
    col1, col2 = st.columns([1, 3])
    with col1:
        demo_file_content = """Artificial Intelligence and Machine Learning: A Comprehensive Overview

Artificial Intelligence (AI) and Machine Learning (ML) have emerged as transformative technologies that are reshaping industries, economies, and societies worldwide. These technologies represent the culmination of decades of research in computer science, mathematics, and cognitive science, bringing us closer to creating systems that can perform tasks traditionally requiring human intelligence.

Machine Learning, a subset of AI, focuses on developing algorithms and statistical models that enable computers to improve their performance on specific tasks through experience. Unlike traditional programming, where explicit instructions are coded, ML systems learn patterns from data and make predictions or decisions based on that learning. This approach has proven particularly effective in areas such as image recognition, natural language processing, recommendation systems, and autonomous vehicles.

The field has seen remarkable progress in recent years, driven by several key factors: the availability of massive datasets, increased computational power, and breakthroughs in neural network architectures. Deep Learning, a specialized form of ML using artificial neural networks with multiple layers, has been particularly influential, achieving state-of-the-art results in numerous domains.

However, the rapid advancement of AI/ML also presents significant challenges and considerations. Issues of bias in training data, privacy concerns, job displacement, and the need for explainable AI systems are among the critical topics that researchers, policymakers, and industry leaders must address. Ensuring that these technologies are developed and deployed responsibly, with appropriate safeguards and ethical considerations, is essential for maximizing their benefits while minimizing potential harms.

Looking forward, AI and ML are expected to continue their rapid evolution, with applications spanning healthcare, education, transportation, finance, and beyond. The key to successful implementation lies in thoughtful design, robust testing, and ongoing collaboration between technologists, domain experts, and stakeholders to ensure these powerful tools serve humanity's best interests."""
        
        st.download_button(
            label="📄 Download Demo File",
            data=demo_file_content,
            file_name="ai-ml-overview.txt",
            mime="text/plain",
            type="secondary"
        )
    
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
    
    # Demo button to auto-fill the default URL
    col1, col2 = st.columns([1, 3])
    with col1:
        if st.button("🎯 Try Demo URL", type="secondary"):
            st.session_state.demo_url = "https://www.anthropic.com/news/introducing-claude"
    
    url = st.text_input(
        "Enter URL:",
        value=st.session_state.get("demo_url", ""),
        placeholder="https://www.anthropic.com/news/introducing-claude",
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
        analytics_tabs = st.tabs(["Usage", "Cost", "API Status", "Model Info", "Log"])

        with analytics_tabs[0]:
            st.subheader("📈 Usage Statistics")
            analytics = monitoring.monitor.get_analytics()
            st.metric("Total Tokens Used", f"{analytics.total_tokens:,}")
            if st.session_state.chat_history:
                st.metric("Total Conversations", len(st.session_state.chat_history))
                st.metric("Latest Chat", st.session_state.chat_history[-1]["timestamp"].strftime("%Y-%m-%d %H:%M:%S"))
            else:
                st.info("No conversations yet. Start chatting to see statistics!")

        with analytics_tabs[1]:
            st.subheader("💸 Cost Metrics")
            analytics = monitoring.monitor.get_analytics()
            st.metric("Total Cost (USD)", format_cost(analytics.total_cost_usd))
            avg_cost = analytics.total_cost_usd / analytics.total_requests if analytics.total_requests > 0 else 0
            st.metric("Avg Cost per Conversation", format_cost(avg_cost))
            if analytics.requests_by_model:
                st.markdown("**Cost by Model:**")
                for model, count in analytics.requests_by_model.items():
                    st.write(f"{model}: {count} requests")

        with analytics_tabs[2]:
            st.subheader("🔑 API Status")
            api_key = get_api_key()
            if api_key:
                st.success("✅ API key is configured")
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

        with analytics_tabs[3]:
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

        with analytics_tabs[4]:
            st.subheader("📜 Request/Response Log")
            num_log_lines = st.number_input(
                "Number of log lines to display",
                min_value=10,
                max_value=1000,
                value=100,
                step=10
            )
            log_lines = tail_log(LOG_PATH, n=num_log_lines)
            st.code("".join(log_lines), language="text")

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: #666;'>
    <p>🤖 Claude Labs - Built with Streamlit and Claude API</p>
    <p>Get your API key from <a href='https://console.anthropic.com/' target='_blank'>Anthropic Console</a></p>
</div>
""", unsafe_allow_html=True) 