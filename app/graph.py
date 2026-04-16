from langgraph.graph import StateGraph
from app.state import State
from app.nodes import (
    memory_node,
    router_node,
    retrieval_node,
    tool_node,
    skip_node,
    answer_node,
    eval_node,
    save_node
)

builder = StateGraph(State)

# Add nodes
builder.add_node("memory", memory_node)
builder.add_node("router", router_node)
builder.add_node("retrieve", retrieval_node)
builder.add_node("tool", tool_node)
builder.add_node("skip", skip_node)
builder.add_node("answer", answer_node)
builder.add_node("eval", eval_node)
builder.add_node("save", save_node)

# Entry point
builder.set_entry_point("memory")

# Basic flow
builder.add_edge("memory", "router")

# Routing
def route_decision(state):
    return state["route"]

builder.add_conditional_edges(
    "router",
    route_decision,
    {
        "retrieve": "retrieve",
        "tool": "tool",
        "skip": "skip"
    }
)

# Continue flow
builder.add_edge("retrieve", "answer")
builder.add_edge("tool", "answer")
builder.add_edge("skip", "answer")

builder.add_edge("answer", "eval")

# Eval loop
def eval_decision(state):
    if state.get("faithfulness", 1) < 0.7 and state.get("eval_retries", 0) < 2:
        return "answer"
    return "save"

builder.add_conditional_edges(
    "eval",
    eval_decision,
    {
        "answer": "answer",
        "save": "save"
    }
)

builder.add_edge("save", "__end__")

graph = builder.compile()