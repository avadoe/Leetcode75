def eraseOverlappingIntervals(intervals):
    n = len(intervals)
    
    intervals.sort()
    
    num_to_remove = 0
    prevEnd = intervals[0][1]
    
    for start, end in intervals[1: ]:
        if start >= prevEnd:
            prevEnd = end
        else:
            num_to_remove += 1
            prevEnd = min(prevEnd, end)
            
    return num_to_remove

print(eraseOverlappingIntervals([[1,2],[1,2],[1,2]]))