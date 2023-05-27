def findMaxAverage(nums, k):
    max_av = sum(nums[:k])
    sum_pres = sum(nums[:k])
    for i in range(k, len(nums)):
        sum_pres = sum_pres + nums[i] - nums[i - k]
        max_av = max(sum_pres, max_av)
        
    return max_av / float(k)

print(findMaxAverage([1,12,-5,-6,50,3], 4))