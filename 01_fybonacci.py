"""
Реалізуйте функцію caching_fibonacci, яка створює та використовує кеш для зберігання і повторного використання вже обчислених значень чисел Фібоначчі.
"""

import time                                   # To test faster cache

def cashing_fibonacci():
    cache = {}                                # Cache dictionary

    def fibonacci(n):
        if n <= 0:
            return 0
        if n == 1:                            # Base case
            return 1
        if n in cache:
            return cache[n]                   # Returns already calculated value from dictionary cahce for number-key "n"
        
        cache[n] = fibonacci(n-1) + fibonacci(n-2) # Рекурсія
        return cache[n]
    
    return fibonacci                               # Повертаємо внутрішню функцію
        

# testing

fib = cashing_fibonacci()

print(fib(10))
print(fib(15))

# testing faster cache 

start_1 = time.time()
print(fib(400))
end_1 = time.time()

start_2 = time.time()
print(fib(400))
end_2 = time.time()

# Just for fun :)
print(f"Execution time 1: {(end_1 - start_1)*(10**6):0.2f} microseconds. Execution time 2:{(end_2 - start_2)*(10**6):0.2f} microseconds")
print(f"time delta: {((end_1 - start_1)-(end_2 - start_2))*10**6:0.2f} microseconds")
print(f"Faster exec {((end_1 - start_1)/(end_2 - start_2))*10**6:_} times")  
