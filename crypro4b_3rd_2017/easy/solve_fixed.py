def gcd(x, y):
    while y:
        x, y = y, x%y
    return x

def lcm(x, y):
    return x*y //gcd(x, y)

def exgcd(x, y):
    c0, c1 = x, y
    a0, a1 = 1, 0
    b0, b1 = 0, 1
 
    while c1 != 0:
        m = c0 % c1
        q = c0 // c1
 
        c0, c1 = c1, m
        a0, a1 = a1, (a0 - q * a1)
        b0, b1 = b1, (b0 - q * b1)
 
    return c0, a0, b0


def main():
    p=16764777456439012943
    q=14588483238879488297

    N = p*q
    e = 65537

    lam = lcm(p-1, q-1)

    c, a, b = exgcd(e, lam)

    print a, b, c

    a = modinv(a, lam)
    print(a)

    with open('flag.enc', 'r') as f:
        crypt = f.read()
        crypt = crypt.encode('hex')
        crypt = int(crypt , 16)

        ans = pow(crypt, a, N)

        ans = hex(ans)[2:-1].decode('hex')
        print ans


#    print(binascii.a2b_hex(ans).decode('utf-8'))

if __name__ == '__main__':
    main()
