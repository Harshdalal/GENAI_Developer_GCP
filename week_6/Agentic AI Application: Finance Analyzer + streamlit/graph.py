
import os
from dotenv import load_dotenv
from typing import TypedDict
from langchain_google_genai import ChatGoogleGenerativeAI
from langgraph.graph import StateGraph, END
from langchain_core.messages import HumanMessage
from langchain_core.runnables import RunnableLambda

load_dotenv()
llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash", google_api_key=os.getenv("GOOGLE_API_KEY"))

class GraphState(TypedDict):
    input: str
    trend: str
    risk: str
    report: str

def trend_analysis(state: GraphState):
    prompt = f"Analyze financial trend from this input:\n{state['input']}\nFocus on market trends, sectors, or sentiment."
    result = llm.invoke([HumanMessage(content=prompt)])
    return {"trend": result.content.strip()}

def risk_analysis(state: GraphState):
    prompt = f"Identify financial risks from the following input:\n{state['input']}\nMention economic, policy, or investment risks."
    result = llm.invoke([HumanMessage(content=prompt)])
    return {"risk": result.content.strip()}

def report_generation(state: GraphState):
    return {
        "report": f"""📈 **Trend Analysis**:\n{state['trend']}\n\n⚠️ **Risk Evaluation**:\n{state['risk']}"""
    }

def build_graph():
    builder = StateGraph(GraphState)

    # Add all nodes
    builder.add_node("Trend", RunnableLambda(trend_analysis))
    builder.add_node("Risk", RunnableLambda(risk_analysis))
    builder.add_node("Report", RunnableLambda(report_generation)

    )

    # Entry point
    builder.set_entry_point("Trend")

    # Chain Trend → Risk → Report → END
    builder.add_edge("Trend", "Risk")
    builder.add_edge("Risk", "Report")
    builder.add_edge("Report", END)

    return builder.compile()
