import random


class MyException(Exception):
    pass

def boo():
    if random.random() < 0.5:
        raise Exception("Boo!")
    print("Ok")

try:
    boo()
except MyException as e:
    print(f"An exception has occured: {e}")
    print("trying to safely end the program")
except Exception as e:
    print(f"Unknown exception: {e}")