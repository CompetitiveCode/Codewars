# Answer to Sum of Digits / Digital Root
# https://www.codewars.com/kata/sum-of-digits-slash-digital-root/python


def digital_root(n):
    res = sum(int(i) for i in str(n))
    return res if res < 10 else digital_root(res)
