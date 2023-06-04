def decodeString(str):
    stack = []
    if len(str) == 0: return ''
    
    for i in range(len(str)):
        if str[i] != ']':
            stack.append(str[i])
        else:
            substr = ''
            while stack[-1] != '[':
                substr = stack.pop() + substr
            stack.pop()
            
            k = ''
            while stack and stack[-1].isdigit():
                k = stack.pop() + k 
                
            stack.append(int(k) * substr)
    return ''.join(stack)

print(decodeString('3[a2[b3[c]]]'))