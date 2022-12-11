def järjesta_punktid(nimekiri):
    for a in nimekiri:
        if nimekiri[nimekiri.index(a)][1] > nimekiri[nimekiri.index(a)+1][1]:
            if nimekiri[nimekiri.index(a)][1] == nimekiri[nimekiri.index(a)+1][1]:
                if nimekiri[nimekiri.index(a)][0] > nimekiri[nimekiri.index(a)+1][0]:
                    vahepealne = nimekiri[nimekiri.index(a)+1]
                    nimekiri[nimekiri.index(a)+1] = nimekiri[nimekiri.index(a)]
                    nimekiri[nimekiri.index(a)] = vahepealne
                
            else:
                vahepealne = nimekiri[nimekiri.index(a)+1]
                nimekiri[nimekiri.index(a)+1] = nimekiri[nimekiri.index(a)]
                nimekiri[nimekiri.index(a)] = vahepealne
        else:
            continue
        return nimekiri
            
    
    
    
p = [(6,1), (3,3), (2,0), (4,1), (3,2), (5,2), (1,1)]
print(järjesta_punktid(p))
uus = järjesta_punktid(p)
k = järjesta_punktid(uus)
k = järjesta_punktid(k)
k = järjesta_punktid(k)

print(k)
    