from lib.productclass import *

class ProductRepo:
    def __init__ (self,connection):
        self.connection=connection

    def all(self):
        rows = self.connection.execute('SELECT * from products')
        products = []
        for row in rows:
            product = Product(row["id"], row["name"], row["unit_price"],row["quantity"])
            products.append(product)
        return products
    
    def create(self,name,unit_price,quantity):
        self.connection.execute('INSERT INTO products (name,unit_price,quantity) VALUES (%s,%s,%s)',[name,unit_price,quantity])
    
    def check_quantity(self,name):
        result = self.connection.execute('SELECT name,quantity from products where name =%s',[name])
        if result == []:
            print (f'No item called {name} found in the system!')
        else:
            print (f'{  result[0]["name"]   } Stock: {  result[0]["quantity"]   }')

    def get_name_from_id(self,product_id):
        result = self.connection.execute('SELECT name from products where id =%s',[product_id])
        return result