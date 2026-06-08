"""LangGraph supervisor with specialized sub-agents."""
from langgraph.graph import StateGraph, END
from langgraph.prebuilt import ToolNode
from langchain_google_vertexai import ChatVertexAI
from typing import TypedDict, Annotated, List
import operator

AGENTS = ["researcher", "coder", "analyst", "writer", "sql_expert", "scraper"]

class SupervisorState(TypedDict):
    messages: Annotated[list, operator.add]
    next_agent: str
    task: str
    results: dict

def create_supervisor():
    llm = ChatVertexAI(model_name="gemini-1.5-pro-002")
    graph = StateGraph(SupervisorState)

    def supervisor_node(state):
        system = f"""You are a supervisor routing tasks to: {AGENTS}.
        Analyze the task and decide which agent(s) to call next.
        Respond with just the agent name or FINISH."""
        response = llm.invoke(system + f"\nTask: {state['task']}\nResults so far: {state['results']}")
        next_agent = response.content.strip().lower()
        return {**state, "next_agent": next_agent}

    def route(state): return END if state["next_agent"] == "finish" else state["next_agent"]

    graph.add_node("supervisor", supervisor_node)
    for agent in AGENTS:
        graph.add_node(agent, lambda s, a=agent: {**s, "results": {**s["results"], a: f"Result from {a}"}})
        graph.add_edge(agent, "supervisor")
    graph.set_entry_point("supervisor")
    graph.add_conditional_edges("supervisor", route, {a: a for a in AGENTS} | {END: END})
    return graph.compile()
