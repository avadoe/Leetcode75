from collections import deque

def predictPartyVictory(senate):
    senate = list(senate)
    
    R = deque()
    D = deque()
    
    for i, val in enumerate(senate):
        if val == 'R':
            R.append(i)
        else:
            D.append(i)
            
    while R and D:
        r = R.popleft()
        d = D.popleft()
        
        if r < d:
            R.append(d + len(senate))
        else:
            D.append(r + len(senate))
        
    return "Radiant" if not D else "Dire"