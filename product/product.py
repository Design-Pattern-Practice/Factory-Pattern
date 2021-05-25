from abc import ABC, abstractmethod

class Product(ABC):
    
    @abstractmethod
    def show(self,data):
        pass