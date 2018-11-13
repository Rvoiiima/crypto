#!/usr/bin/env python
# -*- coding: utf-8 -*-

import itertools
import string
import sys

f = open('./enc', 'rb')
data = f.read()

smallprimes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59,
       61, 67, 71, 73, 79, 83, 89, 97, 101]


def check(v):
   return v[0] ^ v[1] ^ v[2] == v[3]


def get_key(v):
   return v[2], v[0] ^ v[1] ^ v[3]


def valid(v):
   # set(v) == different tuples
   # f for... == different first elements
   return len(set(v)) == len({f for f, g in v})


# For a certain key-length guess
for keyl in range(1, 22):
   print 'keylength: %d' % keyl
   # For a prime-pair candidate
   for p,q in itertools.product(smallprimes, repeat=2):
       s = []
       # Generate a key for this combination
       for c, pt in enumerate('m1z0r3{'):
           # This is known for a given p,q
           ilist = range(0 + c, 217, 31)
           senc = [ord(data[i]) for i in ilist]
           x1 = map(lambda x: x % p, ilist)
           x2 = [(ord(pt)**q) % (q**2 - 6 * q + 7)] * 7
           # calculate a possible key for this p, q pair
           indices = map(lambda x: (x * 7) % keyl, ilist)
           s.extend(map(get_key, zip(x1, x2, indices, senc)))
           # Key still valid?
           if not valid(s):
#               print s
               break
           if pt == '{':
               s = list(set(s))
               s.sort(key=lambda x: x[0])
               key = map(lambda x: x[1], s)
               # print 'decrypting with \np: %d\nq: %d\nkey: %s' % (p, q, ''.join(map(lambda x: chr(x), key)))
               # Bruteforce pt char-by-char
               pt = ''
               for i in range(len(data)):  # or range(43)
                   for ptc in string.printable:
                       x1 = i % p
                       x2 = (ord(ptc)**q) % (q**2 - 6 * q + 7)
                       x3 = key[7 * i % len(key)]
                       enc = x1 ^ x2 ^ x3
                       if enc == ord(data[i]):
                           pt += ptc
               print pt
               print s
