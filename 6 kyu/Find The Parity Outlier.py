#Answer of Find The Parity Outlier - https://www.codewars.com/kata/find-the-parity-outlier/python

def find_outlier(integers):
    j,k,l,m=0,0,0,0
    for i in integers:
        if i%2==0:
            j=i
            k+=1
        else:
            l=i
            m+=1
    if(k==1):
        return j
    else:
        return l