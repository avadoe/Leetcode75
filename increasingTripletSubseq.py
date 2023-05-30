def increasingTriplet(nums):
    positive_inf = float('inf')
    
    n = len(nums)
    left = positive_inf
    middle = positive_inf
    
    for i in range(n):
        right = nums[i]
        
        if right < left:
            left = right

        elif right < middle and right > left:
            middle = right
            
        elif right > middle and right > left: return True
        
    return False


            
    