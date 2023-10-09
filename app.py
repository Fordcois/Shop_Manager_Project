from lib.database_connection import DatabaseConnection
from lib.ProductRepo import *
from lib.OrderRepo import *
import re

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
        print ("Here's a list of all orders:")
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

    def create_new_order(self, customer_name, order_date):
        order_repo = OrderRepo(self._connection)
        print(f'New Order for {customer_name} placed on {order_date}')
        return order_repo.create_order(customer_name, order_date)

    def add_product_to_order(self, order_id, product_id):
        order_repo = OrderRepo(self._connection)
        order_repo.add_product_to_order(order_id, product_id)
    
    def call_on_id(self,product_id):
        product_repo = ProductRepo (self._connection)
        ItemName = product_repo.get_name_from_id(product_id)
        if ItemName == []:
            return None
        else:
            return ItemName[0]['name']
        
#    User Interface below 
    def run_user_interface(self):
        print (self.dots)
        print ('Welcome to the Shop Management System'.center(75))
        print (self.dots)
        print ('* [1] - View all products and current stock')
        print ('* [2] - View all current orders')
        print ('* [3] - Check stock level of specific item')
        print ('* [4] - Add a new item')
        print ('* [5] - Check order')
        print ('* [6] - Create new order')

        FeatureSelected = input('What would you like to do today?: ')
        print (self.dots)
        # Checks input is valid
        if FeatureSelected not in ['1','2','3','4', '5','6']:
            print (f' {FeatureSelected} is not a valid input - Goodbye')
        
        # Return all the Products
        elif FeatureSelected == '1':
            self.return_all_products()

        # Views all Current Orders
        elif FeatureSelected == '2':
            self.return_all_orders()

        # Takes an input then runs a check stock using that variable
        elif FeatureSelected == '3':
            SearchRequest = input('What item would you like to check on? : ')
            print (self.dots)
            self.check_stock_level(SearchRequest)
        
        # Add new item - Talks you through each input then runs command
        elif FeatureSelected == '4':
            print ("What's the name of the product you'd like to add?")
            name = input('Product Name: ')
            print ("What's the unit price of the product you'd like to add? (Format: 00.00)")
            unit_price = input('Unit Price: £')
            print ("What's the quantity of the item?")
            quantity = input('Quantity: ')
            self.create_item(name,unit_price,quantity)
            print (f'{quantity} {name} added at a unit price of £{unit_price} Each')

        # Check a Preexisting Order
        elif FeatureSelected == '5':
            print ("What order number would you like to check?")
            order_to_check = input('Order number: ')
            print (self.dots)
            self.check_order(order_to_check)
        # Create a new Order
        elif FeatureSelected == '6':
#           Takes name for new order
            print (f"What's the Customer Name?")
            CustomerName = input('Name: ')

#           Takes a Date - Makes sure it is in the correct format before proceeding:
            print (f"What's the date of the order? (Format YYYY-MM-DD)")
            OrderDate = input('Date: ')
            date_pattern = re.compile(r'^\d{4}-\d{2}-\d{2}$')
            if date_pattern.match(OrderDate) == None:
                print (f"'{OrderDate}' is not a valid date format - Please start again using the format YYYY-MM-DD")
                return None
            print (self.dots)
            NewOrderID=self.create_new_order(CustomerName,OrderDate)
#           Loop of adding items to order before confirming
            OrderIncomplete = True
            print (f"Enter the Product ID of the item you would like to add to {CustomerName}'s Order")
            print ("Enter 'DONE' When you're finished")
            while OrderIncomplete == True:
                CustomerInput=input('Enter Input: ')

                if CustomerInput.upper() == 'DONE':
                    OrderIncomplete = False

                else:
                    ItemToAdd=self.call_on_id(int(CustomerInput))
                    if ItemToAdd == None:
                        print (f'No Such product with ID {CustomerInput}')
                    else:
                        self.add_product_to_order(NewOrderID,int(CustomerInput))
                        print (f"Added 1x {ItemToAdd} to {CustomerName}'s order")
                        print (f"Enter another product ID to add to order or enter DONE when you've finished")


            print (self.dots)
            print ('Order Confirmed'.center(75))
            print (self.dots)
            self.check_order(NewOrderID)

if __name__ == '__main__':
    app = Application()
    app.run()
