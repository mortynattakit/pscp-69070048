"""This code will add fibonacci'ly as many times as user inputs"""
def fibonacci(numba):
    """This will do the fibonacci"""
    if numba == 1:
        return numba
    return numba * fibonacci(numba-1)
print(fibonacci(int(input())))
