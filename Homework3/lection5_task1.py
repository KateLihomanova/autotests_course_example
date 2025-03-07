def letter_stat(our_str):
    letters_dict = {item: our_str.count(item) for item in our_str}
    return letters_dict


