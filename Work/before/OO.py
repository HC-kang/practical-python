nums = [1, 2, 3]

nums.append(4)

nums

nums.insert(1, 10)

nums


class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.health = 100
        
    def move(self, dx, dy):
        self.x += dx
        self.y += dy
        
    def damage(self, pts):
        self.health -= pts
        
a = Player(2, 3)
b = Player(10, 20)
a.x