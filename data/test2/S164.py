def järjesta_punktid(järjend):
    selection_sort(järjend)
    
    

def selection_sort(A):
    for i in range(0, len(A)-1):
        s = i
        for j in range(i, len(A)):
            if A[j][1] < A[s][1] or A[j][1] == A[s][1] and A[j][0] < A[s][0]:
                s = j
                
        A[i], A[s] = A[s], A[i]
        
p = [(4,1), (3,3), (2,0), (6,1), (3,2), (5,2), (1,1)]
järjesta_punktid(p)        
print(p)