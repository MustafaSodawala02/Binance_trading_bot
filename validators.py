
def validate_order(order_type, price):
    if order_type in ["LIMIT", "STOP"] and price is None:
        raise ValueError("Price required for LIMIT and STOP orders")
