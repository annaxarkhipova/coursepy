

# Напишите функцию odd_primes(end, start), которая ищет все простые числа в диапазоне
# от заданного числа start (по умолчанию 3) до заданного числа end.
# Запустите ее:
# Три раза последовательно в диапазоне от 3 до 10000, от 10001 до 20000, от 20001 до 30000.

import time


def odd_primes(end, start):

    print('Старт вычислений, начиная с {}'.format(end))

    primes = []
    for a in range(end, start, -1):
        if is_prime_number(a):
            primes.append(a)

    print('Конец')

    return primes


def is_prime_number(x):
    if x >= 2:
        for y in range(2, x):
            if not (x % y):
                return False
    else:
        return False
    return True


v = time.time()

for i in range(3):
    odd_primes(10000, 2)
    # odd_primes(20000, 10001)
    # odd_primes(30000, 20001)

print('Общее время вычислений в секундах: {}'.format(int(time.time() - v)))


