from PIL import Image
import numpy as np
import collections
import hashlib

f = open("encrypted.txt")
b = ""

while True:
    s = f.read(64)
    if s == "": break
    if s == "709e80c88487a2411e1ee4dfb9f22a861492d20c4765150c0c794abd70f8147c":
        b += chr(0) + chr(0) + chr(0)
    else:    
        b += chr(255) + chr(255) + chr(255)

f.close()

x = len(b)/3
print(x)

for a in range(1, int(np.sqrt(x))):
    if x%a == 0:
        print a, x/a
    i = Image.frombytes("RGB", (int(x/a), a), b)
    i.save("out"+ str(a)+".png")
