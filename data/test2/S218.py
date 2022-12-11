def järjesta_punktid(p):

    for i in range(len(p)):

        vähim = i

        for j in range(i + 1, len(p)):
            if p[j][1] < p[vähim][1]:
                
                vähim = j

        p[i], p[vähim] = p[vähim], p[i]
    for i in range(len(p)):

        vähim = i

        for j in range(i + 1, len(p)):
            if p[j][1] == p[vähim][1] and p[j][0] < p[vähim][0]:
                
                vähim = j

        p[i], p[vähim] = p[vähim], p[i]
nums = [(4,1), (3,3), (2,0), (6,1), (3,2), (5,2), (1,1)]
järjesta_punktid(nums)
print(nums)