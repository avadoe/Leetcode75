def moveZeroes(arr):
    left, right = 0, 0
    n = len(arr)
    while right < n:
        if arr[right] == 0:
            right += 1
        else:
            temp = arr[left]
            arr[left] = arr[right]
            arr[right] = temp
            left += 1
            right += 1
            
    return arr

print(moveZeroes([0, 1, 0, 2, 3, 0, 4]))