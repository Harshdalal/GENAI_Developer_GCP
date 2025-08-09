# MCP Calculator Server

A Model Context Protocol (MCP) server that provides basic mathematical operations and can be integrated with Claude Desktop for enhanced calculation capabilities.

## What is MCP?

**Model Context Protocol (MCP)** is an open standard that enables AI assistants to securely connect to external data sources and tools. It allows Claude Desktop to interact with your local files, databases, and custom applications through standardized servers.

### Key Benefits:
- **Secure Integration**: Connect Claude to your local tools safely
- **Extensible**: Build custom tools and resources
- **Standardized**: Uses a common protocol for AI-tool communication
- **Real-time**: Access live data and perform actions

## Features

This calculator server provides:

### 🔧 Tools
- **Addition**: Add two numbers
- **Subtraction**: Subtract second number from first
- **Multiplication**: Multiply two numbers
- **Division**: Divide numbers with zero-division protection

### 📚 Resources
- **Personal Greetings**: Get customized welcome messages
- **Usage Guide**: Access documentation from local files

### 💬 Prompts
- **Calculator Prompt**: Structured calculation requests with formatted responses

## Prerequisites

- **Python 3.8+** installed on your system
- **Claude Desktop** application
- **pip** package manager

## Step-by-Step Setup Guide

### Step 1: Install Claude Desktop

1. **Download Claude Desktop**:
   - Visit [Claude Desktop Download Page](https://claude.ai/download)
   - Choose your operating system (Windows, macOS, or Linux)
   - Download and install the application

2. **Create Claude Account**:
   - Open Claude Desktop
   - Sign up or log in with your existing account

### Step 2: Prepare Your Python Environment

1. **Verify Python Installation**:
   ```bash
   python --version
   # Should show Python 3.8 or higher
   ```

2. **Install Required Package**:
   ```bash
   pip install mcp
   ```

### Step 3: Set Up the Calculator Server

1. **Create Project Directory**:
   ```bash
   mkdir mcp_calculator
   cd mcp_calculator
   ```

2. **Save the Calculator Code**:
   - Create a file named `calculator.py`
   - Copy the provided calculator server code into this file

3. **Create Documentation Directory** (Optional):
   ```bash
   mkdir docs
   echo "Calculator MCP Server Usage Guide" > docs/usage.txt
   echo "Use the available tools to perform calculations." >> docs/usage.txt
   ```

4. **Test the Server**:
   ```bash
   python calculator.py
   # The server should start without errors
   # Press Ctrl+C to stop
   ```

### Step 4: Configure Claude Desktop (Windows)

1. **Locate Configuration File**:
   - Press `Windows + R`
   - Type: `%APPDATA%\Claude`
   - Press Enter
   - Look for `claude_desktop_config.json`

2. **Create Configuration File** (if it doesn't exist):
   - Right-click in the Claude folder
   - Select "New" → "Text Document"
   - Rename it to `claude_desktop_config.json`
   - Make sure to change the extension from `.txt` to `.json`

3. **Edit Configuration File**:
   - Right-click on `claude_desktop_config.json`
   - Open with Notepad or any text editor
   - Replace all content with:

   ```json
   {
     "mcpServers": {
       "calculator-server": {
         "command": "python",
         "args": [
           "D:/mcp_learning/calculator.py"
         ]
       }
     }
   }
   ```

4. **Important Windows Path Notes**:
   - **Use forward slashes** `/` instead of backslashes `\`
   - **Example paths**:
     - `"C:/Users/YourName/Documents/calculator.py"`
     - `"D:/Projects/mcp_calculator/calculator.py"`
     - `"E:/Python_Projects/calculator.py"`

5. **Find Your File Path**:
   - Navigate to your `calculator.py` file in File Explorer
   - Right-click on the file
   - Select "Copy as path"
   - Paste it in the config, but change `\` to `/`
   
   **Example**:
   - Copied path: `"C:\Users\John\Desktop\calculator.py"`
   - Config path: `"C:/Users/John/Desktop/calculator.py"`

### Step 5: Restart and Test

1. **Restart Claude Desktop**:
   - Completely close Claude Desktop
   - Restart the application

2. **Verify Connection**:
   - Look for a "Connected" status or server indicator
   - Check that no error messages appear

3. **Test the Tools**:
   In Claude Desktop, try these commands:
   ```
   Add 15 and 25
   Calculate 100 divided by 4
   Multiply 7 by 8
   What's 50 minus 12?
   ```

## Usage Examples

### Basic Calculations
```
User: "Add 123 and 456"
Claude: Uses the addition tool → Result: 579

User: "What's 144 divided by 12?"
Claude: Uses the division tool → Result: 12.0
```

### Resource Access
```
User: "Give me a greeting for John"
Claude: Accesses greeting resource → "Hello, John! Ready to calculate something today?"

User: "Show me the usage guide"
Claude: Reads from docs/usage.txt → Displays documentation
```

## Windows-Specific Troubleshooting

### Common Windows Issues

**1. "Python is not recognized"**
   - Open Command Prompt as Administrator
   - Type: `python --version`
   - If error occurs, reinstall Python and check "Add to PATH" during installation

**2. "Access denied" or "Permission error"**
   - Right-click on Claude Desktop
   - Select "Run as administrator"
   - Try again

**3. "File path not found"**
   - Open File Explorer
   - Navigate to your calculator.py file
   - Right-click → "Copy as path"
   - Replace `\` with `/` in the config file

**4. Configuration file location issues**
   - Press `Windows + R`
   - Type: `%APPDATA%`
   - Navigate to Claude folder
   - Create folder if it doesn't exist

### Windows Debug Steps

1. **Test Python Installation**:
   ```cmd
   python --version
   python -c "print('Python is working')"
   ```

2. **Test Calculator Script**:
   ```cmd
   cd D:\mcp_learning
   python calculator.py
   ```

3. **Find Configuration Path**:
   ```cmd
   echo %APPDATA%\Claude\claude_desktop_config.json
   ```

4. **Open Configuration Location**:
   - Press `Windows + R`
   - Type: `%APPDATA%\Claude`
   - Press Enter

## File Structure

```
mcp_calculator/
├── calculator.py          # Main MCP server
├── docs/
│   └── usage.txt         # Documentation resource
└── README.md            # This file
```