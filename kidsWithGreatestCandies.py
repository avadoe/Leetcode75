def kidsWithCandies(candies, extraCandies):
    max_can = -1
    for i in candies:
        if i > max_can: max_can = i
    new_arr = candies
    bool_arr = []
    for i in new_arr:
        i += extraCandies
        bool_val = True if i >= max_can else False
        bool_arr.append(bool_val)
        
    return bool_arr

bool_arr = kidsWithCandies([2, 3, 5, 1, 3], 3)
print(bool_arr)
        