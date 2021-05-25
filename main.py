from creator.conCreatorA import ConCreatorA
from creator.conCreatorB import ConCreatorB

a = ConCreatorA()
b = ConCreatorB()


prodA = a.createProduct(5)
prodB = b.createProduct(5)
prodC = a.createProduct(7)
prodD = b.createProduct(7)


prodA.show()
prodB.show()
prodC.show()
prodD.show()