import state_graph_provider
from utils import render_result

graph = state_graph_provider.get_graph()


def test_with_order_id():
    result = graph.invoke({"messages": [{"role": "user", "content": "Where is my order ORD123?"}]})
    render_result(result)


def test_order_info():
    result = graph.invoke({"messages": [
        {"role": "user", "content": "What information do I need to provide if I want help with my order?"}]})
    render_result(result)


def main():
    test_with_order_id()
    test_order_info()


main()
