def sum_digits(num):
    our_sum = 0
    num = str(num)
    for i in num:
        our_sum = our_sum + int(i)
    return our_sum

