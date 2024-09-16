from datetime import datetime, date
from typing import Type
from orders import Orders
from pizza import Pizza
from order import Order


def order_pizza() -> Order:
    name = input('What name of a pizza you want?')
    size = input('What size of a pizza you want?')
    while not Pizza.validate_size(size):
        size = input('Please provide a correct size of the pizza you want, choose from (s, m, l, xl)')

    if input('Do you want any toppings?').lower() == 'yes':
        toppings = input('Write down which toppings you want').lower().split()
        pizza_to_order = Pizza(name, size, toppings)
        the_order = Order()
        the_order.add_pizza(pizza_to_order)
        return the_order
    else:
        pizza_to_order = Pizza(name, size)
        the_order = Order()
        the_order.add_pizza(pizza_to_order)
        return the_order


def menu():
    return ("To order a pizza type: order\n"
            "To edit an order type: edit\n"
            "To finish ordering type: finish\n"
            "To show today order details: show\n"
            )


def edit_menu():
    return "To edit a pizza type the name of the pizza you want"


def edit_today_order(order):
    print('editing')
    # match input(edit_menu()):
    #     case "order":
    #         order_pizza()
    #     case "edit":
    #         edit_menu()
    #     case "finish":
    #         quit()
    #     case _:
    #         pass


def show_details(today_order):
    print('order_details')


def ordering_program(all_orders: Orders):
    while True:
        today = date.today()
        if all_orders.order_at_date(today):
            today_orders = all_orders.order_at_date(today)
        else:
            today_orders = Order()
        match input(menu()):
            case "order":
                order_pizza()
            case "edit":
                if today_orders:
                    edit_today_order(all_orders.order_at_date(today))
                else:
                    print("No pizzas today yet")
            case "show":
                show_details(all_orders.order_at_date(today))

            case "finish":
                all_orders.add_orders(today_orders)
                break
            case _:
                pass


if __name__ == '__main__':
    # margarita = Pizza('margarita', 's')
    # order1 = Order()
    # order1.add_pizza(margarita)
    all_orders = Orders()
    # all_orders.add_orders(order1)
    ordering_program(all_orders)
    # print(order1.show_date())
    # print(all_orders.order_at_date('2024-09-16').show_pizzas())



"""
Imports your Pizza class.
2. Repeatedly asks the user if they want to order a pizza. If they say yes, your program should:
a. Prompt for the size of the pizza to be made
b. Takes in a list of toppings from the user (they do not have to supply any. If they do not, you
should create a pizza with default toppings)
c. Creates a pizza from the user-supplied data
d. Adds the pizza to the user’s order (a list)
3. When the user is finished adding pizzas to their order, your program should:
a. Calculate the cost of each pizza in the user’s order list
# b. Displays the most expensive pizza and its details
# c. Adds up the total bill for the pizzas and informs the user.
"""
