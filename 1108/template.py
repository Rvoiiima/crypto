#!/usr/bin/python
# -*- coding:utf-8 -*-
import socket, struct, telnetlib,string
import itertools

import os, base64, time, random
from Crypto.Cipher import AES
from Crypto.Hash import *
# --- common funcs ---
def sxor(s1,s2):    
  return ''.join(chr(ord(a) ^ ord(b)) for a,b in zip(s1,s2))

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
HOST, PORT = "52.193.157.19", 9999
s, f = sock(HOST, PORT)    # 接続
text = read_until(f, "XXXX:")
text = text.split('==')
hash_from4 = text[0].split("+")[1].strip()[:-1]
hash = text[1].split("\n")[0].strip()
print "hash", hash
for i in itertools.product(string.ascii_letters + string.digits, repeat=4):
    
    pr = "".join(i) + hash_from4
    if SHA256.new(pr).hexdigest() == hash:
        s.send("".join(i) + "\n")
        print i
        break
        
    
print read_until(f, "Done!\n")
w = read_until(f)
print w

iv = '2jpmLoSsOlQrqyqE'

w = base64.b64decode(w)

source = "Welcome!!" + "\x07" * 7
target = "get-flag" + "\x08" * 8

iv2 = sxor( iv , sxor(source, target) )

s.send(base64.b64encode(iv2 + w[16:]) + "\n")
enc_flag = read_until(f).strip()

enc_flag = base64.b64decode(enc_flag)
print len(enc_flag)

target2 = "get-md5" + "\x09" * 9
iv3 = sxor( iv, sxor(source, target2) )

s.send(base64.b64encode(iv3 + w[16:]) + "\n")
md5 = read_until(f).strip()
iv4 = sxor( "hitcon{" + "\x09" * 9 , sxor( "get-md5" + "\x09" * 9 , enc_flag[:16]))

for te in range(255):
    print te
    s.send(base64.b64encode(iv4 +enc_flag[16:32]+enc_flag[32:47] + chr(te) + enc_flag[48:]) + "\n")
    sou = read_until(f).strip()
    if sou == md5:
        print "ans", te
        midnum = te
        break

bit_num = 41 ^ midnum ^ ord(enc_flag[47])
print bit_num

