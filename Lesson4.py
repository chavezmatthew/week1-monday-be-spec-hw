class Order:
    def __init__(self, meals, table):
        self.meals = meals
        self.table = table
        self.next = None

class Kitchen:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_order (self, meals, table):
        new_order = Order(meals, table)
        if self.head == None:
            self.head = new_order
            self.tail = new_order
        else:
            self.tail.next = new_order
            self.tail = new_order

    def view_orders (self):
        current = self.head
        while current:
            print(f"Table {current.table} orders: {', '.join(current.meals)}")
            current = current.next

    def cook_order(self):
        if self.head == None:
            return "No orders available to cook."
        else:
            removed = self.head
            self.head = removed.next
            return f"Cooked order for Table {removed.table}: {', '.join(removed.meals)}"

orders = Kitchen()


orders.add_order(["Hamburger", "Steak"], 3)
orders.add_order(["Soup", "Salad"], 4)
orders.add_order(["Fish", "Chicken"], 5)

print("*****Viewing Orders*****")
orders.view_orders()

print("*****Cooking Order*****")
print(orders.cook_order())

print("*****Viewing Remaining Orders*****")
orders.view_orders()