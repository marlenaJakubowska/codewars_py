# 1 soution

def song_decoder(song):
    song = song.split('WUB')
    original_song = []
    for item in song:
        if item != '':
            original_song += [item]
    return ' '.join(original_song)


# 2 solution

def song_decoder(song):
    return " ".join(song.replace('WUB', ' ').split())


# 3 solution

def song_decoder(song):
    return ' '.join([a for a in song.split('WUB') if a])


# 4 solution

def song_decoder(song):
    # Splitting strings by "WUBs" and filtering out voids
    list = filter(lambda x: x != '', song.split('WUB'))

    # Returning the joint items separed by spaces
    return ' '.join(list)


# 5 solution

def song_decoder(song):
    return ' '.join(word for word in song.split('WUB') if word)


# 6 solution

def song_decoder(song):
    return ' '.join(filter(None, song.split('WUB')))


# 7 solution

def song_decoder(song):
    s = song.replace("WUB"," ").replace("  "," ").strip(" ")
    while "  " in s: s=s.replace("  "," ")
    return s


print(song_decoder("AWUBWUBWUBBWUBWUBWUBC"))
