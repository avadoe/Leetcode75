def highestAltitude(gains): # This is a list of gains
    max_alt = 0
    curr_alt = 0
    for gain in gains:
        curr_alt += gain
        max_alt = max(max_alt, curr_alt)
        
    return max_alt
        
print(highestAltitude([-5, 1, 5, 0, -7]))