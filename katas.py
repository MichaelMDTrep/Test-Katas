#!/usr/bin/env python3
"""
Math functions to be tested with test_katas.py

Students should not change this file.
"""

__author__ = 'madarp and Q3 friends'


def add(x, y):
    """Return the result of adding x to y."""
    return x + y


def multiply(x, y):
    """Return the result of multiplying x by y."""
    result = 0
    for _ in range(abs(y)):
        result = add(result, x)
    return -result if y < 0 else result


def power(x, n):
    """Return the result of taking x to the nth power."""
    # Negative and fractional powers are not allowed
    if n < 0:
        raise ValueError('n cannot be negative')
    elif 0 < n < 1.0:
        raise ValueError('n cannot be fractional')

    result = 1
    for _ in range(n):
        result = multiply(result, x)
    return result


def factorial(n):
    """Return the result of calculating the factorial of n."""
    if n < 0:
        raise ValueError("n cannot be negative")
    result = 1
    for i in range(1, n + 1):
        result = multiply(result, i)
    return result


def fibonacci(n):
    """Returns the nth term of the Fibonacci sequence, starting from 0."""
    if n < 0:
        raise ValueError("n cannot be negative")
    elif n < 2:
        return n
    else:
        a, b = 0, 1
        for _ in range(n):
            a, b = b, add(a, b)
        return a


def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print('{} got: {}     expected: {}'.format(
        prefix,
        repr(got),
        repr(expected)))


def main():
    add(2, 4)
    print(add(2, 4))
    multiply(6, -8)
    print(multiply(6, -8))
    power(2, 8)
    print(power(2, 8))
    factorial(4)
    print(factorial(4))
    fibonacci(8)
    print(fibonacci(0))
    print(fibonacci(1))
    print(fibonacci(2))
    print(fibonacci(3))
    print(fibonacci(4))
    print(fibonacci(5))
    print(fibonacci(6))
    print(fibonacci(7))
    print(fibonacci(8))

# print('add')
# print('\nmultiply')
# print('\npower')
# print('\nfactorial')
# print('\nfibonacci')


if __name__ == '__main__':
    main()
