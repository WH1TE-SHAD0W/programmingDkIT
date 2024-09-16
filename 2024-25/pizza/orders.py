from order import Order


class Orders:
    def __init__(self):
        self.orders = []

    def add_order(self, order: Order):
        self.orders.append(order)

    def count_orders(self):
        return len(self.orders)

    def show_orders(self):
        return self.orders