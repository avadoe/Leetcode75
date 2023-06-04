def gcdOfStrings(str1, str2):
    l1 = len(str1)
    l2 = len(str2)
    
    def isDivisor(l):
        if l1%l or l2%l:
            return False
        
        c1, c2 = l1//l, l2//l
        return str1[:l] * c1 == str1 and str1[:l] * c2 == str2
    
    for l in range(min(l1, l2), 0, -1):
        if isDivisor(l):
            return str1[:l]
        
    return ""