def stringCompression(chars):
    n = len(chars)
    i, j = 0, 0
    
    while j < n:
        curr_char = chars[j]
        count = 1
        
        while j + 1 < n and chars[j + 1] == chars[j]:
            count += 1
            j += 1
            
        chars[i] = curr_char
        i += 1
        
        if count > 1:
            count_str = str(count)
            for digit in count_str:
                chars[i] = digit
                i += 1
                
        j += 1
        
    return i

print(stringCompression(['a', 'a', 'b', 'b']))