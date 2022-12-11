#--- Kasutasin Bubble Sort'i----

def järjesta_punktid(jarjend):
    lst_lenght = len(jarjend)
    sorted_ = False
    while not sorted_:
        sorted_counter = 1
        for i in range(lst_lenght - 1):
            if jarjend[i][1] > jarjend[i+1][1] or jarjend[i][1] == jarjend[i+1][1] \
            and jarjend[i][0] > jarjend[i+1][0]:
                jarjend[i], jarjend[i+1] = jarjend[i+1], jarjend[i]
                
            else:
                sorted_counter += 1

        if sorted_counter == lst_lenght:
            sorted_ = True

    