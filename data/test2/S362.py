def järjesta_punktid(p):
    if len(p)>2:
        for i in range(len(p)):
            for j in range(i+1,len(p)):
                if p[i][1]>p[j][1]:
                    p[i], p[j] = p[j], p[i]
                    
        for i in range(len(p)):
            for j in range(i+1,len(p)):
                if p[i][1]==p[j][1] and p[i][0]>p[j][0]:
                    p[i], p[j] = p[j], p[i]
    elif len(p)==2:
        for i in range(len(p)):
            for j in range(i+1,len(p)):
                if p[i][1]>p[j][1]:
                    p[i], p[j] = p[j], p[i]
        
            
            
    
p=[(4,1), (3,3), (2,0), (6,1), (3,2), (5,2), (1,1)]
j=[(4,1), (3,3), (2,0), (6,1), (3,2), (5,2)]
n=[(4,1), (3,3), (2,0), (6,1), (3,2)]
m=[(4,1), (3,3), (2,0), (6,1)]
l=[(4,1), (3,3), (2,0)]
o=[(4,1), (3,3)]
k=[(4,1)]

järjesta_punktid(p)
#[(2, 0), (1, 1), (4, 1), (6, 1), (3, 2), (5, 2), (3, 3)]