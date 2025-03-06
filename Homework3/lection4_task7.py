def move_zeros(lst):
    non_zero_elements = [x for x in lst if x != 0]
    zeros = [0] * lst.count(0)
    return non_zero_elements + zeros


