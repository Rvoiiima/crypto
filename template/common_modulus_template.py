import gmpy

def common_modules_attack(c1, c2, e1, e2, n):
    gcd, s1, s2 = gmpy.gcdext(e1, e2)
    if s1 < 0:
        s1 = -s1
        c1 = gmpy.invert(c1,n)

    elif s2 < 0:
        s2 = -s2
        c2 = gmpy.invert(c2,n)

    v = pow(c1, s1, n)
    w = pow(c2, s2, n)

    x = (v*w) % n
    return x

