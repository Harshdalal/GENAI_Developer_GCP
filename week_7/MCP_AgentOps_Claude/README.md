# Windows: Claude Desktop + MCP + Agentops Calculator Complete Setup

Complete step-by-step guide for Windows users to set up Claude Desktop with your custom MCP Calculator Server. Follow every step for guaranteed success!

## 📥 Step 1: Download and Install Claude Desktop

### Download Claude Desktop for Windows

1. **Visit the official website**
   - Open your web browser
   - Go to: **https://claude.ai/download**
   - Or search "Claude Desktop download" on Google

2. **Download the Windows installer**
   - Click **"Download for Windows"**
   - File will download as: `Claude-Setup-x.x.x.exe`
   - Wait for download to complete (usually in Downloads folder)

3. **Install Claude Desktop**
   - Go to your Downloads folder
   - Double-click `Claude-Setup-x.x.x.exe`
   - Click **"Yes"** when Windows asks for permission
   - Follow the installation wizard:
     - Choose installation location (default `C:\Users\[YourName]\AppData\Local\Claude` is fine)
     - Click **"Install"**
     - Wait for installation to complete
     - Click **"Finish"**

4. **First Launch**
   - Claude Desktop should launch automatically
   - If not, press `Win + S`, type "Claude", and click the app
   - Sign in with your Claude account (or create a new one at claude.ai)
   - Complete any initial setup

## 🐍 Step 2: Install Python for Windows

### Check if Python is Already Installed

1. **Open Command Prompt**
   - Press `Win + R`
   - Type `cmd` and press Enter
   - Black window should open

2. **Test Python installation**
   - Type: `python --version` and press Enter
   - If you see something like `Python 3.11.0`, Python is installed ✅
   - If you see `'python' is not recognized...`, you need to install Python ❌

### Install Python (if needed)

1. **Download Python**
   - Go to: **https://www.python.org/downloads/**
   - Click the big yellow button **"Download Python 3.x.x"**
   - Wait for `python-3.x.x-amd64.exe` to download

2. **Install Python**
   - Double-click the downloaded file
   - ⚠️ **CRITICAL**: Check the box **"Add Python to PATH"** at the bottom
   - Click **"Install Now"**
   - Wait for installation (may take a few minutes)
   - Click **"Close"** when finished

3. **Verify Installation**
   - Open a **NEW** Command Prompt window (important!)
   - Type: `python --version`
   - Should show: `Python 3.x.x`

## 📁 Step 3: Create Your Project Folder

### Set Up Project Directory

1. **Create folder on Desktop**
   - Go to your Desktop
   - Right-click on empty space
   - Select **"New" → "Folder"**
   - Name it: `mcp-calculator`
   - Double-click to open the folder

2. **Open Command Prompt in this folder**
   - Inside the `mcp-calculator` folder
   - Hold `Shift` and right-click on empty space
   - Select **"Open PowerShell window here"** or **"Open command window here"**
   - You should see something like: `C:\Users\YourName\Desktop\mcp-calculator>`

## 📝 Step 4: Create Your Project Files

### Create main.py

1. **Create the main server file**
   - In the `mcp-calculator` folder, right-click on empty space
   - Select **"New" → "Text Document"**
   - Rename from `New Text Document.txt` to `main.py`
   - If Windows warns about changing file extension, click **"Yes"**

2. **Add the server code**
   - Right-click on `main.py`
   - Select **"Open with" → "Notepad"**
   - Delete any existing content
   - Copy and paste your complete `main.py` code
   - Press `Ctrl + S` to save
   - Close Notepad

### Create client_test.py

1. **Create the test file**
   - Right-click in the folder → **"New" → "Text Document"**
   - Rename to `client_test.py`
   - Click **"Yes"** to change extension

2. **Add the test code**
   - Open with Notepad
   - Copy and paste your complete `client_test.py` code
   - Save with `Ctrl + S`
   - Close Notepad

### Create .env file

1. **Create environment file**
   - Right-click in folder → **"New" → "Text Document"**
   - Try to rename to `.env`
   - If Windows won't let you, use Command Prompt method:

2. **Alternative method using Command Prompt**
   - In your Command Prompt window (should be in the mcp-calculator folder)
   - Type: `echo # Environment variables > .env`
   - Press Enter

3. **Edit the .env file**
   - Open `.env` with Notepad
   - Replace contents with:
   ```
   # AgentOps API Key (optional - get from https://agentops.ai)
   AGENTOPS_API_KEY=your_agentops_api_key_here
   
   # Python encoding for Windows
   PYTHONIOENCODING=utf-8
   ```
   - Save the file

