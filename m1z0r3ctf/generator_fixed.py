#!/usr/bin/env python3


from secret import p, q, r, key, flag
flag = flag * r

def encrypt(msg, p, q, r, key):
  enc = []
  for i in range(len(msg)):
  	enc += [(i%p) ^ ((ord(msg[i])**q) % (q**2 - 6*q + 6)) ^ key[r*i % len(key)]]

  return bytes(enc)

with open('enc', 'wb') as f:
  f.write(encrypt(flag, p, q, r, key))
