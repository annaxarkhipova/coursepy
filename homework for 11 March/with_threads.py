# Также запустите ее три раза с теми же аргументами,
# но каждую в отдельной потоке с помощью  threading.Thread.
# Не забудьте стартануть треды и дождаться их окончания.

import threading
import time


def odd_primes(end, start):
    print('Старт вычислений, начиная с {}'.format(end))

    primes = []
    for a in range(end, start, -1):
        if is_prime_number(a):
            primes.append(a)
    return primes


def is_prime_number(x):
    if x >= 2:
        for y in range(2, x):
            if not (x % y):
                return False
    else:
        return False
    return True


# odd_primes(10000, 2)
# odd_primes(20000, 10001)
# odd_primes(30000, 20001)


    print('Конец')


v = int(time.time())

threads = []

for i in range(3):
    thr1 = threading.Thread(target=odd_primes, args=(i, )).start()
    thr2 = threading.Thread(target=odd_primes, args=(i, )).start()
    thr3 = threading.Thread(target=odd_primes, args=(i, )).start()

    threads.append(thr1,thr2,thr3)

for thr in threads:
    thr.join()
print('Общее время вычислений в секундах: {}'.format(int(time.time() - v)))

