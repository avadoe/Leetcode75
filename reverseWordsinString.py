def reverseWordsInString(string):
    i, j = 0, 0
    string = list(string)
    while j < len(string):
        if j == len(string) - 1:
            k = j
            while i < k:
                temp = string[i]
                string[i] = string[k]
                string[k] = temp
                i += 1
                k -= 1
        elif string[j] == ' ':
            k = j
            while i < k:
                temp = string[i]
                string[i] = string[k - 1]
                string[k - 1] = temp
                i += 1
                k -= 1
            i = j + 1
        j += 1
        
    i, j = 0, len(string) - 1
    while i < j:
        temp = string[i]
        string[i] = string[j] 
        string[j] = temp
        i += 1
        j -= 1
        
    string = ''.join(string)
    return ' '.join(string.split())

ans = reverseWordsInString('this is a blue fox')
print(ans)