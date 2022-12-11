def järjesta_punktid(A):
    for i in range(0, len(A)-1):
        s = i
        for j in range(i, len(A)):
            if A[j][1] < A[s][1]:
                s = j
            elif A[j][1] == A[s][1]:
                if A[j] < A[s]:
                    s=j
        A[i], A[s] = A[s], A[i]
    
        
    
        
    

A = [(4,1), (3,3), (2,0), (6,1), (3,2), (5,2), (1,1)]
järjestatud = järjesta_punktid(A)

#Ül lahendamise inspiratsiooni sain: https://et.wikipedia.org/wiki/Valiksortimine
