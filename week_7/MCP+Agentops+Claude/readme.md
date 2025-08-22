step 1

create folder 
> Documents > agentops_mcp

cd agentops_mcp > create .env

```
AGENTOPS_API_KEY=your_key

```

cd agentops_mcp >python trace_demo.py

<img width="1575" height="131" alt="image" src="https://github.com/user-attachments/assets/53a8ac1e-7e62-445b-88d1-2c4015f2aba9" />


# now your Turn

edit claude_config.json

```
{
  "mcpServers": {
    "agentops": {
      "command": "npx",
      "args": [
        "agentops-mcp"
      ],
      "env": {
        "AGENTOPS_API_KEY": "${AGENTOPS_API_KEY}"
      }
    },
    "calculator-server": {
      "command": "python",
      "args": [
        "C:/Users/HP/Documents/agentops/trace_demo.py"
      ]
    }
  }
}

```

test this on claude.

and once done then trace on Agentops.



