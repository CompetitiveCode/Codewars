# Answer to Simple Pig Latin
# https://www.codewars.com/kata/simple-pig-latin/python


def pig_it(text):
    return ' '.join([i[1:]+i[0]+'ay' if i[0].isalpha() else i for i in text.split()])
