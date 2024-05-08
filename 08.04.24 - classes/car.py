class Engine(object):
    def __init__(self, sn):
        self.sn = sn

class Car(object):
    def __init__(self, engine: str, sn: int):
        self.engine = engine
        self.sn = sn

    def print(self):
        print("Engine sn:", self.engine)
        print("sn:", self.sn)

    def install_engine(self, engine: Engine):
        self.engine = engine


e1 = Engine("123")
car1 = Car("yoko", 32)
car1.install_engine(e1)
print(car1.print())
