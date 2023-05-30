def combinationalSum3(k, n):
    ans = []
    
    def backtrack(start, so_far, remaining):
        if len(so_far) == k and remaining == 0:
            ans.append(so_far[:])
            return 
        
        if len(so_far) > k or remaining < 0:
            return 
        
        for i in range(start, 10):
            so_far.append(i)
            backtrack(i + 1, so_far=so_far, remaining=remaining - i)
            so_far.pop()
            
    backtrack(1, [], n)
    return ans
    
print(combinationalSum3(3, 10))