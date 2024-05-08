class Mosaad:
    purpos = "tora"
    def __init__(self, name, people_n, stuff_n):
        self.name = name
        self.people = people_n
        self.stuff = stuff_n

    def set_building(self, address, width, length):
        self.building = Building(address, width, length)

class Building:
    def __init__(self, address, width, length):
        self.addrs = address
        self.x = width
        self.y = length

    def get_sqmt(self):
        return self.x * self.y


class Shul(Mosaad):
    def place_for_guests(self):
        return(self.building.get_sqmt() - self.people)

class Refui(Mosaad):
    purpos = "Health"

Y = Refui
print(Y("asaf", 100, 15).building)

# telz = Mosaad("telz", 844, 50)
# telz.foo("address")
# print(telz.name)
#
# mir = Mosaad("mir", 1000, 100)
# print(mir.purpos)
# print(mir.name)
