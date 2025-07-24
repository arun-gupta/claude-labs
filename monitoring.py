#!/usr/bin/env python3
"""
Claude Labs - Monitoring & Debugging Module

Priority 3: Production readiness and monitoring features including:
- Request/response logging with timestamps
- Performance metrics (token usage, response time, cost tracking)
- Error tracking with detailed stack traces
- Rate limiting and intelligent retry logic
- Usage analytics dashboard
"""

import json
import logging
import time
import traceback
from datetime import datetime, timedelta
from pathlib import Path
from typing import Any, Dict, List, Optional, Union
from dataclasses import dataclass, asdict
from collections import defaultdict, deque
import threading
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.progress import Progress, SpinnerColumn, TextColumn
from rich.text import Text

console = Console()

@dataclass
class RequestMetrics:
    """Metrics for a single API request"""
    timestamp: datetime
    model: str
    input_tokens: int
    output_tokens: int
    response_time: float
    cost_usd: float
    success: bool
    error_type: Optional[str] = None
    error_message: Optional[str] = None
    retry_count: int = 0

@dataclass
class UsageAnalytics:
    """Aggregated usage analytics"""
    total_requests: int
    successful_requests: int
    failed_requests: int
    total_tokens: int
    total_cost_usd: float
    avg_response_time: float
    requests_by_model: Dict[str, int]
    errors_by_type: Dict[str, int]
    hourly_usage: Dict[int, int]  # Hour -> request count

