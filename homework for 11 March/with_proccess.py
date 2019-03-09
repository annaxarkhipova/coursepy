
# Также запустите ее три раза с теми же аргументами, но каждую в отдельной потоке с помощью  multiprocessing.Process.
# Не забудьте стартануть процессы и дождаться их окончания.

import multiprocessing
import time

v = time.time()

def odd_primes(end, start):
    print('Старт вычислений, начиная с {}'.format(end))


    primes = []
    for a in range(end, start, -1):
        if is_prime_number(a):
            primes.append(a)

    print('Конец вычислений c {}. Затрачено {} сек'.format(end, int(time.time() - v)))


def is_prime_number(x):
    if x >= 2:
        for y in range(2, x):
            if not (x % y):
                return False
    else:
        return False

process = []

pr = multiprocessing.Process(target=odd_primes, args=(10000, 3,))

pr1 = multiprocessing.Process(target=odd_primes, args=(20000, 10001,))

pr2 = multiprocessing.Process(target=odd_primes, args=(30000, 20001,))

pr.start()
pr1.start()
pr2.start()

process.append(pr)
process.append(pr1)
process.append(pr2)

pr.join()
pr1.join()
pr2.join()

print('Общее время вычислений в секундах: {}'.format(int(time.time() - v)))


