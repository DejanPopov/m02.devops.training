import math


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


def power(base, exponent):
    if exponent < 0:
        raise ValueError("Exponent must be non-negative")
    return base ** exponent


def square_root(n):
    if n < 0:
        raise ValueError("Cannot take square root of negative number")
    return math.sqrt(n)


def modulo(a, b):
    if b == 0:
        raise ValueError("Cannot modulo by zero")
    return a % b


def is_even(n):
    return n % 2 == 0


def is_positive(n):
    return n > 0


def factorial(n):
    if n < 0:
        raise ValueError("n must be non-negative")
    if n <= 1:
        return 1
    return n * factorial(n - 1)
