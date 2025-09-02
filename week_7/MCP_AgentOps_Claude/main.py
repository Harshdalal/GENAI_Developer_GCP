#!/usr/bin/env python3
"""
MCP Calculator Server with AgentOps Integration
Unicode-safe version without emojis for Windows compatibility
"""

import os
import sys
import json
import traceback
from typing import Optional, Union, Dict, Any

# Fix Windows Unicode issues at the very start
if sys.platform == "win32":
    os.environ["PYTHONIOENCODING"] = "utf-8"

# Try to load environment from .env file
try:
    from dotenv import load_dotenv
    load_dotenv()
    # No print statements during import to avoid JSON issues
except ImportError:
    pass

# Initialize AgentOps with comprehensive error handling
agentops = None
AGENTOPS_ENABLED = False
AGENTOPS_SESSION_ID = None

def init_agentops():
    """Initialize AgentOps with proper error handling"""
    global agentops, AGENTOPS_ENABLED, AGENTOPS_SESSION_ID
    
    try:
        api_key = os.getenv("AGENTOPS_API_KEY")
        if not api_key:
            return False
        
        # Import and initialize AgentOps
        import agentops as ao
        agentops = ao
        
        # Initialize with comprehensive configuration
        session = agentops.init(
            api_key=api_key,
            tags=["mcp-server", "calculator", "fastmcp"],
            default_tags=["calculator-operation"]
        )
        
        if session:
            AGENTOPS_SESSION_ID = session
            AGENTOPS_ENABLED = True
            return True
        else:
            return False
            
    except Exception:
        return False

# Initialize AgentOps
init_agentops()

# Import FastMCP after AgentOps initialization
try:
    from mcp.server.fastmcp import FastMCP
except ImportError:
    sys.exit(1)

# Initialize MCP Server
mcp = FastMCP("calculator-server")

# -----------------------------
# Logging Functions (No Unicode)
# -----------------------------

def log_to_agentops(operation: str, inputs: Dict[str, Any], result: Any = None, error: str = None):
    """AgentOps logging without console output"""
    if not AGENTOPS_ENABLED or not agentops:
        return
    
    try:
        event_data = {
            "operation": operation,
            "inputs": inputs
        }
        
        if result is not None:
            event_data["result"] = result
            event_data["status"] = "success"
        
        if error is not None:
            event_data["error"] = error
            event_data["status"] = "error"
        
        # Try AgentOps logging methods
        try:
            action_event = agentops.ActionEvent(
                action_type=f"calculator_{operation}",
                params=event_data
            )
            agentops.record(action_event)
            return
        except AttributeError:
            pass
        
        try:
            agentops.record({
                "event_type": "calculator_operation",
                "operation": operation,
                **event_data
            })
            return
        except (AttributeError, TypeError):
            pass
        
        try:
            agentops.log(
                event_type="calculator_operation",
                details=event_data
            )
            return
        except AttributeError:
            pass
            
    except Exception:
        # Silently handle AgentOps errors
        pass

# -----------------------------
# Calculator Tools
# -----------------------------

@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers and return the result."""
    try:
        result = a + b
        log_to_agentops("add", {"a": a, "b": b}, result)
        return result
    except Exception as e:
        log_to_agentops("add", {"a": a, "b": b}, error=str(e))
        raise

@mcp.tool()
def subtract(a: int, b: int) -> int:
    """Subtract the second number from the first."""
    try:
        result = a - b
        log_to_agentops("subtract", {"a": a, "b": b}, result)
        return result
    except Exception as e:
        log_to_agentops("subtract", {"a": a, "b": b}, error=str(e))
        raise

@mcp.tool()
def multiply(a: int, b: int) -> int:
    """Multiply two numbers."""
    try:
        result = a * b
        log_to_agentops("multiply", {"a": a, "b": b}, result)
        return result
    except Exception as e:
        log_to_agentops("multiply", {"a": a, "b": b}, error=str(e))
        raise

@mcp.tool()
def divide(a: float, b: float) -> float:
    """Divide the first number by the second. Raises ZeroDivisionError if b is zero."""
    try:
        if b == 0:
            error_msg = "Cannot divide by zero"
            log_to_agentops("divide", {"a": a, "b": b}, error=error_msg)
            raise ZeroDivisionError(error_msg)
        
        result = a / b
        log_to_agentops("divide", {"a": a, "b": b}, result)
        return result
    except ZeroDivisionError:
        raise
    except Exception as e:
        log_to_agentops("divide", {"a": a, "b": b}, error=str(e))
        raise

@mcp.tool()
def power(a: float, b: float) -> float:
    """Raise the first number to the power of the second."""
    try:
        result = a ** b
        log_to_agentops("power", {"a": a, "b": b}, result)
        return result
    except Exception as e:
        log_to_agentops("power", {"a": a, "b": b}, error=str(e))
        raise

@mcp.tool()
def sqrt(a: float) -> float:
    """Calculate the square root of a number."""
    try:
        if a < 0:
            error_msg = "Cannot calculate square root of negative number"
            log_to_agentops("sqrt", {"a": a}, error=error_msg)
            raise ValueError(error_msg)
        
        import math
        result = math.sqrt(a)
        log_to_agentops("sqrt", {"a": a}, result)
        return result
    except ValueError:
        raise
    except Exception as e:
        log_to_agentops("sqrt", {"a": a}, error=str(e))
        raise

# -----------------------------
# Resources
# -----------------------------

@mcp.resource("calculator://greet/{name}")
def calculator_greeting(name: str) -> str:
    """Get a personalized greeting."""
    try:
        greeting = f"Hello, {name}! Ready to perform some calculations?"
        log_to_agentops("greeting", {"name": name}, greeting)
        return greeting
    except Exception as e:
        log_to_agentops("greeting", {"name": name}, error=str(e))
        raise

@mcp.resource("calculator://usage")
def get_usage_guide() -> str:
    """Get comprehensive usage guide for the calculator."""
    try:
        usage_content = """Calculator MCP Server Usage Guide

