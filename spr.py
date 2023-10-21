def fib(n):
    x, y = 0, 1
    for a in range(n-1):
        a = x + y
        x = y
        y = a
    return x
print(fib(8))