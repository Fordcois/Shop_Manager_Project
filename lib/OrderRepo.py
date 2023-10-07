from lib.orderclass import *
import datetime


class OrderRepo:
    def __init__(self,connection):
        self.connection=connection
    
    def all(self):
        rows = self.connection.execute('SELECT * from orders')
        Orders = []
        for row in rows:
            Order = OrderClass(row["id"], row["customer_name"], row["order_date"])
            Orders.append(Order)
        return Orders
    

    def find_order(self,order_id):
        rows = self.connection.execute('SELECT orders.customer_name,orders.order_date,products.name FROM orders_products JOIN orders ON orders_products.order_id = orders.id JOIN products ON orders_products.product_id = products.id where order_id = %s',[order_id])
        # products = []
        # for row in rows:
        #     product = Product(row["id"], row["name"], row["unit_price"],row["quantity"])
        #     products.append(product)
        # return products
        print (rows[0]["order_date"].strftime("%d-%m-%Y"))

    