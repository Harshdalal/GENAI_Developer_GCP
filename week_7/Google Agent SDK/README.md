
# Agent2Agent Project

## Quick Start Steps

### Prerequisites Check
```bash
python --version  # Should be 3.8+
uv --version      # Should be installed
```

### Project Setup
```bash
# Clone and navigate to project in VS Code
open Document Folder
> go to Terminal then 
Select command prompt
    >  uv init agent2agent
    >  cd agent2agent

# Install dependencies
    >  uv sync
    >  pip install a2a-sdk starlette sse-starlette
    >  uv add a2a-sdk[http-server]
    >  uv run . (optinal)


### Test the Agent
```bash
# Terminal 2
> CMD
> cd agent2agent
> uv run --active test_client.py
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
<img width="891" height="341" alt="image" src="https://github.com/user-attachments/assets/691f890e-f5b7-4f91-8c76-7d5e1ef912ca" />

<img width="1101" height="967" alt="image" src="https://github.com/user-attachments/assets/2f0af792-bd18-4cea-871d-9cabce1239d2" />





