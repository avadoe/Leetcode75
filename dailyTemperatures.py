def dailyTemperatures(temperatures):
    ans = [0] * len(temperatures)
    for i in range(0, len(temperatures) - 1):
        for j in range(i + 1, len(temperatures)):
            if temperatures[j] > temperatures[i]:
                ans[i] = j - i
                break
                
    return ans

def dailyTemperatures(self, temperatures):
    stack = []
    ans = [0] * len(temperatures)
    stack.append(len(temperatures) - 1)
    for i in range(len(temperatures) - 2, -1, -1):
        while stack and temperatures[stack[-1]] <= temperatures[i]:
            stack.pop()
        
        ans[i] = stack[-1] - i if stack else 0
        stack.append(i)
        
    return ans
