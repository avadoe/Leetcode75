def asteroidCollision(asteroids):
    stack = []
    
    for asteroid in asteroids:
        if len(stack) == 0:
            stack.append(asteroid)
        elif asteroid > 0:
            stack.append(asteroid)
        else:
            while len(stack) > 0 and stack[-1] > 0 and stack[-1] < abs(asteroid):
                stack.pop()
            if len(stack) == 0 or stack[-1] < 0:
                stack.append(asteroid)
            elif stack[-1] == -asteroid:
                stack.pop()
                
    return stack