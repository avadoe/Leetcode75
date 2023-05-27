def reverseVowels(s):    
    vowels = set('aeiouAEIOU')
    s = list(s)
    t1, t2 = 0, len(s) - 1
    
    while t1 < t2:
        if s[t1] not in vowels: t1 += 1
        elif s[t2] not in vowels: t2 -= 1
        else:
            s[t1], s[t2] = s[t2], s[t1]
            t1 += 1
            t2 -= 1
            
        
    ans = ''
    for i in s:
        ans += i
    return ans

s = reverseVowels('hello')
print(s)
        