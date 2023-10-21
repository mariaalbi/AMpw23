import time
from time import sleep
def cached(fn):
    cache = {}
    def wrapper(*args, **kwargs):
        params = (args, tuple(kwargs.items()))
        if params not in cache:
            cache[params] = fn(*args, **kwargs)
        return cache[params]
    return wrapper

#from functools import lru_cache

@cached
def fib(n):
    if n in [0, 1]:
        return n
    return fib(n - 1) + fib(n - 2)

print(fib(100))