class ClaudeMonitor:
    """Comprehensive monitoring for Claude API usage"""
    
    def __init__(self, log_file: str = "claude_labs.log", max_history: int = 1000):
        self.log_file = Path(log_file)
        self.max_history = max_history
        self.request_history: deque = deque(maxlen=max_history)
        self.analytics = UsageAnalytics(
            total_requests=0,
            successful_requests=0,
            failed_requests=0,
            total_tokens=0,
            total_cost_usd=0.0,
            avg_response_time=0.0,
            requests_by_model=defaultdict(int),
            errors_by_type=defaultdict(int),
            hourly_usage=defaultdict(int)
        )
        self.rate_limiter = RateLimiter()
        self._lock = threading.Lock()
        
        # Setup logging
        self._setup_logging()
    
    def _setup_logging(self):
        """Configure detailed logging"""
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s',
            handlers=[
                logging.FileHandler(self.log_file),
                logging.StreamHandler()
            ]
        )
        self.logger = logging.getLogger(__name__)
    
    def log_request(self, model: str, input_text: str, start_time: float) -> str:
        """Log the start of a request"""
        request_id = f"req_{int(time.time() * 1000)}"
        self.logger.info(f"Request {request_id} started - Model: {model}, Input length: {len(input_text)} chars")
        return request_id
    
    def log_response(self, request_id: str, response: Any, end_time: float, 
                    input_tokens: int, output_tokens: int, model: str, 
                    success: bool = True, error: Optional[Exception] = None) -> RequestMetrics:
        """Log the completion of a request with metrics"""
        response_time = end_time - time.time()
        
        # Calculate cost (approximate based on Claude pricing)
        cost = self._calculate_cost(input_tokens, output_tokens, model)
        
        # Create metrics
        metrics = RequestMetrics(
            timestamp=datetime.now(),
            model=model,
            input_tokens=input_tokens,
            output_tokens=output_tokens,
            response_time=response_time,
            cost_usd=cost,
            success=success,
            error_type=type(error).__name__ if error else None,
            error_message=str(error) if error else None
        )
        
        # Update analytics
        with self._lock:
            self._update_analytics(metrics)
            self.request_history.append(metrics)
        
        # Log details
        if success:
            self.logger.info(
                f"Request {request_id} completed - "
                f"Time: {response_time:.2f}s, "
                f"Tokens: {input_tokens}+{output_tokens}, "
                f"Cost: ${cost:.4f}"
            )
        else:
            self.logger.error(
                f"Request {request_id} failed - "
                f"Error: {type(error).__name__}: {error}, "
                f"Time: {response_time:.2f}s"
            )
        
        return metrics
    
    def _calculate_cost(self, input_tokens: int, output_tokens: int, model: str) -> float:
        """Calculate approximate cost based on Claude pricing"""
        # Claude 3.5 Sonnet pricing (approximate)
        pricing = {
            "claude-3-5-sonnet-20241022": {"input": 0.003, "output": 0.015},
            "claude-3-5-haiku-20241022": {"input": 0.00025, "output": 0.00125},
            "claude-3-opus-20240229": {"input": 0.015, "output": 0.075}
        }
        
        model_pricing = pricing.get(model, pricing["claude-3-5-sonnet-20241022"])
        input_cost = (input_tokens / 1000) * model_pricing["input"]
        output_cost = (output_tokens / 1000) * model_pricing["output"]
        
        return input_cost + output_cost
    
    def _update_analytics(self, metrics: RequestMetrics):
        """Update aggregated analytics"""
        self.analytics.total_requests += 1
        
        if metrics.success:
            self.analytics.successful_requests += 1
        else:
            self.analytics.failed_requests += 1
            if metrics.error_type:
                self.analytics.errors_by_type[metrics.error_type] += 1
        
        self.analytics.total_tokens += metrics.input_tokens + metrics.output_tokens
        self.analytics.total_cost_usd += metrics.cost_usd
        self.analytics.requests_by_model[metrics.model] += 1
        
        # Update average response time
        if self.analytics.total_requests > 0:
            total_time = self.analytics.avg_response_time * (self.analytics.total_requests - 1)
            self.analytics.avg_response_time = (total_time + metrics.response_time) / self.analytics.total_requests
        
        # Update hourly usage
        hour = metrics.timestamp.hour
        self.analytics.hourly_usage[hour] += 1
    
    def get_analytics(self) -> UsageAnalytics:
        """Get current analytics"""
        with self._lock:
            return self.analytics
    
    def display_analytics(self):
        """Display analytics in a beautiful Rich table"""
        analytics = self.get_analytics()
        
        # Create summary table
        summary_table = Table(title="📊 Claude Labs Usage Analytics", show_header=True, header_style="bold magenta")
        summary_table.add_column("Metric", style="cyan", no_wrap=True)
        summary_table.add_column("Value", style="green")
        
        summary_table.add_row("Total Requests", str(analytics.total_requests))
        summary_table.add_row("Successful", f"{analytics.successful_requests} ({analytics.successful_requests/analytics.total_requests*100:.1f}%)" if analytics.total_requests > 0 else "0")
        summary_table.add_row("Failed", f"{analytics.failed_requests} ({analytics.failed_requests/analytics.total_requests*100:.1f}%)" if analytics.total_requests > 0 else "0")
        summary_table.add_row("Total Tokens", f"{analytics.total_tokens:,}")
        summary_table.add_row("Total Cost", f"${analytics.total_cost_usd:.4f}")
        summary_table.add_row("Avg Response Time", f"{analytics.avg_response_time:.2f}s")
        
        console.print(summary_table)
        
        # Model usage breakdown
        if analytics.requests_by_model:
            model_table = Table(title="🤖 Model Usage", show_header=True, header_style="bold blue")
            model_table.add_column("Model", style="cyan")
            model_table.add_column("Requests", style="green")
            model_table.add_column("Percentage", style="yellow")
            
            for model, count in analytics.requests_by_model.items():
                percentage = (count / analytics.total_requests * 100) if analytics.total_requests > 0 else 0
                model_table.add_row(model, str(count), f"{percentage:.1f}%")
            
            console.print(model_table)
        
        # Error breakdown
        if analytics.errors_by_type:
            error_table = Table(title="❌ Error Analysis", show_header=True, header_style="bold red")
            error_table.add_column("Error Type", style="cyan")
            error_table.add_column("Count", style="red")
            
            for error_type, count in analytics.errors_by_type.items():
                error_table.add_row(error_type, str(count))
            
            console.print(error_table)
    
    def export_analytics(self, filename: str = "claude_analytics.json"):
        """Export analytics to JSON file"""
        analytics_dict = asdict(self.get_analytics())
        analytics_dict["exported_at"] = datetime.now().isoformat()
        
        with open(filename, 'w') as f:
            json.dump(analytics_dict, f, indent=2, default=str)
        
        console.print(f"📊 Analytics exported to {filename}")

class RateLimiter:
    """Intelligent rate limiting with exponential backoff"""
    
    def __init__(self, max_requests_per_minute: int = 50, max_requests_per_hour: int = 1000):
        self.max_requests_per_minute = max_requests_per_minute
        self.max_requests_per_hour = max_requests_per_hour
        self.request_times: deque = deque(maxlen=max_requests_per_hour)
        self._lock = threading.Lock()
    
    def can_make_request(self) -> bool:
        """Check if we can make a request without hitting rate limits"""
        now = time.time()
        
        with self._lock:
            # Remove old requests (older than 1 hour)
            while self.request_times and now - self.request_times[0] > 3600:
                self.request_times.popleft()
            
            # Check minute limit
            minute_ago = now - 60
            recent_requests = sum(1 for t in self.request_times if t > minute_ago)
            
            if recent_requests >= self.max_requests_per_minute:
                return False
            
            # Check hour limit
            if len(self.request_times) >= self.max_requests_per_hour:
                return False
            
            return True
    
    def record_request(self):
        """Record a request for rate limiting"""
        with self._lock:
            self.request_times.append(time.time())
    
    def get_wait_time(self) -> float:
        """Get recommended wait time if rate limited"""
        now = time.time()
        
        with self._lock:
            if not self.request_times:
                return 0
            
            # Find oldest request in last minute
            minute_ago = now - 60
            recent_requests = [t for t in self.request_times if t > minute_ago]
            
            if recent_requests:
                oldest_recent = min(recent_requests)
                return max(0, 60 - (now - oldest_recent))
            
            return 0

