from time import sleep

def fibonacci_generator():
    now = 0
    yield now
    nxt = 1
    yield nxt
    while True:
        now += nxt
        yield now 
        nxt += now
        yield nxt

f = fibonacci_generator()

for i in range(10):
    print(next(f))
    
    

# while True:
#     try:
#         sleep(0.5)
#         print(next(f))
#     except KeyboardInterrupt:
#         print('Завершено вычисление')
#         break
        
