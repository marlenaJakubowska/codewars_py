# """a new string where each character in the new string is '('
#     if that character appears only once in the original word, or ')'
#     if that character appears more than once in the original word.
#     Ignores capitalization when determining if a character is a duplicate. """

# 1 solution

# importing counter from collections
# from collections import Counter

# def duplicate_encode(word):
#     word = word.lower()       # making sure that it's fool friendly
#     word = list(word)         # changing the word to list
#     count = Counter(word)     # using the counter

#     result = ''

#     for char in word:
#         if count[char] == 1:
#             result += "("
#         else:
#             result += ")"
#     return result

# 2 solution


def duplicate_encode(word):
    word = word.lower()
    return "".join(["(" if word.lower().count(c) == 1 else ")" for c in word.lower()])

# 3 solution:


def duplicate_encode(word):

    word = word.upper()
    result = ""
    for char in word:
        if word.count(char) > 1:
            result += ")"
        else:
            result += "("

    return result


# 4 solution

def duplicate_encode(word):
    word = word.lower()
    new_word = ""
    char_count = {}
    for char in word:
        if char not in char_count:
            char_count[char] = 1
        else:
            char_count[char] += 1
    print(char_count)

    for char in word:
        if char_count[char] > 1:
            new_word += ")"
        else:
            new_word += "("
    return new_word


print(duplicate_encode("Truchełkoełko"))
