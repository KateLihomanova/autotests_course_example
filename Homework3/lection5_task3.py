def everything_for_your_cat(cats_data):
    owners = {}
    for cat_name, age, first_name, last_name in cats_data:
        owner_key = f"{first_name} {last_name}"
        if owner_key not in owners:
            owners[owner_key] = []
        owners[owner_key].append(f"{cat_name}, {age}")
    our_str = ""
    for owner, cats in owners.items():
        our_str += f"{owner}: {'; '.join(cats)}\n"
    return our_str.strip()

