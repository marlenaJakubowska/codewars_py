# 1 solution
def disemvowel(string):
    return "".join(char for char in string if char.lower() not in "aeiou")

# 2 solution


def disemvowel(s):
    for i in "aeiouAEIOU":
        s = s.replace(i, '')
    return s


# 3 solution using re

import re


def disemvowel(string):
    return re.sub(r"[aeiouAEIOU]", "", string)


# 4 solution


def disemvowel(string):
    s = ""
    for c in string:
        if c.lower() not in "aeiou":
            s += c
    return s

# 5 solution using lambda. not sure if working

# def disemvowel(string):
#     v = 'aeiouAEIOU'
#     return filter(lambda x: x not in v, string)

# 6 solution my


def disemvowel(string):
    vowels = 'aeiouAEIOU'
    new_string = ''
    for i in string:
        if i not in vowels:
            new_string += i
    return new_string


print(disemvowel("This string should not have any vowels. Is it working?"))
