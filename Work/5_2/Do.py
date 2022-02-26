class Person:
    def __init__(self, name):
        self._name = name
        
p = Person('Guido')

p._name

p._name = 'Dave'
p._name

class Stock:
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price
        
s = Stock('IBM', 50, 91.1)

s.shares
s.name
s.price

s.shares = '100'
s.shares

class Stock:
    def __init__(self, name, shares, price):
        self.name = name
        self.set_shares(shares)
        self.price = price
        
    def get_shares(self):
        return self._shares
    
    def set_shares(self, value):
        if not isinstance(value, int):
            raise TypeError('Expected an int')
        self._shares = value
        
        
s = Stock('IBM', 100, 19.19)
s.shares = 10
s.__dict__
s.get_shares()


class Stock:
    def __init__(self, name, shares, price):
        self.name = name
        self._shares = shares
        self.price = price
        
    @property
    def cost(self):
        return self._shares * self.price
    
    @property
    def shares(self):
        return self._shares
    
    @shares.setter
    def shares(self, value):
        if not isinstance(value, int):
            raise TypeError('Expected int')
        self._shares = value
        
    @shares.getter
    def shares(self):
        return self._shares
        
s = Stock('IBM', '100', 19.19)
s = Stock('IBM', 100, 19.19)
s.__dict__
s._shares
s.shares = 10
s.shares
s._shares
s.__dict__

s.cost


class Stock:
    __slots__ = ('name', '_shares', 'price')
    def __init__(self, name, shares, price):
        self.name = name
        self._shares = shares
        self.price = price
    
    @property
    def cost(self):
        return self._shares * self.price
    
    @property
    def shares(self):
        return self._shares
        
    @shares.setter
    def shares(self, value):
        if not isinstance(value, int):
            raise TypeError('Expected int')
        self._shares = value
    
s = Stock('IG', 100, 1.1)

s.__dict__
s.n = 10
s.name
s.shares
s._shares
s.price



from stock import Stock

s = Stock('G', 100, 490.1)
s.shares = 50
s.shares
s.shares = 'lot'

s.ss = 1

