import re

def is_isogram(string):
    arr = list(re.sub("[^a-zA-Z]+", "", string).lower())
    uniq = list(set(arr))
    return len(arr) == len(uniq)
