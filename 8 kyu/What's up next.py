#Answer to What's up next? - https://www.codewars.com/kata/whats-up-next/python

import collections
import itertools
def next_item(xs, item):
    if isinstance(xs, collections.Iterator):
        if item in xs:
            xs1 = []
            xs1.extend(itertools.islice(xs, 2))
            if len(xs1) == 2:
                return item+xs1[1]-xs1[0]
    else:
        try:
            index = xs.index(item)
            if index+1 < len(xs):
                return xs[index+1]
        except ValueError:
            return None
    return None