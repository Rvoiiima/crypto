import math
def fermat(N):
    x = math.sqrt(N)
    y = math.sqrt(pow(x, 2)-N)

    z = (x+y)*(x-y)
    while (N == z):
        if N > z:
            x += 1
        else:
            y += 1
    return (x+y), (x-y)


modulus = "A25F8E22F342009C0A52E3BEA4D40EBD0E67292A01E7A26AD6A98AFB3C899D95B3848EE4E0FDFD0662B7E8B29E98F9C2DBCA2EA00488F0C6783492E0BD52D6FA6BB2F192A4B7582276FBF0352A17B61845D5E0AD95F9C91C39766CA57E59AF6407EA44592085A791F98738111F7CCB9B02135BE433A3CFA0397F9B84F96D8A25"

e = 3

N = int(modulus, 16)
print "N:", N

print fermat(N)

