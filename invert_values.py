# Given a set of numbers, return the additive inverse of each.
# Each positive becomes negatives, and the negatives become positives.


def invert(lst):
    return [x and -x for x in lst]

def invert(lst):
    return [-x for x in lst]

def invert(lst):
   return [i*-1 for i in lst]


print(invert([1, 2, 3, -4]))

