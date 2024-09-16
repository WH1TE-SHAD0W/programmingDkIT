from datetime import datetime

from pizza import Pizza
from typing import List


class Order:
    def __init__(self):
        self.date_created = datetime.date(datetime.now())
        self.pizzas = []

    def show_date(self):
        return self.date_created

    def show_pizzas(self):
        return self.pizzas

    def add_pizza(self, pizza: Pizza) -> None:
        self.pizzas.append(pizza)

    def total_bill(self):
        total_bill = 0
        for pizza in self.pizzas:
            total_bill += pizza.calc_price()
        return total_bill

    def most_expensive_pizza(self):
        return max(self.pizzas, key=lambda pizza: pizza.calc_price())

