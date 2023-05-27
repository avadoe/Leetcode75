def singleNumber(nums):
    ans = 0
    for i in nums:
        ans ^= i
        
    return ans

print(singleNumber([1, 2, 2, 3, 4, 4, 3]))