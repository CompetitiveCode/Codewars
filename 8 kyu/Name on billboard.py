#Answer to Name on billboard - https://www.codewars.com/kata/name-on-billboard

def billboard(name, price=30):
    res = 0
    for i in name:
        res += price
    return res