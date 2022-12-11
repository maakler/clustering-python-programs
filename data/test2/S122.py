def järjesta_punktid(järjend):
    n = len(järjend) 
    for i in range(n):
        for j in range(i+1, n):
            if järjend[i][1]>järjend[j][1]:
                järjend[i],järjend[j]=järjend[j],järjend[i]
            elif järjend[i][1] == järjend[j][1]:
                x_koord1, x_koord2 = järjend[i][0],järjend[j][0]
                if x_koord2 < x_koord1:
                    järjend[i],järjend[j]=järjend[j],järjend[i]
                
#print(järjesta_punktid([(4,1), (3,3), (2,0), (6,1), (3,2), (5,2), (1,1)]))