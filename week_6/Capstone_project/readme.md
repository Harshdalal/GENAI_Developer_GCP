# 1️⃣ E-commerce Industry Problem Statement
Title: "Intelligent Product Return & Replacement Assistant"

# Context:
An e-commerce company receives thousands of customer queries daily regarding product returns, replacements, refund timelines, and eligibility criteria. The company wants to automate this process using AI agents that can dynamically choose the right tools, persist conversation history, and route queries to specialized nodes based on context.

# Problem Statement:
You are required to design and implement an AI-powered Return & Replacement Assistant that:

1.Uses Gemini API (Free Key) with Google Flash 1.5 or 2.5 model for all reasoning and response generation.

2.Uses LangChain + LangGraph for building and linking execution nodes in the workflow.

3.Implements memory persistence so that if the same customer returns after some time, the assistant can recall past interactions.

4Builds API wrappers (callable as LangChain tools) for:

>Checking return eligibility (via a mock product database API).

>Checking replacement status.

>Calculating estimated refund date.

5.Supports task routing and dynamic tool selection—e.g., if the query is “Where is my refund?”, it should directly trigger the refund date API wrapper, but if it’s “I received the wrong product,” it should trigger the replacement workflow.

6.Integrates with a Streamlit UI so customers can type queries, view agent responses, and track conversation history in a user-friendly interface.

7.Deploys over Docker so the entire solution (LangGraph backend + Streamlit UI) can be run as a containerized application.

# Expected Deliverable:

>A LangGraph agent chain with multiple nodes representing eligibility checks, refund queries, and replacement workflows.

>State persistence so that conversations continue seamlessly.

>Streamlit interface for live interaction with the assistant.

>Dockerized solution with a Dockerfile to run the app end-to-end.

# 2️⃣ Telecommunication Industry Problem Statement
Title: "Smart Telecom Service Troubleshooting Agent"

# Context:
A telecom company receives large volumes of support queries like internet speed issues, billing disputes, prepaid recharge problems, and service activation requests. The current chatbot often fails to route the problem to the right support flow. The company needs an agent-based AI system that can handle multiple request types intelligently.

# Problem Statement:
You are required to build a Smart Telecom Troubleshooting Agent that:

1.Uses Gemini API (Free Key) with Google Flash 1.5 or 2.5 model.

2.Uses LangChain + LangGraph for designing an execution graph where each node represents a troubleshooting workflow (e.g., internet issues, billing issues, activation requests).

3.Implements memory persistence so if a customer first complains about slow internet and later asks about the same ticket, the agent recalls past conversation details.

4.Builds API wrappers (tools callable by the agent) for:

>Checking network outage in the customer’s area.

>Retrieving last bill details and payments.

>Running an internet speed diagnostic (mock API).

5.Supports task routing and dynamic tool selection—e.g., if the query is “Why is my bill so high?”, route to billing workflow; if “Internet is slow,” route to connectivity troubleshooting.

6.Integrates with a Streamlit UI where customers can submit their queries, view troubleshooting steps, and track progress.

7.Deploys over Docker to ensure the agent can run as a containerized application across different environments.

Expected Deliverable:

>A LangGraph-based agent workflow with multiple tool-enabled nodes.

>Dynamic routing based on query classification.

>Persistent state storage so follow-up queries maintain context.

>Streamlit interface for customer interaction.

>Dockerized setup with a Dockerfile for deployment.
