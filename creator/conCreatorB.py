from .creator import Creator
from product.productB import ConcreteProductB

class ConCreatorB(Creator):

    def createProduct(self,data):
        return ConcreteProductB(data)