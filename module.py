class Cars:
    def __init__(self, brand, color, transmission):
        self.brand = brand
        self.color = color
        self.transmission = transmission

    def show(self):
        print(self.brand, self.color, self.transmission)


class Laptops:
    def __init__(self, brand, cpu, memory):
        self.brand = brand
        self.cpu = cpu
        self.memory = memory

    def show(self):
        print(self.brand, self.cpu, self.memory)
