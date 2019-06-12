# Answer to Moving Zeros To The End
# https://www.codewars.com/kata/moving-zeros-to-the-end/python\


def move_zeros(array):
    a,b = [],[]
    for i in array:
        try:
            if int(i) == 0 and str(i) != 'False' and i != '0':
                b.append(i)
            else:
                a.append(i)
        except:
            a.append(i)
    a.extend(b)
    return a
