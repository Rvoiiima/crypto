#! -*- coding:utf-8 -*-
from Crypto.Util.number import *
# utf8での記述を明示．

# 拡張ユークリッドの互除法
## 引数にax+by = c の a,bを与える
## 戻り値は上の式で言う(c,x,y)

#openssl rsa -text -modulus  < private.pem

def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, x, y = egcd(b % a, a)
        return (g, y - (b // a) * x, x)

def modInv(a, m):
 g, x, y = egcd(a, m)
 if (g != 1):
     raise Exception("[-]No modular multiplicative inverse of %d under modulus %d" % (a, m))
 else:
     return x % m
# =====二つの素数(p,q)=====

p = 16764777456439012943
q = 14588483238879488297

p = 266683113499462312545298628822065386373
q = 308758312134856791097912370126872877707
print "q:", q
# =====公開鍵(e,n)の(e,n)=====
n = p*q
e = 65537 # phinと互いに素


# =====オイラーのφ関数(phin)=====
phin = (p-1) * (q-1)

# =====秘密鍵(d)=====
d = egcd(e, phin)[1]
if d < 0:
    d += phin

print "秘密鍵d: ",d


# ====鍵による暗号化=====
plain = "flag{My_fav0rite_pr1mes!}" # 平文(のつもりの数値) 1<plain_int<n

plain = bytes_to_long(plain)

print plain
c = pow(plain, e, n)
with open('flag.enc', 'w') as f:
    f.write(long_to_bytes(c))
with open("flag.enc","r") as fb:
    c = fb.read()
