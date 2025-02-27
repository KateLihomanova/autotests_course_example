def even_sum(lst):
    sum_list = 0
    for i in lst:
        if lst.index(i)%2 == 0:
            sum_list = sum_list+i
    return sum_list




