# Answer to You're a square!
# https://www.codewars.com/kata/youre-a-square/train/python

from math import sqrt


def is_square(n):
    if n > 0:
        return sqrt(n) == int(sqrt(n))
    elif n == 0:
        return True
    return False
