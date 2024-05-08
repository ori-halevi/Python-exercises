class Car(object):
    def __init__(self, model_name: str, first_year: int):
        self.model_name = model_name
        self.first_year = first_year


class BMW(Car):
    def __init__(self, first_year):
        super.__init__("BMW", first_year)

ronoen_bmw = BMW(2023)

print(ronoen_bmw)