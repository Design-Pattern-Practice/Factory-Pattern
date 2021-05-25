from .product import Product

class ConcreteProductA(Product):

    def __init__(self,data):
        self.data = data 

    def show(self):
        print("This is product A with data:",self.data)