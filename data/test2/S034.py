def järjesta_punktid(järjend):
    for i in range(0,len(järjend)-1):
         s = i
         for j in range(i,len(järjend)):
             if järjend[j][1] < järjend[s][1]:
                 s = j
             järjend[i],järjend[s] = järjend[s], järjend[i]
             
    for i in range(0,len(järjend)-1):
         s = i       
         for j in range(i,len(järjend)):
             s = i 
             if järjend[j][1] == järjend[s][1]:
                 if järjend[j][0] < järjend[s][0]:
                     s=j
                 järjend[i],järjend[s] = järjend[s], järjend[i]