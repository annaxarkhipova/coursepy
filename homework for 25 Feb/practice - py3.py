



class Practice:
    def is_prime():
        for a in range(2, 1001):
            prime = True
            for i in range(2, a):
                if a % i == 0:
                    prime = False
            if prime:
                print (a, '- prime')
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
        if word.startswith(word[0].upper()) == False:
            update = word[0].upper()
            a = word[1:]
            print(update + a)


        # wave("hello") = > ["Hello", "hEllo", "heLlo", "helLo", "hellO"]



        return
    wave()

if __name__ == '__main__':
    Practice()