#Answer to Sum of positive - https://www.codewars.com/kata/sum-of-positive/python

def positive_sum(arr):
    return max(0,sum([i for i in arr if i > 0]))
