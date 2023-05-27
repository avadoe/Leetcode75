def mergeStringsAlt(word1, word2):
    t1, t2 = 0, 0
    flag = 0
    ans = ''
    toTrav = min(len(word1), len(word2))
    while t1 < toTrav or t2 < toTrav:
        if not flag:
            ans += word1[t1]
            t1 += 1
        else:
            ans += word2[t2]
            t2 += 1
        flag = not flag
    if toTrav == len(word1):
        while t2 < len(word2):
            ans += word2[t2]
            t2 += 1
    else:
        while t1 < len(word1):
            ans += word1[t1]
            t1 += 1
            
    return ans

ans = mergeStringsAlt('abcd', 'pq')
print(ans)