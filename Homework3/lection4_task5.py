def josephus_task(num_people, kill_num):
    survivor = list(range(1, num_people + 1))
    idx = 0
    while len(survivor) > 1:
        idx = (idx + kill_num - 1) % len(survivor)
        survivor.pop(idx)
    return survivor[0]


