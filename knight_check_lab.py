# Bryce Kelly
# COP 2500 0v64
# LAB 6.3
# Oct 18, 2022


def knight_check(word):
    song = '''UCF charge onto the field With our spirit we’ll never yield Black and gold Charge right through the line Victory is our cry V-I-C-T-O-R-Y Tonight our Knights will shine!'''
    song = song.split(" ")
    for x in song:
        if x == word:
            return True
        else:
            continue
    else:
        return False
