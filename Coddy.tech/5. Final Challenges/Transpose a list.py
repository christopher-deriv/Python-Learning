def transpose(lst):
    rows = len(lst)
    cols = len(lst[0])

    transposed_lst = [[0] * rows for _ in range(cols)]

    for i in range(rows):
        for j in range(cols):
            transposed_lst[j][i] = lst[i][j]
    return(transposed_lst)