class ErrorTracker:
    """Enhanced error tracking with suggestions"""
    
    def __init__(self):
        self.error_patterns = {
            "authentication": {
                "patterns": ["invalid api key", "unauthorized", "401"],
                "suggestions": [
                    "Check your ANTHROPIC_API_KEY environment variable",
                    "Verify your API key is correct at https://console.anthropic.com/",
                    "Ensure your account has sufficient credits"
                ]
            },
            "rate_limit": {
                "patterns": ["rate limit", "429", "too many requests"],
                "suggestions": [
                    "Wait a moment before making another request",
                    "Consider using a different model (Haiku is faster)",
                    "Check your usage limits in the Anthropic Console"
                ]
            },
            "model_error": {
                "patterns": ["model not found", "invalid model"],
                "suggestions": [
                    "Check the model name is correct",
                    "Use one of: claude-3-5-sonnet-20241022, claude-3-5-haiku-20241022, claude-3-opus-20240229"
                ]
            },
            "network": {
                "patterns": ["connection", "timeout", "network"],
                "suggestions": [
                    "Check your internet connection",
                    "Try again in a moment",
                    "Verify Anthropic's service status"
                ]
            }
        }
    
    def analyze_error(self, error: Exception) -> Dict[str, Any]:
        """Analyze error and provide suggestions"""
        error_str = str(error).lower()
        error_type = type(error).__name__
        
        # Find matching error patterns
        suggestions = []
        detected_type = "unknown"
        
        for error_category, info in self.error_patterns.items():
            if any(pattern in error_str for pattern in info["patterns"]):
                suggestions.extend(info["suggestions"])
                detected_type = error_category
        
        return {
            "error_type": error_type,
            "detected_category": detected_type,
            "message": str(error),
            "suggestions": suggestions,
            "stack_trace": traceback.format_exc()
        }
    
    def display_error_analysis(self, error: Exception):
        """Display error analysis with Rich formatting"""
        analysis = self.analyze_error(error)
        
        # Create error panel
        error_text = Text()
        error_text.append(f"❌ Error Type: {analysis['error_type']}\n", style="red")
        error_text.append(f"🔍 Category: {analysis['detected_category']}\n", style="yellow")
        error_text.append(f"💬 Message: {analysis['message']}\n", style="white")
        
        if analysis['suggestions']:
            error_text.append("\n💡 Suggestions:\n", style="green")
            for i, suggestion in enumerate(analysis['suggestions'], 1):
                error_text.append(f"  {i}. {suggestion}\n", style="cyan")
        
        error_panel = Panel(error_text, title="Error Analysis", border_style="red")
        console.print(error_panel)

# Global monitor instance
monitor = ClaudeMonitor()
error_tracker = ErrorTracker()

def monitor_request(func):
    """Decorator to monitor API requests"""
    def wrapper(*args, **kwargs):
        start_time = time.time()
        request_id = None
        
        try:
            # Check rate limiting
            if not monitor.rate_limiter.can_make_request():
                wait_time = monitor.rate_limiter.get_wait_time()
                console.print(f"⏳ Rate limited. Please wait {wait_time:.1f} seconds...")
                time.sleep(wait_time)
            
            # Record request start
            model = kwargs.get('model', 'unknown')
            input_text = args[0] if args else kwargs.get('text', '')
            request_id = monitor.log_request(model, input_text, start_time)
            
            # Make the request
            result = func(*args, **kwargs)
            
            # Record successful response
            end_time = time.time()
            monitor.rate_limiter.record_request()
            
            # Extract token info from result (if available)
            input_tokens = getattr(result, 'usage', {}).get('input_tokens', 0)
            output_tokens = getattr(result, 'usage', {}).get('output_tokens', 0)
            
            monitor.log_response(
                request_id, result, end_time, input_tokens, output_tokens, model, success=True
            )
            
            return result
            
        except Exception as e:
            # Record failed response
            end_time = time.time()
            monitor.rate_limiter.record_request()
            
            monitor.log_response(
                request_id, None, end_time, 0, 0, 'unknown', success=False, error=e
            )
            
            # Display error analysis
            error_tracker.display_error_analysis(e)
            
            raise
    
    return wrapper 