### Verify Your Files

Your `mcp-calculator` folder should now contain:
- ✅ `main.py`
- ✅ `client_test.py` 
- ✅ `.env`

## 📦 Step 5: Install Required Python Packages

### Install Dependencies

1. **Use the Command Prompt in your project folder**
   - Should still be open from Step 3
   - If closed, navigate back to the folder and Shift + right-click → "Open PowerShell window here"

2. **Install the packages**
   - Type this command and press Enter:
   ```cmd
   pip install python-dotenv fastmcp agentops
   ```
   - Wait for installation to complete
   - You should see "Successfully installed" messages

3. **If you get errors**
   - Try: `python -m pip install python-dotenv fastmcp agentops`
   - Or try: `py -m pip install python-dotenv fastmcp agentops`

## 🧪 Step 6: Test Your MCP Server

### Run the Test Script

1. **Test the server**
   - In your Command Prompt (in the mcp-calculator folder)
   - Type: `python client_test.py`
   - Press Enter

2. **Expected successful output:**
   ```
   === Simple MCP Server Test ===
   This test avoids Unicode characters to prevent JSON errors.
   
   Checking environment...
   SUCCESS: main.py found
   WARNING: AGENTOPS_API_KEY not set (or SUCCESS if you have it)
   Python version: 3.11.0
   Platform: win32
   
   Testing direct function calls...
   add(5, 3) = 8
   subtract(10, 4) = 6
   multiply(6, 7) = 42
   divide(15, 3) = 5.0
   SUCCESS: All function tests passed
   
   Testing MCP Server startup...
   SUCCESS: Server started without errors
   SUCCESS: Sent initialization message
   SUCCESS: Server stopped cleanly
   
   === Test Complete ===
   If you see 'SUCCESS' messages above, your server should work with Claude.
   ```

3. **If tests fail**
   - Make sure you're in the right folder
   - Check that Python is properly installed
   - Re-run the pip install command

## 🔧 Step 7: Configure Claude Desktop

### Find Claude Configuration Folder

1. **Open File Explorer**
   - Press `Win + E`

2. **Navigate to Claude config folder**
   - Click in the address bar at the top
   - Type: `%APPDATA%\Claude`
   - Press Enter
   - You should be in: `C:\Users\[YourName]\AppData\Roaming\Claude`

3. **If the folder doesn't exist**
   - The folder is created when Claude Desktop first runs
   - Launch Claude Desktop once, then try again

### Get Your Project Path

1. **Get the exact path to your main.py**
   - Go back to your `mcp-calculator` folder
   - Click on `main.py` to select it
   - Hold `Shift` and right-click on `main.py`
   - Select **"Copy as path"**
   - The path is now copied to your clipboard

2. **Alternative method**
   - Open Command Prompt in your project folder
   - Type: `echo %cd%\main.py`
   - Copy the output path

### Create Configuration File

1. **Check for existing config**
   - In the `%APPDATA%\Claude` folder
   - Look for a file named `claude_desktop_config.json`

2. **Create or edit the config file**
   - If file exists: Right-click → "Open with" → "Notepad"
   - If file doesn't exist: Right-click in folder → "New" → "Text Document" → rename to `claude_desktop_config.json`

3. **Add your MCP server configuration**
   - Replace `YOUR_FULL_PATH_TO_MAIN_PY` with the path you copied earlier
   - The path should look like: `C:\Users\YourName\Desktop\mcp-calculator\main.py`

   ```json
   {
     "mcpServers": {
       "calculator": {
         "command": "python",
         "args": ["YOUR_FULL_PATH_TO_MAIN_PY"],
         "env": {
           "AGENTOPS_API_KEY": "your_agentops_api_key_here",
           "PYTHONIOENCODING": "utf-8",
           "PYTHONUNBUFFERED": "1"
         }
       }
     }
   }
   ```

4. **Example with real path:**
   ```json
   {
     "mcpServers": {
       "calculator": {
         "command": "python",
         "args": ["C:\\Users\\John\\Desktop\\mcp-calculator\\main.py"],
         "env": {
           "AGENTOPS_API_KEY": "ag-your-api-key-here",
           "PYTHONIOENCODING": "utf-8",
           "PYTHONUNBUFFERED": "1"
         }
       }
     }
   }
   ```

5. **Important Notes:**
   - Use double backslashes `\\` in Windows paths
   - Keep all quotes and commas exactly as shown
   - If you don't have AgentOps API key, you can leave it as is or remove the env section

### Save the Configuration

1. **Save the file**
   - Press `Ctrl + S` in Notepad
   - Make sure it's saved as `claude_desktop_config.json`
   - Close Notepad

