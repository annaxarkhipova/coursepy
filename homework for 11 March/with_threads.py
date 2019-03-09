# Также запустите ее три раза с теми же аргументами,
# но каждую в отдельной потоке с помощью  threading.Thread.
# Не забудьте стартануть треды и дождаться их окончания.


import threading
import time

v = time.time()


def odd_primes(end, start):
    print('Старт вычислений, начиная с {}'.format(end))

    primes = []
    for a in range(end, start, -1):
        if is_prime_number(a):
            primes.append(a)


    print('Конец вычислений c {}. Затраченo {} сек'.format(end, int(time.time() - v)))


def is_prime_number(x):
    if x >= 2:
        for y in range(2, x):
            if not (x % y):
                return False
    else:
        return False


v = time.time()

threads = []

thr = threading.Thread(target=odd_primes, args=(10000, 3, ))

thr1 = threading.Thread(target=odd_primes, args=(20000, 10001, ))

thr2 = threading.Thread(target=odd_primes, args=(30000, 20001, ))

thr.start()
thr1.start()
thr2.start()

threads.append(thr1)
threads.append(thr)
threads.append(thr2)


thr.join()
thr1.join()
thr2.join()

print('Общее время вычислений в секундах: {}'.format(int(time.time() - v)))

