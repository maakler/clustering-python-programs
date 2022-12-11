def järjesta_punktid(A):
    for i in range(len(A)):
        min_indeks = i
        for j in range(i+1, len(A)):
            if A[min_indeks][1] > A[j][1] or (A[min_indeks][1] == A[j][1] and A[min_indeks][0] > A[j][0]):
                min_indeks = j
        A[i], A[min_indeks] = A[min_indeks], A[i]