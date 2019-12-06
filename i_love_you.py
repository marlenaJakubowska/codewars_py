# Who remembers the time where in the schoolyard, girls take flower petals. Tears saying:
# I love you
# a little
# a lot
# passionately
# madly
# not at all
# When the last petal torn comes to the word 'madness', these are cries of excitement,
# dreams and emotions surging in thoughts.
# Your goal in this kata is to define the result of such a game given nb_petals > 0, the number of petals torn.


def how_much_i_love_you(nb_petals):
    if nb_petals % 6 == 1:
        return "I love you"
    elif nb_petals % 6 == 2:
        return "a little"
    elif nb_petals % 6 == 3:
        return "a lot"
    elif nb_petals % 6 == 4:
        return "passionately"
    elif nb_petals % 6 == 5:
        return "madly"
    else:
        return "not at all"


def how_much_i_love_you2(nb_petals):
    msg = ["I love you", "a little", "a lot", "passionately", "madly", "not at all"]
    return msg[(nb_petals - 1) % len(msg)]
