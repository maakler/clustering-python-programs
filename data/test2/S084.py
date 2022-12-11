def järjesta_punktid(lst):
    while True:
        vahetus = False
        for i in range(len(lst)-1):
            if lst[i][1] > lst[i+1][1] or (lst[i][0] > lst[i+1][0] and lst[i][1] == lst[i+1][1]):
                lst[i], lst[i+1] = lst[i+1], lst[i]
                vahetus = True
        if not vahetus:
            break