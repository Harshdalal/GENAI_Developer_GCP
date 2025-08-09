import re
import os
from typing import TypedDict, Literal
from dotenv import load_dotenv

from langgraph.graph import StateGraph, START, END
from langchain.prompts import PromptTemplate
from langchain_core.tools import tool
import google.generativeai as genai

# Load environment variables from .env
load_dotenv()
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

# Configure Gemini
genai.configure(api_key=GOOGLE_API_KEY)


class GeminiLLM:
    def __init__(self, model_name="gemini-1.5-flash"):
        self.model = genai.GenerativeModel(model_name)

    def invoke(self, prompt: str):
        try:
            response = self.model.generate_content(prompt)
            return type("GeminiResponse", (object,), {"content": response.text})()
        except Exception as e:
            return type("GeminiResponse", (object,), {"content": f"Error: {str(e)}"})()

# Initialize Gemini model
llm = GeminiLLM()

# Define the state
class IntermediateState(TypedDict, total=False):
    query: str
    tool_decision: str
    tool_output: str
    final_answer: str
    retry_count: int

# Tool: Calculator
@tool
def calculator(expression: str) -> str:
    """Evaluates a mathematical expression."""
    try:
        return str(eval(expression, {"__builtins__": {}}, {}))  # Safe-ish eval
    except Exception as e:
        return f"Error: {str(e)}"

# Agent node to decide tool
def agent_node(state: IntermediateState) -> IntermediateState:
    print(f"Agent Node: Received state: {state}")
    prompt = PromptTemplate(
        input_variables=["query"],
        template="Decide which tool to use for this query: {query}. Return 'calculator' for math queries or 'llm' for general knowledge."
    )
    tool_decision = llm.invoke(prompt.format(query=state["query"])).content.strip().lower()
    print(f"Agent Node: Decided tool: {tool_decision}")
    return {**state, "tool_decision": tool_decision}

# Calculator node
def calculator_node(state: IntermediateState) -> IntermediateState:
    print(f"Calculator Node: Received state: {state}")
    query = state["query"]
    match = re.search(r"(\d+\s*[\+\-\*/]\s*\d+)", query)
    if match:
        expression = match.group(1)
        print(f"Calculator Node: Extracted expression: {expression}")
        result = calculator.invoke(expression)
    else:
        result = "Error: Could not extract a valid mathematical expression."
    return {**state, "tool_output": result}

# LLM node
def llm_node(state: IntermediateState) -> IntermediateState:
    print(f"LLM Node: Received state: {state}")
    prompt = PromptTemplate(
        input_variables=["query"],
        template="Answer the following question: {query}"
    )
    try:
        response = llm.invoke(prompt.format(query=state["query"]))
        result = response.content.strip() if hasattr(response, "content") else str(response)
    except Exception as e:
        result = f"Error in LLM invocation: {str(e)}"
    return {**state, "tool_output": result}

# Verifier node
def verifier_node(state: IntermediateState) -> IntermediateState:
    print(f"Verifier Node: Received state: {state}")
    prompt = PromptTemplate(
        input_variables=["query", "tool_output"],
        template="Verify if the answer to '{query}' is correct: {tool_output}. If correct, provide the final answer. If incorrect, indicate 'retry'."
    )
    verification = llm.invoke(prompt.format(query=state["query"], tool_output=state["tool_output"])).content.strip().lower()
    retry_count = state.get("retry_count", 0)
    if "retry" in verification:
        return {**state, "retry_count": retry_count + 1}
    return {**state, "final_answer": state["tool_output"]}

# Route to calculator or llm
def route_tool(state: IntermediateState) -> Literal["calculator_node", "llm_node"]:
    tool = state["tool_decision"]
    return "calculator_node" if tool == "calculator" else "llm_node"

# Conditional retry or finish
def route_verifier(state: IntermediateState) -> Literal["calculator_node", "llm_node", END]:
    if "final_answer" not in state or not state["final_answer"]:
        if state.get("retry_count", 0) < 3:
            return route_tool(state)
    return END

# Build the graph
builder = StateGraph(IntermediateState)
builder.add_node("agent_node", agent_node)
builder.add_node("calculator_node", calculator_node)
builder.add_node("llm_node", llm_node)
builder.add_node("verifier_node", verifier_node)

builder.add_edge(START, "agent_node")
builder.add_conditional_edges("agent_node", route_tool)
builder.add_edge("calculator_node", "verifier_node")
builder.add_edge("llm_node", "verifier_node")
builder.add_conditional_edges("verifier_node", route_verifier)

graph = builder.compile()

# Run the graph with test queries
queries = [
    "What is 7 * 4?",
    "Who won the Nobel Peace Prize in 2020?"
]

for query in queries:
    print("\n===============================")
    input_state = {"query": query, "retry_count": 0}
    result = graph.invoke(input_state)
    print(f"User Query: {result['query']}")
    print(f"Final Answer: {result.get('final_answer', 'No answer')}")
