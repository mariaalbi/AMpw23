def par(n):
    for a in range(2*n):
        if a % 2 == 0:
            yield a
#for number in par(20):
   # print(number)


def is_prime(n):
    if n in [0, 1]:
        return False
    for d in range (2, n):
        if n % d == 0:
            return False
    return True


def primes(n):
    x = 0
    cnt = 0
    while cnt < n:
        while not is_prime(x):
            x += 1
        yield x
        x += 1
        cnt += 1


for p in primes(10):
    print(p)
