from typing import TypedDict

from langgraph.graph import StateGraph, START, END
from llm_client import ollama_llm

class OverallState(TypedDict):
    messages: list
    request_type: str

class IntentState(TypedDict):
    request_type: str

def classify_intent(state: OverallState) -> IntentState:
    messages = [{"role": "system", "content": "You classify customer requests. Return exactly one of: FAQ, ORDER, REFUND. Do not provide an explanation."}]
    messages = messages + state["messages"]
    ai_content = ollama_llm.invoke(messages).content
    return {"request_type": ai_content}

def route_request(state: IntentState):
    state = state["request_type"]
    return state

def order_handler(state):
    print("Order Handler")
    return {}

def faq_handler(state):
    print("FAQ Handler")
    return {}

def refund_handler(state):
    print("Refund Handler")
    return {}

graph = StateGraph(OverallState)
graph.add_node(classify_intent)
graph.add_node(order_handler)
graph.add_node(faq_handler)
graph.add_node(refund_handler)
graph.add_edge(START, "classify_intent")
graph.add_conditional_edges("classify_intent", route_request,
                            {
                                "ORDER": "order_handler",
                                "FAQ": "faq_handler",
                                "REFUND": "refund_handler"
                            })

graph.add_edge("order_handler", END)
graph.add_edge("faq_handler", END)
graph.add_edge("refund_handler", END)
graph = graph.compile()

result = graph.invoke({"messages": [{"role": "user", "content": "Where is my order?"}]})
print("Result : ", result)