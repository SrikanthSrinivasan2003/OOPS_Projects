class Cart:
    def __init__(self):
        self.items = {}
        self.price_list = {"Book": 100, "Laptop": 50000, "Mobile": 15000}

    def add_item(self, item_name,quantity):
        self.items[item_name] = quantity

    def remove_item(self, item_name):
        del self.items[item_name]

    def update_cart(self,item_name,quantity):
        self.items[item_name] = quantity

    def show_cart(self):
        cart_items = list(self.items.keys())
        return cart_items
        
    def show_bill(self):
        result = 0
        for item_name, quantity in self.items.items():
            result += quantity * self.price_list[item_name]
        return result


cart_obj = Cart()
cart_obj.add_item("Laptop", 2)
cart_obj.add_item("Book", 5)
output = cart_obj.show_cart()
cart_obj.remove_item("Laptop")
cart_obj.add_item("Mobile", 2)
money = cart_obj.show_bill()
print(money)
cart_obj.add_item("Laptop", 1)
op = cart_obj.show_bill()
print(op)
