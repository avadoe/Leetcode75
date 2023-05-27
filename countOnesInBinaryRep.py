def countOnes(num):
    l = []
    for i in range(num + 1):
        count = 0
        while i:
            count += i & 1
            i = i >> 1
        l.append(count)
    return l
        
print(countOnes(5))