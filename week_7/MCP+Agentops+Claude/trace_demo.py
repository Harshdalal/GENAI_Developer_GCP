from mcp.server.fastmcp import FastMCP
import agentops
import os

# -----------------------------
# Initialize AgentOps
# -----------------------------
# Make sure you set AGENTOPS_API_KEY in your environment:
#   Windows (CMD): set AGENTOPS_API_KEY=your_key_here
#   Linux/Mac: export AGENTOPS_API_KEY=your_key_here
agentops.init(api_key=os.getenv("AGENTOPS_API_KEY"), tags=["fastmcp", "calculator"])

# -----------------------------
# Initialize MCP Server
# -----------------------------
mcp = FastMCP("calculator server")

# -----------------------------
# Register Tools
# -----------------------------
@mcp.tool("Addition")
def add(a: int, b: int) -> int:
    """add two numbers and return the result."""
    with agentops.trace("Addition Tool"):
        result = a + b
        agentops.log("Inputs", {"a": a, "b": b})
        agentops.log("Result", result)
        return result

@mcp.tool("Subtract")
def subtract(a: int, b: int) -> int:
    """subtract the second number from first."""
    with agentops.trace("Subtract Tool"):
        result = a - b
        agentops.log("Inputs", {"a": a, "b": b})
        agentops.log("Result", result)
        return result

@mcp.tool("multiply")
def multiply(a: int, b: int) -> int:
    """Multiply two numbers."""
    with agentops.trace("Multiply Tool"):
        result = a * b
        agentops.log("Inputs", {"a": a, "b": b})
        agentops.log("Result", result)
        return result

@mcp.tool("division")
def divide(a: float, b: float) -> float:
    """Divide the first number by the second number. Raises error on division by Zero."""
    with agentops.trace("Division Tool"):
        if b == 0:
            agentops.log("Error", "Division by zero")
            raise ZeroDivisionError("Division by zero")
        result = a / b
        agentops.log("Inputs", {"a": a, "b": b})
        agentops.log("Result", result)
        return result

# -----------------------------
# Register Resources
# -----------------------------
@mcp.resource("calculator://greet/{name}")
def calculator_greeting(name: str) -> str:
    """Get a personalized greeting"""
    with agentops.trace("Greeting Resource"):
        greeting = f"Hello, {name}! Ready to calculate something today?"
        agentops.log("Greeting", greeting)
        return greeting

@mcp.resource("usage://guide")
def get_usage() -> str:
    with agentops.trace("Usage Guide Resource"):
        with open("docs/usage.txt") as f:
            content = f.read()
            agentops.log("Usage Guide", content[:100] + "...")  # log preview
            return content

# -----------------------------
# Register Prompts
# -----------------------------
@mcp.prompt()
def calculator_prompt(a: float, b: float, operation: str) -> str:
    """Prompt for a calculation and return the result."""
    with agentops.trace("Calculator Prompt"):
        agentops.log("Inputs", {"a": a, "b": b, "operation": operation})

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

# -----------------------------
# Run the MCP Server
# -----------------------------
if __name__ == "__main__":
    print("🚀 Calculator MCP server with AgentOps tracing started!")
    mcp.run(transport="stdio")
