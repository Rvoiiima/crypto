import random, string,base64

from Crypto.Cipher import AES
from Crypto.Hash import *

for _ in xrange(100):
    proof = ''.join([random.choice(string.ascii_letters+string.digits) for _ in xrange(20)])
    print "SHA256", SHA256.new(proof).hexdigest()
    print "SHA256from4", SHA256.new(proof[4:]).hexdigest()

