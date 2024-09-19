# modul
import math

def factorial(n):
    return math.factorial(n)

print(factorial(5))


# Egen

def fakultet(n):
    resultat = 1
    for i in range(1,n + 1):
        resultat *= i
    return resultat


print(fakultet(5))