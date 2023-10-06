from lib.database_connection import DatabaseConnection
from lib.ProductRepo import *
from lib.OrderRepo import *

class Application():
    def __init__(self):
        # Connects to the Database
        self._connection = DatabaseConnection()
        self._connection.connect()

    def return_all_products(self):
        product_repo = ProductRepo(self._connection)
        print ("Here's a list of all products:")
        for product in product_repo.all():
            print (f'* {product.name} - {product.unit_price} - {product.quantity}')

    def create_item(self,name,unit_price,quantity):
        product_repo = ProductRepo(self._connection)
        product_repo.create(name,unit_price,quantity)

    def check_stock_level(self,name):
        product_repo = ProductRepo(self._connection)
        product_repo.check_quantity(name)

    def check_order(self,order_id):
        order_repo = OrderRepo(self._connection)
        order_repo.find_order(order_id)

# Order Number: 5
# Customer Name: Ned Stark
# Order Placed: 10/01/2023
# Ordered: 
# 1X Baked Beans
# 5X Diamonds
        
# Ned Stark - Placed on - Order Number

Trial=Application()
Trial.check_order(2)