2. **Verify the file**
   - The file should appear in `%APPDATA%\Claude\`
   - File size should be more than 0 bytes

## 🔄 Step 8: Restart Claude Desktop

### Complete Restart Process

1. **Close Claude Desktop completely**
   - Right-click on Claude in the taskbar
   - Select **"Close window"** or click the X
   - Make sure Claude is not running in system tray

2. **Wait 5 seconds**

3. **Launch Claude Desktop**
   - Press `Win + S`
   - Type "Claude"
   - Click on Claude Desktop to launch
   - Sign in if prompted

## ✅ Step 9: Verify Connection

### Check for Calculator Integration

1. **Start a new conversation**
   - Click **"New Chat"** or similar button in Claude

2. **Look for the calculator indicator**
   - Look in the attachment area (usually at the bottom)
   - Should see a calculator icon (📱, 🧮, or "C" icon)
   - This indicates your MCP server is connected

3. **Test with calculations**
   - Type: **"What is 25 times 17?"**
   - Press Enter and wait for response
   - Claude should use your calculator server

4. **Verify it's working**
   - The response should show Claude used the "multiply" tool
   - You should see the calculation process
   - Result should be: 425

### Additional Test Questions

- what is the value of 10* 2?

Try these to verify everything works:
- "Calculate 456 + 789"
- "What's the square root of 144?"
- "What is 2 to the power of 8?"
- "Divide 1000 by 25"

## 🚨 Troubleshooting Windows Issues

### Issue 1: Calculator icon not showing

**Solutions:**
1. **Check config file location**
   - Make sure it's in `%APPDATA%\Claude\claude_desktop_config.json`
   - Not in `%LOCALAPPDATA%` or other locations

2. **Verify file path**
   - Open Command Prompt in your project folder
   - Type: `dir main.py` to confirm file exists
   - Copy the full path using `echo %cd%\main.py`

3. **Check JSON syntax**
   - Copy your JSON content
   - Go to https://jsonlint.com/
   - Paste and validate - fix any errors

### Issue 2: "Python is not recognized"

**Solutions:**
1. **Reinstall Python**
   - Download from python.org again
   - Make sure to check **"Add Python to PATH"**
   - Restart Command Prompt after installation

2. **Use full Python path**
   - Find Python installation: `where python`
   - Use full path in config: `"command": "C:\\Python311\\python.exe"`

### Issue 3: Import/Module errors

**Solutions:**
1. **Reinstall packages**
   ```cmd
   pip uninstall fastmcp agentops python-dotenv
   pip install fastmcp agentops python-dotenv
   ```

2. **Check pip installation**
   ```cmd
   python -m pip --version
   ```

### Issue 4: Permission denied errors

**Solutions:**
1. **Run as Administrator**
   - Right-click Command Prompt → "Run as administrator"
   - Navigate to your folder and retry

2. **Check file permissions**
   - Right-click on `main.py` → Properties → Security
   - Make sure you have full control

### Issue 5: Path with spaces

**Solutions:**
1. **Move project to path without spaces**
   - Avoid folders like "My Documents"
   - Use `C:\mcp-calculator` instead

2. **Or quote the path properly**
   ```json
   "args": ["C:\\Users\\John Smith\\Desktop\\mcp-calculator\\main.py"]
   ```

## 🎯 Step 10: Final Verification

### Complete Success Checklist

✅ **Claude Desktop installed and running**  
✅ **Python installed with PATH configured**  
✅ **Project files created in mcp-calculator folder**  
✅ **Python packages installed successfully**  
✅ **Test script runs without errors**  
✅ **Configuration file created with correct path**  
✅ **Claude Desktop restarted completely**  
✅ **Calculator icon appears in Claude**  
✅ **Claude performs calculations using your server**  

### Test Everything Works

1. **Ask Claude:** "What is 123 multiplied by 456?"
2. **Verify:** You see the multiply tool being used
3. **Check:** Result is 56,088
4. **Success:** Your MCP Calculator Server is fully operational!

## 🎉 Congratulations!

You have successfully set up Claude Desktop with your custom MCP Calculator Server on Windows! 

**What you achieved:**
- ✅ Installed Claude Desktop
- ✅ Set up Python development environment  
- ✅ Created a custom MCP server
- ✅ Connected it to Claude Desktop
- ✅ Enabled Claude to perform calculations using your local Python environment

**Claude can now:**
- Perform accurate mathematical calculations
- Use your local computing resources
- Show detailed calculation processes
- Handle complex mathematical operations

Enjoy your enhanced Claude experience with custom calculator capabilities!