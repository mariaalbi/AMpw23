# def fib(n):
#     x, y = 0, 1
#     for _ in range(n):
#         x, y = y, x + y
#     return x
#
# #for n in range(10):
#     #print(n, fib(n))
#
# def fib_items(n):
#     return [
#         fib(x) for x in range(n)
#     ]
# print(fib_items(10))


def fib(n:int) -> int:
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b
i = 0
for n in fib(10):
    print(i, n)
    i += 1
