class Stock:
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price
    
    def cost(self):
        return self.shares * self.price
    
    def sell(self, amount):
        self.shares -= amount
        return self.shares
    

class MyStock(Stock):
    def __init__(self, name, shares, factor):
        super().__init__(name, shares)
        self.factor = factor
    
    def panic(self):
        self.sell(self.shares)
        
    def cost(self):
        return 1.25 * self.shares * self.price
    
    def cost2(self):
        return super().cost()