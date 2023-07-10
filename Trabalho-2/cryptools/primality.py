import secrets
import random

def fexp(base, exp, mod=None):
    res = 1
    while exp:
        if (exp & 1):
           res = (res * base) % mod 
        base = (base * base) %mod
        exp >>= 1
    return res

def is_composite(n, d, s, a):
    x = fexp(a, d, mod=n)

    if x == 1 or x == n - 1:
        return False


    for i in range(1, s):
        x = (x * x) % n

        if x == n - 1:
            return False

    return True

def miller_rabbin(n, iter=40):

    """
    Implementação do teste de primalidade de Miller-Rabbin

    Ret:
    - True: se um número é possivelmente primo
    - False: se o número é composto
    """
    small_primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

    # testa primalidade com números menores que 100 para acelerar o processo
    for prime in small_primes:
        if n % 2 == 0:
            return False

    d = n-1
    s = 0

    while d % 2 == 0:
        d >>=1
        s+=1

    for i in range(iter):
        a = random.randint(2, n - 1)
        if is_composite(n,d,s,a):
            return False
    return True

def random_1024():
    # gera número aleatório de 1024 bits
    random_bytes = secrets.token_bytes(128)
    integer_value = int.from_bytes(random_bytes) 
    return integer_value

def gen_prime():
    while True:
        p = random_1024()
        if miller_rabbin(p):
            return p
