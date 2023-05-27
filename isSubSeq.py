def isSubSequence(s, t):
    s = list(s)
    t = list(t)
    
    for c in s:
        if c not in t:
            return False
        
    a, b = 0, 0
    while a < len(s):
        while b < len(t):
            if a < len(s) and b < len(t) and t[b] == s[a]:
                a += 1
                b += 1
            else:
                b += 1
        if b == len(t) and a != len(s):
            return False
        
    return True

    
print(isSubSequence('axc', 'acbd'))