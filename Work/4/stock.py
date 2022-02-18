from unicodedata import name


class Stock:
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price
        
    def cost(self):
        return self.shares * self.price
    
    def sell(self, amt):
        self.shares -= amt