import math

def primes(x):
    if x < 2: return []

    primes = [i for i in range(x)]
    primes[1] = 0 

    for prime in primes:
        if prime > math.sqrt(x): break
        if prime == 0: continue
        for non_prime in range(2 * prime, x, prime): primes[non_prime] = 0

    return [prime for prime in primes if prime != 0]


def is_prime(x):
    if x < 2: return False 
    if x == 2 or x == 3 or x == 5: return True 
    if x % 2 == 0 or x % 3 == 0 or x % 5 == 0: return False 

    prime = 7
    step = 4
    while prime <= math.sqrt(x):
        if x % prime == 0: return False

        prime += step
        step = 6 - step

    return True


if __name__ == '__main__':
    print(primes(500)) 

