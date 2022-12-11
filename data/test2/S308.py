p = [(4,1), (3,3), (2,0), (6,1), (3,2), (5,2), (1,1)]
def järjesta_punktid(A):
    for i in range(0, len(A)-1):
        s = i
        for j in range(i, len(A)):
            if A[j] < A[s]:
                s = j
        A[i], A[s] = A[s], A[i]
        
print(järjesta_punktid(p))