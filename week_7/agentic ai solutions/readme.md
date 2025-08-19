# Visualizing the LangGraph

```
from IPython.display import Image, display

try:
    display(Image(graph.get_graph().draw_mermaid_png()))
except Exception:
    # You can put your exception handling code here
    pass
```
# Network Patterns

<img width="1600" height="836" alt="image" src="https://github.com/user-attachments/assets/bc4d3f5e-458e-4428-bc05-27bacf57dc12" />

# test network Pattern

<img width="1239" height="882" alt="image" src="https://github.com/user-attachments/assets/f69bfb05-aab0-43a8-8374-dd3ba8a94fd1" />

# sequential Pattern

<img width="1239" height="882" alt="image" src="https://github.com/user-attachments/assets/d31c37a3-fedf-4f64-a4ed-47fb7aa3bb87" />


# Hub Pattern with Stateless Tool

Hub Pattern is a multi-agent coordination strategy used in Agentic AI / LangGraph setups.

Think of it as a central hub (manager) that connects multiple spokes (tools or agents).

The hub does routing: it decides which tool/agent to call based on the request.

It does not hold complex state itself; instead, it just forwards inputs/outputs.

# Stateless Tool

A stateless tool does not remember past interactions or context.

It processes only the current input → output, without depending on history.

Example: A calculator tool (you give 2+2, it gives 4 — no memory of the previous question).

# ✅ Hub Pattern with Stateless Tool

When combined:

1.The Hub Agent gets a user query.

2.It decides which stateless tool is appropriate.

3.Forwards the query → tool → gets result → returns to user.

This pattern is good when:

1.You have multiple specialized tools (calculator, weather, database search).

2.You don’t need tools to remember history, just compute results.

3.You want a central router managing all tool usage.

# 👉 In short:
Hub Pattern with Stateless Tool = A central router agent that picks and calls external tools (without memory) for task completion.
