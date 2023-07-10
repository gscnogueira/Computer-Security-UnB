import secrets
from math import lcm
import hashlib
import base64

from cryptools.primality import gen_prime, fexp
import cryptools.OAEP as OAEP

def gcd (a, b):
    """
    Implementação iterativa do algoritmo extendido de euclides
    para o caculo do gcd

    Ret: tripla (gcd, x, y,) em que gcd = x*a + y*b
    """

    x,y = 0, 1
    x1, y1 = 1, 0

    while b:
        q = a//b
        a, b = b, a % b
        x, x1 = x1  - q * x, x
        y, y1 = y1  - q * y, y

    return a, x1, y1

def find_e(l):
    for i in range(3, l):
        g, x, y = gcd(i,l)
        if g == 1:
            return i, x, y

def gen_keys():
    p = gen_prime()
    q = gen_prime()
    n = p*q
    lambda_n =(lcm(p-1, q-1))
    e, d, _ = find_e(lambda_n)
    d%=lambda_n

    return (n,e),(n,d)

def to_bytes(n):
    """
    Transforma um número inteiro em uma sequencia de bytes
    """
    bytes_ = b''
    while n:
        bytes_ = bytes([n & 0xFF]) + bytes_
        n >>=8

    return bytes_

def encrypt(text, p_key):
    n, e = p_key
    m = OAEP.encrypt(text )
    m = int.from_bytes(m)
    c = fexp(m, e, mod=n)
    return to_bytes(c)

def decrypt(message, s_key):
    n, d = s_key
    c = int.from_bytes(message)
    m = fexp(c, d, mod=n)
    m_bytes = b'\x00' + to_bytes(m)

    return OAEP.decrypt(m_bytes)

def sign(message, private_key):
    n, d = private_key
    hash_value = (hashlib.sha3_256(message).digest())
    hash_value = int.from_bytes(hash_value)
    sig = to_bytes(fexp(hash_value, d, mod=n))
    sig = base64.b64encode(sig)
    return sig

def verify(message, public_key, signature):
    n, e = public_key
    hash_value = (hashlib.sha3_256(message).digest())
    signature = base64.b64decode(signature)
    signature = int.from_bytes(signature)
    m = to_bytes(fexp(signature, e, mod=n))

    if m==hash_value:
        print('Ok. Mensagem não foi adulterada.')
    else:
        print('PERIGO. Mensagem foi adulterada.')
    
