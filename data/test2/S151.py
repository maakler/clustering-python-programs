import re

def järjesta_punktid(punkt):
    for i in range(len(punkt)):
        min = i
        for j in range(i+1, len(punkt)):
            if punkt[j][1] < punkt[min][1]:
                min = j
            elif punkt[j][1] == punkt[min][1]:
                if punkt[j][0] < punkt[min][0]:
                    min = j
        if i != min:
            punkt[i], punkt[min] = punkt[min], punkt[i]
    
    
    
    
    
p = [(3, 6), (5, 3), (2, 2), (2, 1), (3, 5), (4, 6)]
järjesta_punktid(p)
print(p)