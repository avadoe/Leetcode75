def maxVowelsInSubstring(string, k):
    string = list(string)
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    left, right = 0, 0
    present_count, max_count = 0, 0
    while right < k:
        if string[right] in vowels:
            present_count += 1
        right += 1
    max_count = max(max_count, present_count)
    
    while right < len(string):
        if string[right] in vowels:
            present_count += 1
        if string[left] in vowels:
            present_count -= 1
        left += 1
        right += 1
        max_count = max(max_count, present_count)
        
    return max_count

print(maxVowelsInSubstring("abciiidef", 3))