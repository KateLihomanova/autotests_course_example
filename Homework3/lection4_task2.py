def flatten_and_sort(array):
    result_list = []
    for i in array:
        for j in i:
            result_list.append(j)
    return sorted(result_list)

