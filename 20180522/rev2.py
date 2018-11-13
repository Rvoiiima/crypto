from PIL import Image
import numpy as np
import collections
import hashlib

f = open("encrypted.txt")

text = f.read()
enc = [text[i:i + 64] for i in range(0, len(text), 64)]
c = collections.Counter(enc)
print c
#l1 = open('./list.txt','w')
#for i in enc:
#    l1.write(i+"\n")

color_map = {}

for r in range(256):
    for g in range(256):
        for b in range(256):
            hash = hashlib.sha256(chr(r) + chr(g) + chr(b)).hexdigest()
            if hash in c.keys():
                print "(", r, g, b, ")"
                print "find!"
                color_map[hash] = (chr(r), chr(g), chr(b))

print color_map

b = ""
f = open("encrypted.txt")
while True:
    s = f.read(64)
    if s == "": break
    else:
        b += color_map[s][0] + color_map[s][1] + color_map[s][2]
        
f.close()

x = len(b)/3
print(x)

for a in range(1, int(np.sqrt(x))):
    if x%a == 0:
        print a, x/a
    i = Image.frombytes("RGB", (int(x/a), a), b)
    i.save("2out"+ str(a)+".png")
