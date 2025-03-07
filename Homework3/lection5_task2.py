def repeats(our_str):
    new_str = [i+'_'+str(our_str.count(i, 0, item+1)) for item, i in enumerate(our_str)]
    return ''.join(new_str)

