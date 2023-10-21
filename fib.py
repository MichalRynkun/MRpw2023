import time

_cache = {}

# def fib(n):
#     if n  in [0,1]:
#         return  n
#     if n not in _cache:
#         _cache[n] = fib(n-1) + fib(n-2)
#     return _cache[n]
# print(fib(70))
# print(len(_cache))

from time import sleep

def timeit(fn):

    def wrapper(*args, **kwargs):
        start = time.time()
        result = fn(*args, **kwargs)
        end = time.time()
        print((f"Duration {end - start}"))
        return result
    return wrapper


@timeit
def greeting():
    a = 2
    b = 4
    c = b % a
    sleep(3)
    print("Hello Marysia")
    sleep(1)
    print(f"{c}")
    sleep(1)
# start = time.time()
# greeting()
# end = time.time()
# print(end-start)

# greeting = timeit(greeting)
greeting()