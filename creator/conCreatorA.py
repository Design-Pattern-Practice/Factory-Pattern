from .creator import Creator
from product.productA import ConcreteProductA

class ConCreatorA(Creator):

    def createProduct(self,data):
        return ConcreteProductA(data)