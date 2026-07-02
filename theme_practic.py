from decimal import Decimal

class Customer:
    def __init__(self, name, discount=10):
        self.name = name

    __discount = 10
        # Добавьте сюда атрибут "скидка" со значением по умолчанию 10.
    def get_price(self, price):
        return round((price - ( (price / 100) * self.__discount) ), 2)

    # Реализуйте методы get_price() и set_discount().

    def set_discount(self, new_discount):
        if (new_discount <= 80) and (new_discount > 0):
            self.__discount = new_discount
        if new_discount > 80:
            self.__discount = 80


customer = Customer("Иван Иванович")
print(customer.get_price(100))
customer.set_discount(19)
print(customer.get_price(1114))