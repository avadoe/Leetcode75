def minArrows(points):
    points.sort()
    curr = points[0]
    
    count = 1
    
    for i in range(1, len(points)):
        if points[i][0] > curr[1]:
            count += 1
            curr = points[i]
            
        else:
            curr[1] = min(curr[1], points[i][1])
            
    return count

