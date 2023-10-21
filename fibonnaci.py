def fib(n: int) -> int:
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b
    return a
i = 0
for n in fib(10):
    print(i, n)
    i += 1
#
# def fib_items(n):
#     return [
#         fib(x) for x in range(n)
#     ]
#

print(fib_items(10))