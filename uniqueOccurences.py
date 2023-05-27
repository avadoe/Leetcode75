def uniqueOcc(list):
    hash_map = {}
    for i in list:
        if i in hash_map:
            hash_map[i] += 1
        else:
            hash_map[i] = 1
    l = []
    for key in hash_map:
        l.append(hash_map[key])
    
    return len(l) == len(set(l))

print(uniqueOcc([1, 1, 2, 4, 4, 4]))