#!/usr/bin/env python3
"""
Claude Labs - Analytics Dashboard

Priority 3: Standalone analytics dashboard for monitoring Claude API usage.
Run this script to view detailed analytics and monitoring data.
"""

import sys
from monitoring import monitor, error_tracker
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.text import Text
from rich import print as rprint

console = Console()

def main():
    """Display comprehensive analytics dashboard"""
    
    analytics = monitor.get_analytics()
    
    # Main dashboard header
    console.print(Panel(
        "[bold blue]📊 Claude Labs Analytics Dashboard[/bold blue]\n"
        "[dim]Priority 3: Production Monitoring & Debugging[/dim]",
        title="🤖 Claude Labs",
        border_style="blue"
    ))
    
    # Display analytics
    monitor.display_analytics()
    
    # Additional insights
    if analytics.total_requests > 0:
        console.print("\n")
        
        # Performance insights
        insights_table = Table(title="💡 Performance Insights", show_header=True, header_style="bold green")
        insights_table.add_column("Metric", style="cyan")
        insights_table.add_column("Value", style="yellow")
        insights_table.add_column("Status", style="green")
        
        # Success rate
        success_rate = (analytics.successful_requests / analytics.total_requests * 100) if analytics.total_requests > 0 else 0
        success_status = "✅ Excellent" if success_rate >= 95 else "⚠️ Good" if success_rate >= 80 else "❌ Needs Attention"
        insights_table.add_row("Success Rate", f"{success_rate:.1f}%", success_status)
        
        # Average response time
        response_status = "⚡ Fast" if analytics.avg_response_time < 2 else "🐌 Slow" if analytics.avg_response_time > 5 else "⏱️ Normal"
        insights_table.add_row("Avg Response Time", f"{analytics.avg_response_time:.2f}s", response_status)
        
        # Cost efficiency
        cost_per_request = analytics.total_cost_usd / analytics.total_requests if analytics.total_requests > 0 else 0
        cost_status = "💰 Low" if cost_per_request < 0.01 else "💸 High" if cost_per_request > 0.05 else "💵 Normal"
        insights_table.add_row("Cost per Request", f"${cost_per_request:.4f}", cost_status)
        
        console.print(insights_table)
        
        # Recommendations
        if analytics.failed_requests > 0:
            console.print(Panel(
                "[bold yellow]⚠️ Recommendations:[/bold yellow]\n\n"
                "• Check error logs for failed requests\n"
                "• Monitor rate limiting and API quotas\n"
                "• Consider using Haiku model for faster responses\n"
                "• Review API key permissions and credits",
                title="🔧 Suggestions",
                border_style="yellow"
            ))
        
        # Export option
        console.print(Panel(
            "[bold blue]📤 Export Options:[/bold blue]\n\n"
            "• python analytics.py --export claude_analytics.json\n"
            "• python main.py --export-analytics claude_analytics.json\n"
            "• Check claude_labs.log for detailed logs",
            title="💾 Data Export",
            border_style="blue"
        ))
    
    else:
        console.print(Panel(
            "[bold yellow]📊 No Data Available[/bold yellow]\n\n"
            "No requests have been made yet.\n\n"
            "[bold blue]💡 To generate analytics:[/bold blue]\n"
            "• Run: python main.py \"Your text to summarize\"\n"
            "• Or: python main.py --file document.txt\n"
            "• Or: python main.py --url https://example.com",
            title="🚀 Get Started",
            border_style="yellow"
        ))

if __name__ == "__main__":
    main() 