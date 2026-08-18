from langgraph.graph import StateGraph, START, END
from langgraph.prebuilt import tools_condition

from handlers import classify_intent, order_handler, faq_handler, refund_handler, route_request
from llm_client import tool_node
from states import OverallState


def get_graph():
    graph = StateGraph(OverallState)
    graph.add_node(classify_intent)
    graph.add_node(order_handler)
    graph.add_node(faq_handler)
    graph.add_node(refund_handler)
    graph.add_node("my_tools", tool_node)
    # graph.add_node("tools", tool_node) # the default name

    graph.add_edge(START, "classify_intent")
    graph.add_conditional_edges("classify_intent", route_request,
                                {
                                    "ORDER": "order_handler",
                                    "FAQ": "faq_handler",
                                    "REFUND": "refund_handler"
                                })

    # graph.add_edge("order_handler", END)

    ## To work with default given name for tools .i.e "tools"
    # graph.add_conditional_edges("order_handler", tools_condition) # works with default added node with name "tools"
    # graph.add_edge("tools", "order_handler")

    ## for custom given name in the node
    graph.add_conditional_edges("order_handler", tools_condition, {
        "tools": "my_tools", END: END
    })
    graph.add_edge("my_tools", "order_handler")

    graph.add_edge("faq_handler", END)
    graph.add_edge("refund_handler", END)
    graph = graph.compile()
    return graph
