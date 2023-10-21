import time

_cache = {}

def fib(n):

    if n in [0,1]:
        return n
    if n not in _cache:
        _cache[n] = fib(n - 1) + fib(n -2)
    return _cache[n]
print(fib(70))
print(len(_cache))

import time
from time import sleep

def timeit(fn):
    def wrapper():
        start = time.time()
        result = fn()
        end = time.time()
        print(f"Duration {end - start}")
        return result
    return wrapper

@timeit
def greeting():
    print("Hello world")
    sleep(3)
# start = time.time()
# greeting()
# end = time.time()
# print(end - start)

#greeting = timeit(greeting())
greeting()