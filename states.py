from typing import TypedDict, Annotated
from langgraph.graph.message import add_messages


class OverallState(TypedDict):
    messages: Annotated[list, add_messages]
    request_type: str

class IntentState(TypedDict):
    request_type: str