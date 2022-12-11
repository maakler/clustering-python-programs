def järjesta_punktid(A):
    for i in range(0, len(A)-1):
        s = i
        for j in range(i, len(A)):
            a,b=A[j]
            c,d=A[s]
            if b<d:
                s = j
            elif b==d:
                if a < c:
                    s = j
        A[i], A[s] = A[s], A[i]
