def järjesta_punktid(jrn):
    a = []
    for el in jrn:
        a.append(el[1])
    for i in range(len(jrn)):
        vähim = i
        for j in range(i+1, len(jrn)):
            if a[j] < a[vähim]:
                vähim=j
            if i != vähim:
                a[i], a[vähim] = a[vähim], a[i]
                jrn[i], jrn[vähim] = jrn[vähim], jrn[i]
    return (jrn)