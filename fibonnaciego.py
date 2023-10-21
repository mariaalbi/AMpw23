def fib(n):
    x, y = 0, 1
    for _ in range(n):
        x, y = y, x + y
    return x


for n in range(10):
    print(n, fib(n))
#a = x + y
#y = x
#x = a