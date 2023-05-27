def diffOfArrays(a1, a2):
    r1 = []
    r2 = []
    for i in a1:
        if i not in a2 and i not in r1:
            r1.append(i)
    for i in a2:
        if i not in a1 and i not in r2:
            r2.append(i)
            
    r = []
    r.append(r1)
    r.append(r2)
    return r

print(diffOfArrays([1, 2, 3, 3], [1, 1, 2, 2]))