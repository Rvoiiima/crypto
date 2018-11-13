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

def sxor(s1,s2):    

#main
HOST, PORT = "localhost", 10001
s, f = sock(HOST, PORT)    # 接続

s.send("" + "\n") # 端末で書き込んでenterを押す動作と対応
read_until(f, "")
