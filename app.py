from lib.database_connection import DatabaseConnection
from lib.ProductRepo import *

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

        
        


Trial=Application()
Trial.return_all_products()
Trial.check_stock_level('Diamonds')