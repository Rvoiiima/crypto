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
#13.113.218.1 54321
HOST, PORT = "13.113.218.1", 54321

s, f = sock(HOST, PORT)    # 接続

read_until(f, ">")
s.send("3")
test = read_until(f)
enc_flag = long(read_until(f).split()[3])
print "enc_flag:",enc_flag
read_until(f, ">")
s.send("1")
read_until(f, ":")
s.send(l2b(256))
enc_256 = long(read_until(f))
read_until(f, ">")
s.send("4")
read_until(f)
n = long(read_until(f).split()[3][:-2])
print "n:", n
read_until(f,">")
s.send("2")
read_until(f,":")
s.send( str(enc_256 * enc_flag % n) )
flag =  long(read_until(f))
pt = ""

print l2b(flag)
'''
while flag != 0:
    dummy = flag % 256
    pt += chr(dummy)
    flag = flag / 256
    print pt
print pt[::-1]
'''
