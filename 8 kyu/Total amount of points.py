#Answer to Total amount of points - https://www.codewars.com/kata/total-amount-of-points/python

def points(games):
    result = 0
    for i in games:
        j = i.split(':')
        if j[0] > j[1]:
            result+=3
        elif j[0] == j[1]:
            result += 1
    return result