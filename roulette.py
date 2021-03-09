from random import randrange

class Roulette:

    def __init__(self):
        self.numbers = []
        for i in range(50):
            color = "red"
            if i%2 == 0 :
                color = "black"
            self.numbers.append({"color": color, "number": i})


    def launch(self):
        number_rand = randrange(50)
        return self.numbers[number_rand]


