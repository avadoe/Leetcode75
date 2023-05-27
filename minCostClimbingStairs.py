def minCost(nums):
    dp = [0] * len(nums)
    dp[0] = nums[0]
    dp[1] = nums[1]
    
    for i in range(2, len(nums)):
        dp[i] = min(dp[i - 1], dp[i - 2]) + nums[i]
    return min(dp[-1], dp[-2])

print(minCost([10, 15, 20]))