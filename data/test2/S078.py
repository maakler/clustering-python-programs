def järjesta_punktid(p):
    for i in range(len(p)):
        min_idx = i
        for j in range(i+1, len(p)):
            if p[min_idx][1] > p[j][1]:
                min_idx = j
            elif p[min_idx][1] == p[j][1]:
                if p[min_idx][0] > p[j][0]:
                    min_idx = j
            
        p[i], p[min_idx] = p[min_idx], p[i]
        
    
    
    
    
p = [(4,1), (3,3), (2,0), (6,1), (3,2), (5,2), (1,1)]