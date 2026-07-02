from decimal import Decimal

number = 123.19484
round_number = Decimal(str(number)).quantize(Decimal('0.01'))
print(round_number)
