import os
from dotenv import load_dotenv
from google import genai

from app.rag import retrieve
from app.tools import bmi_calculator

# Load environment
load_dotenv()

# Initialize Gemini client
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

# Model configuration
MODEL_NAME = "models/gemini-2.5-flash-lite"


# Memory Node
def memory_node(state):
    messages = state.get("messages", [])
    messages.append(state["question"])

    state["messages"] = messages[-6:]
    return state


# Router Node
def router_node(state):
    question = state["question"]

    prompt = f"""
Decide route:

retrieve → for diet, diseases, food
tool → for BMI, calculations
skip → for casual chat

Return ONLY one word.

Question: {question}
"""

    response = client.models.generate_content(
        model=MODEL_NAME,
        contents=prompt
    )

    route = response.text.strip().lower()

    if route not in ["retrieve", "tool", "skip"]:
        route = "retrieve"

    state["route"] = route
    return state


# Retrieval Node
def retrieval_node(state):
    results = retrieve(state["question"])

    docs = results["documents"][0]
    state["retrieved"] = "\n".join(docs)

    return state


# Skip Node
def skip_node(state):
    state["retrieved"] = ""
    state["sources"] = []
    return state


# Tool Node
def tool_node(state):
    result = bmi_calculator(70, 1.75)
    state["tool_result"] = result
    return state


# Answer Node
def answer_node(state):
    prompt = f"""
You are a health assistant.

Rules:
- Give a clear, short, structured answer
- Do NOT repeat information
- Summarize the key points
- Use bullet points if helpful
- Answer ONLY from context
- If answer not found → say "I don't know"

Context:
{state.get('retrieved', '')}

Question:
{state['question']}
"""

    response = client.models.generate_content(
        model=MODEL_NAME,
        contents=prompt
    )

    state["answer"] = response.text
    return state


# Eval Node
def eval_node(state):
    prompt = f"""
Rate the faithfulness of this answer based ONLY on the context.

Context:
{state.get('retrieved', '')}

Answer:
{state.get('answer', '')}

Give a score between 0 and 1 only.
"""

    response = client.models.generate_content(
        model=MODEL_NAME,
        contents=prompt
    )

    try:
        score = float(response.text.strip())
    except:
        score = 0.5

    state["faithfulness"] = score
    state["eval_retries"] = state.get("eval_retries", 0) + 1

    return state


# Save Node
def save_node(state):
    messages = state.get("messages", [])
    messages.append(state["answer"])
    state["messages"] = messages

    return state