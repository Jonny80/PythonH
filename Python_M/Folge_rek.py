from cmath import sqrt


def folge():
    erg = 0.5
    count = 0
    erg2 = 0.5
    while(count < 30):
        count = count +1
        erg = 1-sqrt(1-erg)
        print(erg2 / erg)
        erg2 = erg
        print(erg)


folge()