#!/usr/bin/python
# -*- coding:utf-8 -*-
import socket, struct, telnetlib
from Crypto.Util.number import long_to_bytes as l2b
# --- common funcs ---
def sock(remoteip, remoteport):
  s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  s.connect((remoteip, remoteport))
  return s, s.makefile('rw', bufsize=0)

def read_until(f, delim='\n'):
  data = ''
  while not data.endswith(delim):
    data += f.read(1)
  return data

def shell(s):
  t = telnetlib.Telnet()
  t.sock = s
  t.interact()

def get_cookie(username):
    read_until(f, "whitespace):")
    s.send(username+"\n")
    read_until(f, "is: ")
    return read_until(f).strip()

def p(a): return struct.pack("<I",a)
def u(a): return struct.unpack("<I",a)[0]

# --- main ---
HOST, PORT = "13.113.218.1", 12345
s, f = sock(HOST, PORT)    # 接続

dummy = read_until(f, ">")
s.send("3\n")
enc_flag = read_until(f, ")")
print "enc_flag:" ,enc_flag
c1 = long(enc_flag.split()[6][1:-1])
c2 = long(enc_flag.split()[7][:-1])
print "c1:", c1
print "c2:", c2
test = read_until(f,">")
print test
s.send("1\n")
read_until(f, "message:")
s.send(l2b(2))
c_x02 = read_until(f , ")").split()

print "c_x02", c_x02
c1_x02 = long(c_x02[0][1:-2])
c2_x02 = long(c_x02[1][:-2])
print "c1_x02:", c1_x02
print "c2_x02:", c2_x02

read_until(f,">")
s.send("4\n")
ygp = read_until(f, "L)").split(":")[1].split(",")
print "ygp:", ygp
y = long(ygp[0][2:-1])
g = long(ygp[1][1:-1])
p =long(ygp[2][1:-2])

print "y:", y
print "g:", g
print "p:", p

UB = p
LB = 0
while 1:
    read_until(f,">")
    c1 = (c1 * c1_x02) % p
    c2 = (c2 * c2_x02) % p
    s.send("2\n")
    read_until(f,"c1:")
    s.send(str(c1) + "\n")
    read_until(f,"c2:")
    s.send(str(c2) + "\n")
    digit = read_until(f, "-")
    digit = int(digit[:-2])
    print digit

    if digit == 1:
        LB = (UB + LB) / 2
    elif digit == 0:
        UB = (UB + LB) / 2

    print "UB:", UB
    print "LB:", LB

    if UB == LB:
        break


l2b(69738345988067693181314793186309978610630742549490905494208294511042643521281937979300103764610521451627246631677319339182822908610794392454479662058908169381185634181102047282880328141368645925991377533350995542987546641350646000961945495137116228421431107018007766909403934581044144731898196405)
'm1z0r3{ElGamal_1s_h0m0m0rph1c_3ncrypt10n!!}\nService Problem(It have a no connection with the score.)->nc 13.113.218.1 5431\xb5'

