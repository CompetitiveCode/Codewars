# Answer to Find the odd int
# https://www.codewars.com/kata/find-the-odd-int/python


def find_it(seq):
    return [i for i in seq if seq.count(i) % 2 != 0][0]