Available Tools:
- add(a, b) - Add two numbers
- subtract(a, b) - Subtract b from a  
- multiply(a, b) - Multiply two numbers
- divide(a, b) - Divide a by b (b cannot be 0)
- power(a, b) - Calculate a raised to power b
- sqrt(a) - Square root of a (a >= 0)

Examples:
- add(15, 25) = 40
- subtract(100, 30) = 70
- multiply(7, 8) = 56
- divide(84, 12) = 7.0
- power(2, 8) = 256.0
- sqrt(64) = 8.0

Resources:
- calculator://greet/{name} - Personalized greeting
- calculator://usage - This usage guide

Prompts:
- calculator_prompt(a, b, operation) - Execute calculation with context

Features:
- AgentOps integration for operation tracking
- Comprehensive error handling
- Support for integer and float operations
- Input validation and safety checks
        """.strip()
        
        log_to_agentops("usage_guide", {}, f"Generated ({len(usage_content)} chars)")
        return usage_content
    except Exception as e:
        log_to_agentops("usage_guide", {}, error=str(e))
        raise

# -----------------------------
# Prompts
# -----------------------------

@mcp.prompt()
def calculator_prompt(a: float, b: float, operation: str) -> str:
    """Execute a calculation with detailed context and explanation."""
    try:
        log_to_agentops("prompt_start", {"a": a, "b": b, "operation": operation})
        
        operation = operation.lower().strip()
        
        # Map operations to functions
        operations = {
            "add": lambda x, y: add(int(x), int(y)),
            "subtract": lambda x, y: subtract(int(x), int(y)),
            "multiply": lambda x, y: multiply(int(x), int(y)),
            "divide": lambda x, y: divide(x, y),
            "power": lambda x, y: power(x, y),
            "sqrt": lambda x, y: sqrt(x)
        }
        
        if operation not in operations:
            available_ops = ", ".join(operations.keys())
            error_msg = f"Invalid operation '{operation}'. Available: {available_ops}"
            log_to_agentops("prompt_error", {"a": a, "b": b, "operation": operation}, error=error_msg)
            return f"Error: {error_msg}"
        
        try:
            if operation == "sqrt":
                result = operations[operation](a, None)
                response = f"The square root of {a} is {result}"
            else:
                result = operations[operation](a, b)
                response = f"{operation.title()}({a}, {b}) = {result}"
            
            log_to_agentops("prompt_success", {"a": a, "b": b, "operation": operation}, response)
            return response
            
        except ZeroDivisionError:
            error_response = "Error: Division by zero is not allowed"
            log_to_agentops("prompt_error", {"a": a, "b": b, "operation": operation}, error=error_response)
            return error_response
        except ValueError as ve:
            error_response = f"Error: {str(ve)}"
            log_to_agentops("prompt_error", {"a": a, "b": b, "operation": operation}, error=error_response)
            return error_response
            
    except Exception as e:
        error_msg = f"Prompt execution failed: {str(e)}"
        log_to_agentops("prompt_error", {"a": a, "b": b, "operation": operation}, error=error_msg)
        return f"Error: {error_msg}"

# -----------------------------
# Server Health Check
# -----------------------------

@mcp.tool()
def health_check() -> Dict[str, Any]:
    """Check server health and status."""
    try:
        status = {
            "server_status": "healthy",
            "agentops_enabled": AGENTOPS_ENABLED,
            "agentops_session": str(AGENTOPS_SESSION_ID) if AGENTOPS_SESSION_ID else None,
            "available_operations": ["add", "subtract", "multiply", "divide", "power", "sqrt"],
            "python_version": sys.version.split()[0],
            "platform": sys.platform
        }
        
        log_to_agentops("health_check", {}, status)
        return status
    except Exception as e:
        log_to_agentops("health_check", {}, error=str(e))
        raise

# -----------------------------
# Main Server Execution
# -----------------------------

def main():
    """Main server execution with minimal console output."""
    try:
        mcp.run(transport="stdio")
    except KeyboardInterrupt:
        pass
    except Exception:
        pass
    finally:
        cleanup()

def cleanup():
    """Clean shutdown procedures."""
    if AGENTOPS_ENABLED and agentops:
        try:
            agentops.end_session("Success")
        except Exception:
            pass

if __name__ == "__main__":
    main()