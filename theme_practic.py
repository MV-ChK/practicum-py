class Product:

    def __init__(self, name, cnt):
        self.name = name
        self.count = cnt

    def get_info(self):
        return f"{self.name} (в наличии: {self.count})"


class Kettlebell(Product):

    def __init__(self, name, cnt, weight):
        super().__init__(name, cnt)
        self.weight = weight

    def get_weight(self):
        return self.get_info() + f". Вес: {self.weight} кг"


class Clothing(Product):

    def __init__(self, name, cnt, size):
        super().__init__(name, cnt)
        self.size = size

    def get_size(self):
        return self.get_info() + f". Размер: {self.size}"


small_kettlebell = Kettlebell('Гиря малая', 15, 2)
shirt = Clothing('Футболка', 5, 'L')

print(small_kettlebell.get_weight())
print(shirt.get_size())
