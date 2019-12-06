# An isogram is a word that has no repeating letters, consecutive or non-consecutive.
# Implement a function that determines whether a string that contains only letters is an isogram.
# Assume the empty string is an isogram. Ignore letter case.

# 1 solution using set which drops additional same characters so the length is not the same


def is_isogram(s):
    s = s.lower()
    return len(set(s)) == len(s)


# 2 solution


def is_isogram(string):
    string = string.lower()
    for letter in string:
        if string.count(letter) > 1: return False
    return True


print(is_isogram("Dermatoglyphics"))
print(is_isogram("moOse"))
