#Answer to Who is going to pay for the wall? - https://www.codewars.com/kata/who-is-going-to-pay-for-the-wall

def who_is_paying(name):
    result = []
    result.append(name)
    if len(name) > 2:
        result.append(name[0]+name[1])
    return result