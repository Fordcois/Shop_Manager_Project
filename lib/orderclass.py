class OrderClass():
    def __init__(self, id, customer_name, order_date,products_ordered=[]):
        self.id = id
        self.customer_name = customer_name
        self.order_date = order_date
        self.products_ordered=products_ordered
    
    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def __repr__(self):
        return f"Order({self.id}, {self.customer_name}, {self.order_date},{self.products_ordered})"