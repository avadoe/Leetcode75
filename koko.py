import math

def minEatingSpeed(piles, h):
    l, r = 0, max(piles)
    ans = r
    while l <= r:
        mid = l + (r - l)//2
        hours = 0
        for pile in piles:
            hours += math.ceil(pile/mid)
            
        if hours <= h:
            ans = min(ans, mid)
            r = mid - 1
        else:
            l = mid + 1
            
    return ans

print(minEatingSpeed(piles = [3, 6, 7, 11], h = 8))