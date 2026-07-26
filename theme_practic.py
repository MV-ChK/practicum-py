# Числа Фибоначчи — это последовательность чисел, где первые два числа — это 0 и 1,
# а каждое последующее число вычисляется как сумма двух предыдущих. 
# Например, вот первые шесть чисел последовательности Фибоначчи:
# 0, 1, 1, 2, 3, 5 
# Напишите функцию-генератор fibonacci(n), которая вычисляет элементы последовательности Фибоначчи до n-ого числа.



def fibonacci(n):
    
    # a = 0
    # b = 1
    # for i in range(n):
    #     yield a
    #     current = a
    #     a = b
    #     b = current + b

    fib_list = [0, 1]
    c = 0
    while c < n:
        
        if len(fib_list) == 2:
            yield 0; c += 1
            yield 1; c += 1
            
        temp_x = fib_list[-1] + fib_list[-2]
        fib_list.append(temp_x)
        yield temp_x; c += 1


sequence = fibonacci(12)
for number in sequence:
    print(number)