# Introduction to MCP and FastMCP
# MCP (Multi-Command Protocol) is a lightweight and flexible framework for building interactive command-based applications. FastMCP, built on top of MCP, provides a way to define tools (functions), resources (APIs), and prompts (smart interactions) in a Pythonic and modular way.

# This code example shows how to use FastMCP to build a calculator server that exposes math operations and supports interactive prompts — ideal for integrating into AI assistants, command-based UIs, or developer tools.

# Why Use FastMCP for Building a Tool Server?
# FastMCP is useful for:

# Defining Tools: Wrap standard Python functions as callable services
# Resources: Expose static or dynamic resources like usage guides or personalized messages
# Prompts: Add intelligent, conversational interfaces with logic-driven responses
# Transport Flexibility: Support different I/O protocols like stdio, websockets, etc.

# This allows developers to quickly build and serve interactive tools in a structured and extensible way.

# What This Server Does – A Calculator App
# In this example, the MCP server acts as a simple calculator backend, providing arithmetic functions through tools, dynamic greetings via resources, and an intelligent prompt to guide the user.

from mcp.server.fastmcp import FastMCP

# Initialize the Server
mcp = FastMCP("calculator server")

# Register Tools (Functional APIs)
# Each function is decorated with @mcp.tool("Name"), making it callable through the MCP protocol.
@mcp.tool("Addition")
def add(a: int, b: int) -> int:
    """add two numbers and return the result."""
    return a + b


@mcp.tool("Subtract")
def subtract(a: int, b: int) -> int:
    """subtract the second number from first."""
    return a-b

@mcp.tool("multiply")
def multiply(a: int, b: int) -> int:
    """Multiply two numbers."""
    return a*b

@mcp.tool("division")
def divide(a: float, b: float) -> float:
    """Divide the first number by the second number. Raises error on division by Zero."""
    if b == 0:
        raise ZeroDivisionError("Division by zero")
    else:
        return a / b

# Register Resources (Non-functional content)
# Resources are like read-only APIs or information endpoints.
@mcp.resource("calculator://greet/{name}")
def calculator_greeting(name: str) -> str:
    """Get a personalized greeting"""
    return f"Hello, {name}! Ready to calculate something today?"

@mcp.resource("usage://guide")
def get_usage() -> str:
    with open("docs/usage.txt") as f:
        return f.read()

# Add Prompt Logic (Interactive Responses)
# Prompts allow conversational querying, like natural language requests:    
@mcp.prompt()
def calculator_prompt(a: float, b: float, operation: str) -> str:
    """Prompt for a calculation and return the result."""
    if operation == "add":
        return f"The result of adding {a} and {b} is {add(a, b)}"
    elif operation == "subtract":
        return f"The result of subtracting {b} from {a} is {subtract(a, b)}"
    elif operation == "multiply":
        return f"The result of multiplying {a} and {b} is {multiply(a, b)}"
    elif operation == "divide":
        try:
            return f"The result of dividing {a} by {b} is {divide(a, b)}"
        except ValueError as e:
            return str(e)
    else:
        return "Invalid operation. Please choose add, subtract, multiply, or divide."

# Run the MCP Server
if __name__ == "__main__":
    mcp.run(transport="stdio")


