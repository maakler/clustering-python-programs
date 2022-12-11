p = [(4,1), (3,3), (2,0), (6,1), (3,2), (5,2), (1,1)]
def järjesta_punktid(A):
    for i in range(0, len(A)):
        for j in range(0, len(A)-i-1):
            if (A[j][1] > A[j + 1][1]):
                new_tem = A[j]  
                A[j]= A[j + 1]  
                A[j + 1]= new_tem
    for i in range(0, len(A)):
        for j in range(0, len(A)-i-1):
            if (A[j][1] == A[j + 1][1]) and(A[j][0] > A[j + 1][0]):
                tem = A[j]  
                A[j]= A[j + 1]  
                A[j + 1]= tem
                
järjesta_punktid(p)