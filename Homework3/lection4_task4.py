def multiplication_chain(num):
    count_multy = 0
    while num > 9:
        digits = str(num)
        product = 1
        for digit in digits:
            product *= int(digit)
        num = product
        count_multy += 1
    return count_multy


