def successfulPairs(spells, potions, success):
    successful_with_i = []
    
    for i in range(len(spells)):
        count = 0
        for j in range(len(potions)):
            if spells[i] * potions[j] >= success:
                count += 1
                
        successful_with_i.append(count)
        
    return successful_with_i

def successfulPairsBin(spells, potions, success):
    potions.sort()
    counts = []
    
    for spell in spells:
        idx = len(potions)
        left, right = 0, len(potions) - 1
        
        while left <= right:
            mid = (left + right)//2
            
            if spell * potions[mid] >= success:
                right = mid - 1
                idx = mid
            else:
                left = mid + 1
        counts.append(len(potions) - idx)
        
    return counts

print(successfulPairsBin(spells = [5,1,3], potions = [1,2,3,4,5], success = 7))