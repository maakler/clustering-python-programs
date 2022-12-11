
def järjesta_punktid(p):
    for i in range(len(p)):
        kes = p[i]
        minnike1 = kes[0]
        minnike2 = kes[1]
        for j in range(i+1, len(p)):
            if p[j][1] < minnike2:
                kes2 = p[j]
                minnike1 = kes2[0]
                minnike2 = kes2[1]
            elif p[j][1] == minnike2:
                if p[j][0] < minnike1:
                    kes2 = p[j]
                    minnike2 = kes2[1]
                
        if p[i][1] != minnike2:
            index = p.index(kes2)
            p[i], p[index] = p[index], p[i]
        
p = [(4,1), (3,3), (2,0), (6,1), (3,2), (5,2), (1,1)]
järjesta_punktid(p)
print(p)