import hashlib
import random


def invmod(a, m):
    if a < 0 or m <= a:
        a = a % m

    c, d = a, m
    uc, vc, ud, vd = 1, 0, 0, 1
    while c != 0:
        q, c, d = divmod(d, c) + (c,)
        uc, vc, ud, vd = ud - q * uc, vd - q * vc, uc, vc
    assert d == 1

    if ud > 0:
        return ud
    else:
        return ud + m
    
def  hashFunc(string):
    hash_object = hashlib.sha256(string.encode())
    message_digest = hash_object.digest()
    return int.from_bytes(message_digest, 'big')


def kunci(p, q, h):
    if (p-1)%q != 0:
        print("p-1 tidak habis dibagi q")
        return None
    g = h **((p-1)//q)%p
    x = int(input("Masukkan bilangan acak x (lebih kecil dari p): "))
    y = g**x % p
    return (p, q, g, y, x)

def pembangkitan(kunci):
    p, q, g, y, x = kunci
    k = random.randint(1, q-1)
    r = pow(g, k, p)%q
    s = (invmod(k, q)*(hashFunc("hello")+x*r))%q
    return (r, s)

def verifying(key1, key2):
    p, q, g, y, x = key1
    r, s = key2
    w = invmod(s, q)
    u1 = hashFunc("hello")*w % q
    u2 = r*w % q
    v = ((pow(g, u1, p)*pow(y, u2, p))%p)%q
    if v == r:
        print("Tanda tangan valid")
    else:
        print("Tanda tangan tidak valid")
    return v

