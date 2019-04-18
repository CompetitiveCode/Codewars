# Answer to Disemvowel Trolls
# https://www.codewars.com/kata/disemvowel-trolls/train/python


def disemvowel(string):
    return ''.join(i for i in string if i not in 'aeiouAEIOU')
