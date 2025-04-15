import math


TEMPLATES = {
    'П': [
        [1, 1, 1, 1, 1],
        [1, 0, 0, 0, 1],
        [1, 0, 0, 0, 1],
        [1, 0, 0, 0, 1],
        [1, 0, 0, 0, 1],
    ],
    'Г': [
        [1, 1, 1, 1, 1],
        [1, 0, 0, 0, 0],
        [1, 0, 0, 0, 0],
        [1, 0, 0, 0, 0],
        [1, 0, 0, 0, 0],
    ],
    'Е': [
        [1, 1, 1, 1, 1],
        [1, 0, 0, 0, 0],
        [1, 1, 1, 1, 0],
        [1, 0, 0, 0, 0],
        [1, 1, 1, 1, 1],
    ],
    'О': [
        [0, 1, 1, 1, 0],
        [1, 0, 0, 0, 1],
        [1, 0, 0, 0, 1],
        [1, 0, 0, 0, 1],
        [0, 1, 1, 1, 0],
    ],
    'Р': [
        [1, 1, 1, 0, 0],
        [1, 0, 0, 1, 0],
        [1, 1, 1, 0, 0],
        [1, 0, 0, 0, 0],
        [1, 0, 0, 0, 0],
    ],
    'Т': [
        [1, 1, 1, 1, 1],
        [0, 0, 1, 0, 0],
        [0, 0, 1, 0, 0],
        [0, 0, 1, 0, 0],
        [0, 0, 1, 0, 0],
    ],
}

input_matrix = [
    [1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0],
    [1, 1, 1, 0, 0],
    [1, 0, 1, 0, 0],
    [1, 1, 1, 1, 0],
]

def print_matrix(matrix):
    print("Введённая матрица:")
    for row in matrix:
        print("".join("#" if x else " " for x in row))
    print()

def diff_matrix(m1, m2):
    diff = 0
    for y in range(len(m1)):
        for x in range(len(m1[y])):
            if m1[y][x] != m2[y][x]:
                diff += 1
    return diff

def recognize_letter(matrix):
    result_letter = None
    min_diff = math.inf
    for letter, template in TEMPLATES.items():
        diff = diff_matrix(input_matrix, template)
        print(f'Контрольная сумма с буквой {letter} = {diff}')
        if diff < min_diff:
            min_diff = diff
            result_letter = letter
    return result_letter


print_matrix(input_matrix)
letter = recognize_letter(input_matrix)
print(f'Ввели букву: {letter}')