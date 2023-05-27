def pivotIndex(arr):
    left, right = 0, sum(arr)
    for i, x in enumerate(arr):
        right -= x
        if left == right:
            return i
        left += x
    return -1

print(pivotIndex([2, 1, -1]))
