import re
p = [(4,1), (3,3), (2,0), (6,1), (3,2), (5,2), (1,1)]

def järjesta_punktid(p):
    for i in range(len(p)):
        min_id=i
        for j in range(i+1, len(p)):
            if p[min_id][1] > p[j][1] :
                min_id=j
            elif p[min_id][1]==p[j][1] and p[min_id][0] > p[j][0]:
                min_id=j
        p[i], p[min_id] = p[min_id], p[i]
  
        
        
print(järjesta_punktid(p))