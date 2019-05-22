# Answer to Weight for weight
# https://www.codewars.com/kata/weight-for-weight/python


# Compressed way
def order_weight(strng):
    temp = []
    for i in strng.split():
        j = sum(int(k) for k in str(i))
        temp.append([i,j])
    return ' '.join([str(i[0]) for i in sorted(temp,key=lambda i:(i[1],str(i[0])))])

"""
#Understandable way:

def order_weight(strng):
    temp = []
    for i in strng.split():
        j = 0
        for k in str(i):
            j += int(k)
        temp.append([i,j])
    temp = sorted(temp,key=lambda i:(i[1],str(i[0])))
    t = [str(i[0]) for i in temp]
    return ' '.join(t)
"""
