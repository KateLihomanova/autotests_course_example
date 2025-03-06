def which_triangle(a, b, c):
    if a == b == c:
        type_triangle = "Равносторонний"
    elif a == b or a == c or b == c:
        type_triangle = "Равнобедренный"
    elif a+b == c or b+c == a or c+a == b:
        type_triangle = "Не треугольник"
    else:
        type_triangle = "Обычный"
    return type_triangle



