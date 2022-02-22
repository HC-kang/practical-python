class Stock:
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price
        
    def cost(self):
        return self.shares * self.price
    
class Child(Stock):
    def __init__(self, name, shares, price, hi):
        super().__init__(name, shares, price)
        self.hi = hi

s = Stock('Goog', 100, 111.1)
s.hi = 'hello'
s.__dict__
s.__bases__

c = Child('never', 100, 11.1, 'hi')

c.__dict__
c.__mro__


class A:
    pass

class B:
    pass

class C(A, B):
    pass

c = C()

c.__bases__

goog = Stock('GOOG', 100, 490.1)
ibm = Stock('IBM', 50, 91.23)

goog.__dict__
goog.date = '6/11/2007'
goog.__dict__

goog.__dict__['hello'] = '???'
goog.__dict__
goog.hello

Stock.__dict__['cost'](goog)

Stock.foo = 42

goog.foo = 24
goog.foo
del(goog.foo)
ibm.foo


class Foo(object):
    a = 13
    def __init__(self, b):
        self.b = b
        
f = Foo(10)
g = Foo(20)

f.a
g.a

f.b
g.b

Foo.a = 42
f.a
Foo.a
g.a
f.b
g.b

class Stock():
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price
    
    def cost(self):
        return self.shares * self.price
    
    def sell(self, amount):
        self.shares -= amount

s = Stock('Goog', 100, 1.1)

s.shares
s.sell(10)
s.shares
s.__dict__
s.__bases__

h = s.sell
h
h(10)
s.__dict__


words = 'hello!!'
k = words.replace
k.

words

words.replace('!', '?')

words

class NewStock(Stock):
    def yow(self):
        print('Yow!')
        
n = NewStock('ACME', 50, 123.45)

n.cost()
n.yow()

NewStock.__bases__

NewStock.__mro__

for cls in n.__class__.__mro__:
    if 'cost' in cls.__dict__:
        break
    
cls

cls.__dict__['cost'](n)