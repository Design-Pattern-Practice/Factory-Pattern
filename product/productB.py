from .product import Product

class ConcreteProductB(Product):

    def __init__(self,data):
        self.data = data 

    def show(self):
        print("This is product B with square of data :",self.data*self.data)