list = continued_fraction(e/n).convergents()

candidate =[]
"""
for i in list[1:]:
    d = i.denom()
    k = i.numer()
    phi_n = (e*d - 1)/k 
    if phi_n.is_integral():
        print("get")
        candidate.append(d)
for d in candidate:
    print(pow(m,d*e, n))
"""

"""
m = 5
for i in range(len(list)):
    print(i)
    d1 = list[i].denom()
    d2 = list[i+1].denom()

    for s in range(10):
        for r in range(10):
            d = s*d1 + r*d2
            
#            print(s, r)
            if int(pow(m, e*d, n)) == m:
                print("candidate:", d)
"""


