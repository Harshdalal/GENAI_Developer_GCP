
# Agent2Agent Project

## Quick Start Steps

### Prerequisites Check
```bash
python --version  # Should be 3.8+
uv --version      # Should be installed
```

### Project Setup
```bash
# Clone and navigate to project
cd Agent2Agent-Project

# Install dependencies
uv sync
```

### Start the Server
```bash
# Terminal 1
uv run .

# Wait for: "Uvicorn running on http://0.0.0.0:9999"
```

### Test the Agent
```bash
# Terminal 2
uv run --active test_client.py
```

### Interact and Test
- Choose menu options 1-5
- Try different messages
- Observe routing behavior

## File Structure with Briefs
- `Agent2Agent-Project/`
  - `__main__.py`: Main server - sets up A2A agent with 2 skills
  - `agent_executor.py`: Multi-skill executor - keyword-based routing logic
  - `test_client.py`: Interactive test client - user-friendly testing
  - `README.md`: Project documentation and setup guide

## Expected Output Examples
### Server Start
```
Starting Multi-Skill Agent with skills:
  - Greet (id: hello_world)
  - Get Quote (id: quote)
INFO:     Uvicorn running on http://0.0.0.0:9999
DEBUG: Received message: 'hello'
DEBUG: Routing to greeting agent
```

### Client Interaction
```
MULTI-SKILL AGENT TESTER
Choose what to test:
1. Greeting (hello, hi, hey)
2. Quote/Motivation (quote, inspire, motivate)
3. Custom message
4. Run all tests
5. Exit
```
