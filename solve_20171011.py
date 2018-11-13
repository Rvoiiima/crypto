#!/usr/bin/python
# -*- coding:utf-8 -*-
import socket, struct, telnetlib

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
HOST, PORT = "crypto.chal.csaw.io", 1578
s, f = sock(HOST, PORT)    # 接続
print get_cookie("a" * 27 +"flag"+ "{")[:64]
print get_cookie("a" * 27  )[:64]

flag= ""
for i in range(26):
    check = get_cookie("a" * (26-i))[:64]
    for j in range(32,256):
        print chr(j)
        if get_cookie("a" * (26-i) + "flag{"+ flag + chr(j))[:64] == check:

            flag = flag + chr(j)
            print flag
            break

