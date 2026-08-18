from llm_client import ollama_llm, llm_with_tools
from states import OverallState, IntentState


def classify_intent(state: OverallState) -> IntentState:
    messages = [{"role": "system",
                 "content": "You classify customer requests. Return exactly one of: FAQ, ORDER, REFUND. Do not provide an explanation."}]
    messages = messages + state["messages"]
    ai_content = ollama_llm.invoke(messages).content
    return {"request_type": ai_content}


def route_request(state: IntentState):
    state = state["request_type"]
    return state


def order_handler(state: OverallState):
    response = llm_with_tools.invoke(state["messages"])
    return {"messages": [response]}


def faq_handler(state):
    print("FAQ Handler")
    return {}


def refund_handler(state):
    print("Refund Handler")
    return {}
