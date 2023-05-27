from collections import Counter

def closeStrings(s1, s2):
    if Counter(s1) != Counter(s2):
        return False
    if set(s1) != set(s2):
        return False
    return True

print(closeStrings('a', 'aa'))