# Answer to Get the Middle Character
# https://www.codewars.com/kata/get-the-middle-character/train/python


def get_middle(s):
    l, lby2 = len(s), len(s)//2
    return s[lby2] if l % 2 == 1 else s[lby2-1:lby2+1]
