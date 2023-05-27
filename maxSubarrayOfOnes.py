def maxSubarray(nums):
    prev_count, curr_count, max_count = 0, 0, 0
    if 0 not in nums:
        return len(nums) - 1
    for i in range(len(nums)):
        if nums[i] == 1:
            curr_count += 1
        else:
            max_count = max(max_count, curr_count + prev_count)
            prev_count = curr_count
            curr_count = 0
    max_count = max(max_count, curr_count + prev_count)
    return max_count
    

print(maxSubarray([1, 1, 1, 0, 1, 0, 0, 1]))
