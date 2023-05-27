def minFlips(a, b, c):
    flips = 0
    for i in range(32):
        bit_a = (a >> i) & 1
        bit_b = (b >> i) & 1
        bit_c = (c >> i) & 1
        
        if bit_a | bit_b != bit_c:
            if not bit_c:
                if bit_a == 1 and bit_b == 1:
                    flips += 2
                else:
                    flips += 1
                    
            else:
                flips += 1
                
    return flips
        