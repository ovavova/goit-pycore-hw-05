"""
Реалізуйте функцію caching_fibonacci, яка створює та використовує кеш для зберігання і повторного використання вже обчислених значень чисел Фібоначчі.
"""

import time  # To test faster cache


def cashing_fibonacci():
    cache = {}  # Cache dictionary

    def fibonacci(n):
        if n <= 0:
            return 0
        if n == 1:  # Base case
            return 1
        if n in cache:
            return cache[n]  # Returns already calculated value from dictionary cahce for number-key "n"

        cache[n] = fibonacci(n - 1) + fibonacci(n - 2)  # Рекурсія
        return cache[n]

    return fibonacci  # Повертаємо внутрішню функцію


if __name__ == "__main__":

    # testing

    fib = cashing_fibonacci()

    print(fib(10))
    print(fib(15))

    # testing faster cache
    iterations = 900  # Setting datapoint

    start_1 = time.time()
    print(fib(iterations))
    end_1 = time.time()

    start_2 = time.time()
    print(fib(iterations))
    end_2 = time.time()

    # Comparing camputation times for cashed vs non cached
    print("-|" * iterations)
    print(
        f"Execution time no-cache: {(end_1 - start_1)*(10**6):0.2f} microseconds. Execution time using cache:{(end_2 - start_2)*(10**6):0.2f} microseconds"
    )
    print(
        f"time delta: {((end_1 - start_1)-(end_2 - start_2))*10**6:0.2f} microseconds"
    )
    print(
        f"Cashed access faster on {iterations} iterations  {((end_1 - start_1)/(end_2 - start_2)):.0f} times"
    )
