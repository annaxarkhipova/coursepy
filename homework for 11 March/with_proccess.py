
# Также запустите ее три раза с теми же аргументами, но каждую в отдельной потоке с помощью  multiprocessing.Process.
# Не забудьте стартануть процессы и дождаться их окончания.

import multiprocessing
import threading
import time


def odd_primes(end, start):
    print('Старт вычислений, начиная с {}'.format(end))

    primes = []
    for a in range(end, start, -1):
        if is_prime_number(a):
            primes.append(a)

    print('Конец вычислений')

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

# threads = []

for i in range(5):
    thr1 = threading.Thread(target=odd_primes, args=(10000, 3))
    thr1.start()

    thr2 = threading.Thread(target=odd_primes, args=(20000, 10001))
    thr2.start()

    thr3 = threading.Thread(target=odd_primes, args=(30000, 20001))
    thr3.start()

    thr1.join()
    thr2.join()
    thr3.join()
print('Общее время вычислений в секундах: {}'.format(int(time.time() - v)))

