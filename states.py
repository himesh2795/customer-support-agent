from typing import TypedDict



class OverallState(TypedDict):
    messages: list
    request_type: str

class IntentState(TypedDict):
    request_type: str