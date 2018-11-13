#! -*- coding:utf-8 -*-
from Crypto.Util.number import *
# utf8での記述を明示．

#openssl rsa -text -modulus -pubin < public_key.pem

# 拡張ユークリッドの互除法
## 引数にax+by = c の a,bを与える
## 戻り値は上の式で言う(c,x,y)
def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, x, y = egcd(b % a, a)
        return (g, y - (b // a) * x, x)

# =====二つの素数(p,q)=====


p= 65239
q = 165494699476181209513097307784459589146335370862096470969701955288743090244116797751933368391410036249462854003686693084544152202108407718043006829978153157351565072697495372426864580685114482050124843561828023123222460786476031828030728723597345797464222270282168330504011404230414216871641262526165170730587
print "q:", q
# =====公開鍵(e,n)の(e,n)=====
n = p*q
print "n", n
e = 65537 # phinと互いに素


# =====オイラーのφ関数(phin)=====
phin = (p-1) * (q-1)


# =====秘密鍵(d)=====
d = egcd(e, phin)[1]
if d < 0:
    d += phin

print "秘密鍵d: ",d


# ====鍵による暗号化=====
plain = "flag{1_Like_the_sm@ll_prim3!}" # 平文(のつもりの数値) 1<plain_int<n

plain = bytes_to_long(plain)

print plain
c = pow(plain, e, n)
#with open('flag.enc', 'w') as f:
#    f.write(long_to_bytes(c))
with open("flag.enc","r") as fb:
    c = fb.read()

h = c.encode("hex")

c = int(h,16)
'''
'''
print "暗号文  : ",c

# =====鍵による復号化=====
p = pow(c, d, n)
print "復号結果: ",p

he = hex(p)

print "he:",he

text = he[2:-1].decode("hex")

print "text",text


