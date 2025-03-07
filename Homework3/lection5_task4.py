def scrabble(word):
    counts = {1: ['а', 'в', 'е', 'ё', 'и', 'н', 'о', 'р', 'с', 'т'], 2: ['д', 'к', 'л', 'м', 'п', 'у'], 3: ['б', 'г', 'ь', 'я'], 4: ['й', 'ы'], 5: ['ж', 'з', 'х', 'ц', 'ч'], 8: ['ф', 'ш', 'э', 'ю'], 10: ['щ'], 15: ['ъ']}
    points = 0
    for i in word:
        for key, values in counts.items():
            if i in values:
                points = points + key

    return points

