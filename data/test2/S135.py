# bubble sort
def järjesta_punktid(li):
    n = len(li)
    for i in range(n):
        for j in range(n - i - 1):
            if li[j][1] > li[j + 1][1]:
                li[j], li[j + 1] = li[j + 1], li[j]
            if li[j][1] == li[j + 1][1] and li[j][0] > li[j + 1][0]:
                li[j], li[j + 1] = li[j + 1], li[j]

p = [(4,1), (3,3), (2,0), (6,1), (3,2), (5,2), (1,1)]
järjesta_punktid(p)
print(p)