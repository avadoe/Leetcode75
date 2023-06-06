# int guess(int num) -> API returning -1 or 1 or 0

def guess(x):
    pass

def guessNumber(n):
    l, r = 1, n
    
    while l <= r:
        mid = l + (r - l)//2
        
        check = guess(mid)
        
        if check == -1:
            right = mid - 1
        elif check == 1:
            left = mid + 1
        else:
            return mid