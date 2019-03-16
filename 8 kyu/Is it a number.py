#Answer to Is it a number? - https://www.codewars.com/kata/is-it-a-number

def isDigit(string):
    try:
        text = float(string)
        return True
    except ValueError:
        return False