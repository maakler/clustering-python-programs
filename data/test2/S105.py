def järjesta_punktid(a):
    for i in range(len(a)):
        key=a[i][1]
        key0=a[i][0]
        j=i-1
        while j>=0 and key<=a[j][1]:
            if key==a[j][1] and key0<a[j][0]:
                a[j+1]=(a[j][0],a[j][1])
                j-=1
            elif key==a[j][1] and key0>=a[j][0]:
                break
            else:
                a[j+1]=(a[j][0],a[j][1])
                j-=1
        a[j+1]=(key0, key)