# Импортируйте необходимые модули.
from datetime import datetime 
# Укажите два параметра функции:
def validate_record(name, date_str):
    # Напишите код, верните булево значение.
    try:
        date_obj = datetime.strptime(date_str, '%d.%m.%Y').date()
    except ValueError:
        print(f'Некорректный формат даты в записи: {name}, {date_str}')
        return False 
    else:
        return True

# Укажите параметры функции:
def process_people(data):
    # Объявите счётчики.
    good_count = 0
    bad_count = 0
    # в каждой паре значений из списка data
    # проверьте корректность формата даты рождения
    # и в зависимости от результата проверки увеличьте один из счётчиков.    
    for inf in data:
        if validate_record(*inf):
            good_count += 1
        else:
            bad_count += 1
    return {'good': good_count, 'bad': bad_count}


data = [
    ('Акакий Башмачкинъ',    '23 марта 1791 года'),
    ('Яков Степанов', 'Двадцать шестое июля 1971'),
    ('Потап Алексеев', '16.09.1990'),
    ('Евгений Женин', '5 декабря 1984'),
    ('Кондрат Александров', '18.01.1994')
] 
statistics = process_people(data)

print(f"Корректных записей: {statistics['good']}")
print(f"Некорректных записей: {statistics['bad']}")
