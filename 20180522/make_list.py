import collections
import hashlib
f = open('./encrypted.txt', 'r')
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
                color_map[hash] = (r, g, b)

print color_map
