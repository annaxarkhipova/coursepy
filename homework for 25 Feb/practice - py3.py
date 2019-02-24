



class Practice:
    def is_prime():
        for a in range(2, 1001):
            prime = True
            for i in range(2, a):
                if a % i == 0:
                    prime = False
            if prime:
                print ('{} - prime'.format(a))
        return
    is_prime()


    def modul_chisla():
        n = int(input('Put some number:'))
        if n >= 0:
            print(n)
        else:
            print(-n)
        return
    modul_chisla()


    def wave():
        word = 'hello'
        for i in range(len(word)):
            print(word[:i] + word[i].upper() + word[i + 1:])
        return
    wave()

if __name__ == '__main__':
    Practice()