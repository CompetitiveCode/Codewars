# Answer to Mumbling
# https://www.codewars.com/kata/mumbling/train/python


def accum(s):
    res = []
    for i in range(len(s)):
        temp = s[i].upper()
        for j in range(i):
            temp += s[i].lower()
        res.append(temp)
    return '-'.join(res)
