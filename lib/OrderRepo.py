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
        
        if rows == []:
            print(f"No record found with given order id.")
            return None 
        
        items_ordered = []
        count_dict = {}
        
        for row in rows:
            items_ordered.append(row["name"])
            if row["name"] not in count_dict:
                count_dict[row["name"]] = 1
            else:
                count_dict[row["name"]] += 1

        order = OrderClass(order_id, rows[0]["customer_name"], rows[0]["order_date"], items_ordered )

        print(f"Order Number: {order.id}")
        print(f"Customer Name: {order.customer_name}")
        print(f"Order Placed: {order.order_date.strftime('%d-%m-%Y')}")
        print(f"Ordered:")
        for item in count_dict:
            print(f"- {count_dict[item]}x {item}")

    def create_order(self, customer_name, order_date):
        self.connection.execute('INSERT INTO orders (customer_name, order_date) VALUES (%s, %s)', [customer_name, order_date])
        order_id_dict = self.connection.execute('SELECT id from products where id = (SELECT max(id) from products)')
        return order_id_dict[0]["id"]

    def add_product_to_order(self, order_id, product_id):
        self.connection.execute('INSERT INTO orders_products (order_id,product_id) VALUES (%s, %s)', [order_id, product_id])
    
        

        




