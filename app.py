from lib.database_connection import DatabaseConnection
from lib.ProductRepo import *
from lib.OrderRepo import *

class Application():
    def __init__(self):
        self.dots='*'*75
        # Connects to the Database
        self._connection = DatabaseConnection()
        self._connection.connect()

    def return_all_products(self):
        product_repo = ProductRepo(self._connection)
        print ("Here's a list of all products:")
        print (self.dots)
        for product in product_repo.all():
            print (f'* {product.id} - {product.name} - {product.unit_price} - {product.quantity}')
    
    def return_all_orders(self):
        order_repo = OrderRepo(self._connection)
        print ("Here's a list of all Orders:")
        print (self.dots)
        for order in order_repo.all():
            print (f'* Order Number: {order.id} - Customer Name: {order.customer_name} - Order Placed: {(order.order_date).strftime("%d-%m-%Y")}')

    def create_item(self,name,unit_price,quantity):
        product_repo = ProductRepo(self._connection)
        product_repo.create(name,unit_price,quantity)

    def check_stock_level(self,name):
        product_repo = ProductRepo(self._connection)
        product_repo.check_quantity(name)

    def check_order(self,order_id):
        order_repo = OrderRepo(self._connection)
        order_repo.find_order(order_id)

#    User Interface below 
    def run_user_interface(self):
        print (self.dots)
        print ('Welcome to the Shop Management System'.center(75))
        print (self.dots)
        print ('* [1] - View All Products and Current Stock')
        print ('* [2] - View All Current Orders')
        print ('* [3] - Check Stock Level of specific item')
        print ('* [4] - Add a New Item')
        # - [NeedToImplement] Look-up existing order
        # - [NeedToImplement] Generate a new order


        FeatureSelected=input('What would you like to do today?: ')
        print (self.dots)
        # Checks input is valid
        if FeatureSelected not in ['1','2','3','4']:
            print (f' {FeatureSelected} is not a Valid input - Goodbye')
        
        # Return all the Products
        elif FeatureSelected == '1':
            self.return_all_products()

        # Views all Current Orders
        elif FeatureSelected == '2':
            self.return_all_orders()

        # Takes an input then runs a check stock using that variable
        elif FeatureSelected == '3':
            SearchRequest=input('What item would you like to check on? : ')
            print (self.dots)
            self.check_stock_level(SearchRequest)
        
        # Add new item - Talks you through each input then runs command
        elif FeatureSelected == '4':
            print ("What's the name of the Product you'd like to add?")
            name=input('Product Name: ')
            print ("What's the unit price of the Product you'd like to add? (Format: 00.00)")
            unit_price=input('Unit Price: £')
            print ("What's the quantity of the item?")
            quantity=input('Quantity: ')
            self.create_item(name,unit_price,quantity)
            print (f'{quantity} {name} added at a unit price of £{unit_price} Each')

            
# This is what return a specific Order Should Look Like:
    # Order Number: 5
    # Customer Name: Ned Stark
    # Order Placed: 10/01/2023
    # Ordered: 
    # 1X Baked Beans
    # 5X Diamonds

#-#-#-#-#-#-#-#-#-#-#-#-#-#-#–#-#-#-#-#-#-#-#-#-#–#–#-#-#
#     Commands below here are for testing purposes only
#-#-#-#-#-#-#-#-#-#-#-#-#-#-#–#-#-#-#-#-#-#-#-#-#–#–#-#-#
Trial=Application()
Trial.run_user_interface()
# Trial.check_stock_level('Twigs')
# Trial.check_stock_level('Bread')
# Trial.check_stock_level('Diamonds')
