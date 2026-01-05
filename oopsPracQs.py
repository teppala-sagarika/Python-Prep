#Create a Product Store - name, price
#Track Total Products Being Created
#Create a static method - to calc discount on product based on % parameter

class Product:
    tot=0
    @classmethod
    def trackTot(cls):
        cls.tot+=1

    def __init__(self,name,price):
        self.name=name
        self.price=price
        Product.trackTot()

    @staticmethod
    def calcDiscount(price,percent):
        print(price-(percent*price/100))

prod1=Product("laptop",80_000)
prod2=Product("mobile",58000)
print(prod1.name,prod2.name)
print("Total Products:", Product.tot)
Product.calcDiscount(prod1.price,15)
Product.calcDiscount(prod2.price,5)

