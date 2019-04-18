# Answer to Vowel Count
# https://www.codewars.com/kata/vowel-count/train/python


def getCount(inputStr):
    return sum(1 for i in inputStr if i in ['a', 'e', 'i', 'o', 'u'])
