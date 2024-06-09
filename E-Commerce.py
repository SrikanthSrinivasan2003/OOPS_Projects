class Product:
    def __init__(self,name,price,deal_price,rating):
        #instance attributes
        self.name = name
        self.price = price
        self.deal_price = deal_price
        self.rating = rating
        self.you_save = price - deal_price
    
    def display_product_details(self):
        print("Name : {}".format(self.name))
        print("Price : {}".format(self.price))
        print("Deal Price : {}".format(self.deal_price))
        print("You Save : {}".format(self.you_save))
        print("Rating : {}".format(self.rating))
        
    def get_deal_price(self):
        return self.deal_price
    
#Inheritance Subclass:ElectronicItem Superclass:Product
class ElectronicItem(Product):
    #method overriding
    def __init__(self,name,price,deal_price,rating,warranty_in_months):
        super().__init__(name,price,deal_price,rating)
        self.warranty_in_months = warranty_in_months
        
    #method overriding
    def display_product_details(self):
        super().display_product_details()
        print("Warranty : {}".format(self.warranty_in_months))
        
class GroceryItem(Product):
    #method overriding
    def __init__(self,name,price,deal_price,rating,expiry_date):
        super().__init__(name,price,deal_price,rating)
        self.expiry_date = expiry_date
        
    #method overriding
    def display_product_details(self):
        super().display_product_details()
        print("Expiry Date : {}".format(self.expiry_date))
        
class Order:
    #class attributes
    delivery_charges = {
        "Prime_Delivery":0,"Normal_delivery":50
    }
    def __init__(self,delivery_type,delivery_address):
        self.delivery_type = delivery_type
        self.delivery_address = delivery_address
        self.items_in_cart = []#list contains(product,quantity)<--- Composition
        
    def add_item(self,product,quantity):
        item = (product,quantity)
        self.items_in_cart.append(item)
        
    def get_total_bill(self):
        total_bill = 0 
        for product,quantity in self.items_in_cart:
            price = product.get_deal_price()*quantity
            total_bill += price 
        order_delivery_charges = Order.get_delivery_charges(self.delivery_type)
        total_bill += order_delivery_charges
        return total_bill
        
    def display_order_details(self):
        print("Order Type : {}".format(self.delivery_type))
        print("Delivery Address : {}".format(self.delivery_address))
        print("-------------------------------")
        for Product,quantity in self.items_in_cart:
            Product.display_product_details()
            print("Quantity : {}".format(quantity))
            print("-------------------------")
        order_delivery_charges = Order.get_delivery_charges(self.delivery_type)
        print("Delivery Charge : {}".format(order_delivery_charges))
        print("Total Bill : {}".format(self.get_total_bill()))
        
    @classmethod
    def get_delivery_charges(cls,delivery_type):
        return cls.delivery_charges[delivery_type]
     
#multiple Inheritance
class Laptop(ElectronicItem):
    def __init__(self,name,price,deal_price,rating,warranty_in_months,ram,os,storage):
        super().__init__(name,price,deal_price,rating,warranty_in_months)
        self.ram = ram
        self.os = os
        self.storage = storage
        
    def display_product_details(self):
        super().display_product_details()
        print("Ram : {}".format(self.ram))
        print("OS : {}".format(self.os))
        print("Storage : {}".format(self.storage))
        
tv = ElectronicItem("Led TV",40000,35000,4.5,24)
keyboard = ElectronicItem("Dell keyboard",1000,750,4,12)
wheat_flour = GroceryItem("wheat_flour",100,90,4,"Jan 2025")
milk = GroceryItem("Milk",25,20,4,"Jan 2024")
Laptop = Laptop("Lenova Idea pad 5",50000,47000,4.5,24,"16GB","Windows","1 TB SSD")

my_order = Order("Normal_delivery","Bangalore")
my_order.add_item(tv,1)
my_order.add_item(keyboard,1)
my_order.add_item(wheat_flour,2)
my_order.add_item(milk,5)
my_order.add_item(Laptop,1)
my_order.display_order_details()
