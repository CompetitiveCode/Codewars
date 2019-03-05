#Answer to Thinkful - Number Drills: Blue and red marbles - https://www.codewars.com/kata/thinkful-number-drills-blue-and-red-marbles

def guess_blue(blue_start, red_start, blue_pulled, red_pulled):
    return (blue_start-blue_pulled)/(blue_start-blue_pulled+red_start-red_pulled)