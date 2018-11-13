# coding: utf-8  
from itertools import combinations


def multi(a):
    res = 1
    for i in a:
       res *= i

    return res
    
def check(a):
    if len(str(a)) == 38:
        return 1
    else:
        return 0

hack = 8213242002076053911181908692341986030919593545361549673265676083814813944695092587591375250

factor = [2 , 5, 5, 5 , 19 , 79 , 239 , 106979 , 206603 , 63634387 , 35183414437 , 1643759635229 , 23644671381761 , 26047344042803 , 1828083256178279]

for i in xrange(len(factor)-1):
    l = list(combinations(factor, i)) #i回並べる
    for j in l:
        x = multi(j)
        if check(x) == 1:
            pad = x
            
            hack = hack/(pad *  ord("}")) -1
            flag = ""
            for _ in xrange(27):
                for i in xrange(9, 128):
                    if hack % i == 0:
                        flag += chr(i)
                        hack = hack / i-1
                print flag




#print str(pad)
            


