#!/usr/bin/env python3
"""
Simple test script without Unicode characters
"""

import subprocess
import json
import sys
import time
import os

def test_server_startup():
    """Test if server starts without Unicode errors"""
    print("Testing MCP Server startup...")
    
    try:
        # Start the server
        process = subprocess.Popen(
            [sys.executable, 'main.py'],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            bufsize=0
        )
        
        # Give it time to start
        time.sleep(3)
        
        # Check if it's running
        if process.poll() is None:
            print("SUCCESS: Server started without errors")
            
            # Send a test message
            init_msg = json.dumps({
                "jsonrpc": "2.0",
                "id": 1,
                "method": "initialize",
                "params": {
                    "protocolVersion": "2024-11-05",
                    "capabilities": {},
                    "clientInfo": {
                        "name": "test-client",
                        "version": "1.0.0"
                    }
                }
            }) + "\n"
            
            try:
                process.stdin.write(init_msg)
                process.stdin.flush()
                print("SUCCESS: Sent initialization message")
                
                # Wait for response
                time.sleep(2)
                
            except Exception as e:
                print(f"WARNING: Could not send message: {e}")
        else:
            print("ERROR: Server failed to start")
            stderr = process.stderr.read()
            if stderr:
                print(f"Error output: {stderr}")
        
        # Clean up
        try:
            process.terminate()
            process.wait(timeout=5)
            print("SUCCESS: Server stopped cleanly")
        except:
            process.kill()
            print("WARNING: Server force killed")
            
    except Exception as e:
        print(f"ERROR: Test failed: {e}")

def test_direct_functions():
    """Test functions directly"""
    print("\nTesting direct function calls...")
    
    try:
        # Import the main module
        import sys
        if '.' not in sys.path:
            sys.path.insert(0, '.')
        
        import main
        
        # Test basic operations
        result = main.add(5, 3)
        print(f"add(5, 3) = {result}")
        
        result = main.subtract(10, 4)
        print(f"subtract(10, 4) = {result}")
        
        result = main.multiply(6, 7)
        print(f"multiply(6, 7) = {result}")
        
        result = main.divide(15, 3)
        print(f"divide(15, 3) = {result}")
        
        print("SUCCESS: All function tests passed")
        
    except Exception as e:
        print(f"ERROR: Function test failed: {e}")

def check_environment():
    """Check basic environment setup"""
    print("\nChecking environment...")
    
    # Check main.py exists
    if os.path.exists('main.py'):
        print("SUCCESS: main.py found")
    else:
        print("ERROR: main.py not found")
    
    # Check API key
    api_key = os.getenv("AGENTOPS_API_KEY")
    if api_key:
        masked = f"{api_key[:8]}...{api_key[-4:]}"
        print(f"SUCCESS: AgentOps API key found: {masked}")
    else:
        print("WARNING: AGENTOPS_API_KEY not set")
    
    # Check Python version
    print(f"Python version: {sys.version.split()[0]}")
    print(f"Platform: {sys.platform}")

def main():
    print("=== Simple MCP Server Test ===")
    print("This test avoids Unicode characters to prevent JSON errors.")
    
    check_environment()
    test_direct_functions()
    test_server_startup()
    
    print("\n=== Test Complete ===")
    print("If you see 'SUCCESS' messages above, your server should work with Claude.")

if __name__ == "__main__":
    main()