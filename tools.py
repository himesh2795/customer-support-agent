from langchain.tools import tool


@tool
def check_order_status(order_id: str):
    """Check the current status of an order using its order ID."""

    # TODO: Connect with real data
    orders = {
        "ORD123": "Shipped",
        "ORD456": "Delivered",
        "ORD789": "Processing"
    }

    return orders.get(order_id, "Order not found")