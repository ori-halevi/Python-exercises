class General_minibar(object):
    Hitting_sys = True
    def __init__(self, model_name: str, color: str, is_have_soda: bool,  cooling_sys_watt: int):
        self.model_name = model_name
        self.color = color
        self.is_have_soda = is_have_soda
        self.cooling_sys_watt = Cooling_system(cooling_sys_watt)

    def get_model_name(self):
        return self.model_name

    def get_color(self):
        return self.color

    def get_is_have_soda(self):
        return self.is_have_soda

    def get_cooling_sys_watt(self):
        return self.cooling_sys_watt.get_watt()

class Cooling_system(object):
    def __init__(self, watt: int):
        self.watt = watt

    def get_watt(self):
        return self.watt

class Travel_luggage(object):
    handle = True
    wills = True
    def __init__(self, model_name: str, color: str, length: int, width: int, depth: int):
        self.model_name = model_name
        self.color = color
        self.length = length
        self.width = width
        self.depth = depth



class Maayanot(object):
    store_id = "12123"
    def __init__(self, product: str):
        if product == "minibar":
            self.product = General_minibar("yoto", "blue", False, 16)
        elif product == "luggage":
            self.product = Travel_luggage("GIO", "red", 43, 41, 13)


product_to_buy = Maayanot("minibar")
print(product_to_buy)