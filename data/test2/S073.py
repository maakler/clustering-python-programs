def järjesta_punktid(h):
    arr = list()
    for i in h:
        arr.append((i[1], i[0]))

    n = len(arr)

    for i in range(n):
        for j in range(0, n - i - 1):

            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    p = list()
    count = 0
    for l in arr:
        h[count] = ((l[1], l[0]))
        count+=1
