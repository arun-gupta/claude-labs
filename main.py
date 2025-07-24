#!/usr/bin/env python3
"""
Claude Labs - Comprehensive Claude API Showcase

A comprehensive demonstration of Claude's capabilities including text summarization, chat, and document processing.
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

# Rich terminal output imports
from rich.console import Console
from rich.panel import Panel
from rich.progress import Progress, SpinnerColumn, TextColumn, BarColumn, TimeElapsedColumn
from rich.text import Text
from rich.prompt import Prompt, Confirm
from rich.table import Table
from rich.syntax import Syntax
from rich import print as rprint

# Monitoring imports
from monitoring import monitor, error_tracker, monitor_request

# Initialize rich console
console = Console()


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
        # Create a beautiful error panel
        error_content = """
[bold red]❌ API Key Not Found![/bold red]

[bold blue]🔧 Quick Setup:[/bold blue]
1. Visit [link=https://console.anthropic.com/]https://console.anthropic.com/[/link]
2. Create an account and get your API key
3. Set it as an environment variable:

[bold green]On macOS/Linux:[/bold green]
   export ANTHROPIC_API_KEY='your-api-key-here'

[bold green]On Windows:[/bold green]
   set ANTHROPIC_API_KEY=your-api-key-here

[bold yellow]💡 Pro tip:[/bold yellow] Add this to your ~/.bashrc or ~/.zshrc for persistence
        """
        
        console.print(Panel(
            error_content,
            title="[bold red]Setup Required[/bold red]",
            border_style="red",
            padding=(1, 2)
        ))
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
            console.print(Panel(
                f"[bold red]❌ File Not Found![/bold red]\n\n"
                f"Could not find: [bold yellow]{file_path}[/bold yellow]\n\n"
                f"[bold blue]💡 Check:[/bold blue]\n"
                f"• File path is correct\n"
                f"• File exists in current directory\n"
                f"• Use absolute path if needed",
                title="[bold red]File Error[/bold red]",
                border_style="red"
            ))
            sys.exit(1)
        
        content = path.read_text(encoding='utf-8')
        if not content.strip():
            console.print(Panel(
                f"[bold red]❌ Empty File![/bold red]\n\n"
                f"File [bold yellow]{file_path}[/bold yellow] is empty.\n\n"
                f"[bold blue]💡 Add some content to the file and try again.[/bold blue]",
                title="[bold red]File Error[/bold red]",
                border_style="red"
            ))
            sys.exit(1)
            
        return content
    except UnicodeDecodeError:
        console.print(Panel(
            f"[bold red]❌ Encoding Error![/bold red]\n\n"
            f"Could not read [bold yellow]{file_path}[/bold yellow] due to encoding issues.\n\n"
            f"[bold blue]💡 Solution:[/bold blue] Save the file as UTF-8 encoding.",
            title="[bold red]Encoding Error[/bold red]",
            border_style="red"
        ))
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
        # Validate URL format first
        parsed_url = urlparse(url)
        if not parsed_url.scheme or not parsed_url.netloc:
            console.print(Panel(
                "[bold red]❌ Invalid URL Format![/bold red]\n\n"
                "[bold blue]💡 Please provide a valid URL:[/bold blue]\n"
                "• https://example.com\n"
                "• http://example.com\n"
                "• https://www.example.com/path",
                title="[bold red]URL Error[/bold red]",
                border_style="red"
            ))
            sys.exit(1)
        
        # Show fetching progress
        with Progress(
            SpinnerColumn(),
            TextColumn("[progress.description]{task.description}"),
            console=console
        ) as progress:
            task = progress.add_task(f"[cyan]🌐 Fetching content from: {url}", total=None)
            
            # Fetch content with timeout and user agent
            headers = {
                'User-Agent': 'Claude-Labs/1.0 (https://github.com/arun-gupta/claude-labs)'
            }
            
            response = requests.get(url, headers=headers, timeout=30)
            response.raise_for_status()
            
            # Try to extract text content
            content = response.text
            
            progress.update(task, description=f"[green]✅ Fetched {len(content)} characters")
        
        # Basic content validation
        if not content.strip():
            console.print(Panel(
                "[bold red]❌ No Content Found![/bold red]\n\n"
                f"The URL [bold yellow]{url}[/bold yellow] returned no readable content.\n\n"
                "[bold blue]💡 Try:[/bold blue]\n"
                "• A different URL\n"
                "• Check if the page requires JavaScript\n"
                "• Verify the URL is accessible",
                title="[bold red]Content Error[/bold red]",
                border_style="red"
            ))
            sys.exit(1)
        
        # Limit content size to prevent excessive API usage
        if len(content) > 50000:  # 50KB limit
            console.print(Panel(
                "[bold yellow]⚠️  Large Content Warning[/bold yellow]\n\n"
                f"Content is {len(content):,} characters (50KB limit).\n"
                "Truncating to first 50KB for API efficiency.\n\n"
                "[bold blue]💡 For full content, save to file first.[/bold blue]",
                title="[bold yellow]Size Warning[/bold yellow]",
                border_style="yellow"
            ))
            content = content[:50000]
        
        return content
        
    except requests.exceptions.RequestException as e:
        console.print(Panel(
            f"[bold red]❌ Network Error![/bold red]\n\n"
            f"Failed to fetch [bold yellow]{url}[/bold yellow]\n\n"
            f"[bold blue]Error:[/bold blue] {str(e)}\n\n"
            f"[bold blue]💡 Check:[/bold blue]\n"
            f"• Internet connection\n"
            f"• URL accessibility\n"
            f"• Firewall settings",
            title="[bold red]Network Error[/bold red]",
            border_style="red"
        ))
        sys.exit(1)
    except Exception as e:
        console.print(Panel(
            f"[bold red]❌ Unexpected Error![/bold red]\n\n"
            f"An unexpected error occurred while fetching [bold yellow]{url}[/bold yellow]\n\n"
            f"[bold blue]Error:[/bold blue] {str(e)}",
            title="[bold red]Unexpected Error[/bold red]",
            border_style="red"
        ))
        sys.exit(1)


@monitor_request
def summarize_text(text: str, api_key: str, model: str = "claude-3-5-haiku-20241022") -> str:
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
        
        # Show summarization progress
        with Progress(
            SpinnerColumn(),
            TextColumn("[progress.description]{task.description}"),
            console=console
        ) as progress:
            task = progress.add_task("[cyan]🤖 Claude is analyzing your text...", total=None)
            
            # Claude prompt for summarization
            prompt = f"""Please provide a clear, concise summary of the following text. 
Focus on the key points and main ideas while maintaining accuracy.

Text to summarize:
{text}

Summary:"""
            
            response = client.messages.create(
                model=model,
                max_tokens=1000,
                temperature=0.3,  # Lower temperature for more focused summaries
                messages=[{"role": "user", "content": prompt}]
            )
            
            progress.update(task, description="[green]✅ Summary complete!")
        
        return response.content[0].text.strip()
        
    except anthropic.AuthenticationError:
        console.print(Panel(
            "[bold red]❌ Invalid API Key![/bold red]\n\n"
            "Your ANTHROPIC_API_KEY appears to be invalid.\n\n"
            "[bold blue]💡 Solutions:[/bold blue]\n"
            "• Check your API key at [link=https://console.anthropic.com/]https://console.anthropic.com/[/link]\n"
            "• Ensure you have credits in your account\n"
            "• Verify the key is set correctly",
            title="[bold red]Authentication Error[/bold red]",
            border_style="red"
        ))
        sys.exit(1)
    except anthropic.RateLimitError:
        console.print(Panel(
            "[bold red]❌ Rate Limit Exceeded![/bold red]\n\n"
            "You've hit Claude's rate limit. Please wait a moment.\n\n"
            "[bold blue]💡 Try again in a few seconds.[/bold blue]",
            title="[bold red]Rate Limit Error[/bold red]",
            border_style="red"
        ))
        sys.exit(1)
    except anthropic.APIError as e:
        console.print(Panel(
            f"[bold red]❌ API Error![/bold red]\n\n"
            f"Claude API returned an error: [bold yellow]{str(e)}[/bold yellow]\n\n"
            f"[bold blue]💡 Check:[/bold blue]\n"
            f"• Internet connection\n"
            f"• API service status\n"
            f"• Try again in a moment",
            title="[bold red]API Error[/bold red]",
            border_style="red"
        ))
        sys.exit(1)
    except Exception as e:
        console.print(Panel(
            f"[bold red]❌ Unexpected Error![/bold red]\n\n"
            f"An unexpected error occurred: [bold yellow]{str(e)}[/bold yellow]\n\n"
            f"[bold blue]💡 Try:[/bold blue]\n"
            f"• Check the documentation\n"
            f"• Restart the application\n"
            f"• Contact support if the issue persists",
            title="[bold red]Unexpected Error[/bold red]",
            border_style="red"
        ))
        sys.exit(1)


def main():
    """Main function with argument parsing and user-friendly output."""
    parser = argparse.ArgumentParser(
        description="Claude Labs - Comprehensive Claude API Showcase",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python main.py --url https://www.anthropic.com/news/introducing-claude
  python main.py --file document.txt
  python main.py "This is a long text that needs to be summarized..."
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
    parser.add_argument(
        '--analytics', '-a',
        action='store_true',
        help='Display usage analytics and monitoring data'
    )
    parser.add_argument(
        '--export-analytics',
        help='Export analytics to JSON file'
    )
    
    args = parser.parse_args()
    
    # Handle analytics-only mode
    if args.analytics:
        monitor.display_analytics()
        sys.exit(0)
    
    if args.export_analytics:
        monitor.export_analytics(args.export_analytics)
        sys.exit(0)
    
    # Get input text
    if args.url:
        text = read_url_content(args.url)
    elif args.file:
        text = read_file_content(args.file)
        console.print(f"[cyan]📄 Reading from file: {args.file}[/cyan]")
    elif args.text:
        text = args.text
    else:
        # Read from stdin if no arguments provided
        console.print("[cyan]📝 Enter text to summarize (Ctrl+D when done):[/cyan]")
        text = sys.stdin.read().strip()
        if not text:
            console.print(Panel(
                "[bold red]❌ No text provided![/bold red]\n\n"
                "Please provide text to summarize.\n\n"
                "[bold blue]💡 Usage examples:[/bold blue]\n"
                "• python main.py \"Your text here\"\n"
                "• python main.py --file document.txt\n"
                "• python main.py --url https://example.com",
                title="[bold red]Input Error[/bold red]",
                border_style="red"
            ))
            parser.print_help()
            sys.exit(1)
    
    # Validate input
    if len(text) < 10:
        console.print(Panel(
            "[bold red]❌ Text Too Short![/bold red]\n\n"
            f"Provided text is only {len(text)} characters.\n\n"
            "[bold blue]💡 Please provide at least 10 characters for meaningful summarization.[/bold blue]",
            title="[bold red]Input Error[/bold red]",
            border_style="red"
        ))
        sys.exit(1)
    
    # Display original text in a beautiful panel
    preview_text = text[:200] + ("..." if len(text) > 200 else "")
    console.print(Panel(
        f"[bold blue]📊 Original Text ({len(text):,} characters)[/bold blue]\n\n"
        f"[dim]{preview_text}[/dim]",
        title="[bold blue]Input[/bold blue]",
        border_style="blue"
    ))
    
    # Get API key and summarize
    api_key = get_api_key()
    
    try:
        summary = summarize_text(text, api_key)
        
        # Calculate metrics
        compression_ratio = len(summary) / len(text) * 100
        
        # Display summary in a beautiful panel
        console.print(Panel(
            f"[bold green]✨ Summary ({len(summary):,} characters)[/bold green]\n\n"
            f"{summary}\n\n"
            f"[dim]📈 Summary length: {len(summary):,} characters\n"
            f"📉 Compression ratio: {compression_ratio:.1f}%[/dim]",
            title="[bold green]Claude's Summary[/bold green]",
            border_style="green"
        ))
        
        # Show compression stats in a table
        table = Table(title="📊 Summary Statistics")
        table.add_column("Metric", style="cyan", no_wrap=True)
        table.add_column("Value", style="magenta")
        
        table.add_row("Original Length", f"{len(text):,} characters")
        table.add_row("Summary Length", f"{len(summary):,} characters")
        table.add_row("Compression Ratio", f"{compression_ratio:.1f}%")
        table.add_row("Characters Saved", f"{len(text) - len(summary):,}")
        
        console.print(table)
        
        # Show analytics if requested
        if monitor.get_analytics().total_requests > 1:
            console.print("\n[dim]💡 Run with --analytics to see detailed usage statistics[/dim]")
        
    except KeyboardInterrupt:
        console.print(Panel(
            "[bold yellow]⏹️  Operation cancelled by user[/bold yellow]",
            title="[bold yellow]Cancelled[/bold yellow]",
            border_style="yellow"
        ))
        sys.exit(0)


if __name__ == "__main__":
    main() 