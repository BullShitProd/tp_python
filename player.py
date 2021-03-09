import math

import math
class Player:
    def __init__(self, name):
        self.sold = 50
        self.name = name

    def removeSold(self, price):
        price = math.ceil(price)
        if self.sold - price >= 0:
            self.sold -= price
        return self.sold

    def addSold(self, price):
        self.sold += math.ceil(price)
        return self.sold