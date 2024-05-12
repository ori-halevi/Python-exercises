class Mammals(object):
    def __init__(self, suction_time: int):
        self.suction_time = suction_time


class Cat(Mammals):
    def says(self):
        return "meow"

class Dog(Mammals):
    def says(self):
        return "woof"



