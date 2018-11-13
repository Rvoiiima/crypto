#!/usr/bin/python
import socket
import string, base64, json
import salsa20
def sxor(s1,s2):    
  return ''.join(chr(ord(a) ^ ord(b)) for a,b in zip(s1,s2))

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  
s.connect(('flatearth.fluxfingers.net', 1721))
keybuf = s.recv(4096)

s.send('\x00' * 8192)
abuf = ''
while len(abuf) < 8192:
  abuf += s.recv(409600)

msg = {"cnt" : 1, "data" : "A"*128}
msgtext = json.dumps(msg)
print sxor(sxor(keybuf[1:], abuf[:]), msgtext)
