import math


def MNF(a, b, c):
    if (b*b-4*a*c) < 0:
        print("Kein Ergbenis in den reelen Zahlen")
    else:
        e1 = (-b-math.sqrt(b*b-(4*a*c)))/2*a
        e2 = (-b+math.sqrt(b*b-(4*a*c)))/2*a
        print(e1,e2)

def Fibo(n):
    if n == 1 or n == 0:
        return 1
    return Fibo(n - 1) + Fibo(n - 2)
    print(Fibo(7))


def sum(z):
    result = 0
    while z:
        result += z % 10
        z = int(z/10)
    print(result)
opt = eval(input("geben sie 1 für MNF, 2 für Fib oder 3 für sum ein"))

if opt == 1:
    a1 = eval(input())
    a2 = eval(input())
    a3 = eval(input())
    MNF(a1,a2,a3)
if opt == 2:
    a4= int(input())
    Fibo(a4)
if opt == 3:
    a5 = int(input())
    sum(a5)
else:
    print("bitte geben sie eine der genannten Nummern ein")