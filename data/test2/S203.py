def järjesta_punktid(p):
    for i in range(len(p)):
        minrea_nr = p[i]
        for j in range(i+1, len(p)):
            rea_nr2 = p[j][1]
            if rea_nr2 < minrea_nr[1]:
                minrea_nr = p[j]
                minrea_nr_indeks = j
            elif rea_nr2 == minrea_nr[1]:
                veeru_nr1 = p[i][0]
                veeru_nr2 = p[j][0]
                if veeru_nr2 < veeru_nr1:
                   minrea_nr = p[j]
                   minrea_nr_indeks = j
        if p[i] != minrea_nr:
            p[i], p[minrea_nr_indeks] = p[minrea_nr_indeks], p[i]
               
# järjesta_punktid(p)
# print(p)