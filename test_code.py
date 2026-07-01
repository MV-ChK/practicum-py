class Phone:

    line_type = 'проводной'

    def __init__(self, dial_type_value):
        self.dial_type = dial_type_value
        # Вот он - защищённый атрибут. Значением будет
        # ID ячейки памяти аргумента dial_type_value.
        self._serial_number = id(dial_type_value)

    def ring(self):
        print('Дзззззыыыыыыыынь!')

    def call(self, phone_number):
        print(f'Звоню по номеру {phone_number}! Тип связи - {self.line_type}.')


class MobilePhone(Phone):
    line_type = 'беспроводной'
    battery_type = 'Li-ion'

    def __init__(self, dial_type_value, network_type):
        self.network_type = network_type
        super().__init__(dial_type_value)

    def ring(self):
        print('Дзынь-дзынь!')

    # Это публичный метод, в котором используется защищённый атрибут.
    # Метод определён в классе-наследнике, защищённые атрибуты можно
    # использовать напрямую в базовом классе и его наследниках.
    def get_info(self):
        print(f'Серийный №: {self._serial_number}, тип: {self.network_type}')
        
        
my_phone = MobilePhone("сенсорный", "LTE")

print(my_phone._serial_number)