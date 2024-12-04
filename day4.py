word_matrix = []
with open("input.txt", "r") as file:
    for line in file:
        word_matrix.append(list(line.strip()))

def num_xmas(word_matrix, x, y):
    xmas_count = 0
    max_y = len(word_matrix)
    max_x = len(word_matrix[0])
    # Check to the right
    if x + 3 < max_x and word_matrix[y][x + 1] == "M" and word_matrix[y][x + 2] == "A" and word_matrix[y][x + 3] == "S":
        xmas_count += 1
    # Check to the left
    if x - 3 >= 0 and word_matrix[y][x - 1] == "M" and word_matrix[y][x - 2] == "A" and word_matrix[y][x - 3] == "S":
        xmas_count += 1
    # Check down
    if y + 3 < max_y and word_matrix[y + 1][x] == "M" and word_matrix[y + 2][x] == "A" and word_matrix[y + 3][x] == "S":
        xmas_count += 1
    # Check up
    if y - 3 >= 0 and word_matrix[y - 1][x] == "M" and word_matrix[y - 2][x] == "A" and word_matrix[y - 3][x] == "S":
        xmas_count += 1
    # Check down-right
    if x + 3 < max_x and y + 3 < max_y and word_matrix[y + 1][x + 1] == "M" and word_matrix[y + 2][x + 2] == "A" and word_matrix[y + 3][x + 3] == "S":
        xmas_count += 1
    # Check up-left
    if x - 3 >= 0 and y - 3 >= 0 and word_matrix[y - 1][x - 1] == "M" and word_matrix[y - 2][x - 2] == "A" and word_matrix[y - 3][x - 3] == "S":
        xmas_count += 1
    # Check down-left
    if x - 3 >= 0 and y + 3 < max_y and word_matrix[y + 1][x - 1] == "M" and word_matrix[y + 2][x - 2] == "A" and word_matrix[y + 3][x - 3] == "S":
        xmas_count += 1
    # Check up-right
    if x + 3 < max_x and y - 3 >= 0 and word_matrix[y - 1][x + 1] == "M" and word_matrix[y - 2][x + 2] == "A" and word_matrix[y - 3][x + 3] == "S":
        xmas_count += 1

    return xmas_count

def num_cross_mas(word_matrix, x, y):
    cross_mas_count = 0
    max_y = len(word_matrix)
    max_x = len(word_matrix[0])
    # Check MAS-SAM
    if x + 2 < max_x and y + 2 < max_y and word_matrix[y][x + 2] == "S" and word_matrix[y + 1][x + 1] == "A" and word_matrix[y+2][x] == "M" and word_matrix[y + 2][x + 2] == "S":
        cross_mas_count += 1
    # Check MAS-MAS
    if x + 2 < max_x and y + 2 < max_y and word_matrix[y][x + 2] == "M" and word_matrix[y + 1][x + 1] == "A" and word_matrix[y+2][x] == "S" and word_matrix[y + 2][x + 2] == "S":
        cross_mas_count += 1
    # Check SAM-MAS
    if x - 2 >= 0 and y - 2 >=0 and word_matrix[y][x - 2] == "S" and word_matrix[y - 1][x - 1] == "A" and word_matrix[y-2][x] == "M" and word_matrix[y - 2][x - 2] == "S":
        cross_mas_count += 1
    # Check SAM-SAM
    if x - 2 >= 0 and y - 2 >=0 and word_matrix[y][x - 2] == "M" and word_matrix[y - 1][x - 1] == "A" and word_matrix[y-2][x] == "S" and word_matrix[y - 2][x - 2] == "S":
        cross_mas_count += 1
    
    return cross_mas_count

xmas_count = 0
for y in range(len(word_matrix)):
    for x in range(len(word_matrix[y])):
        if word_matrix[y][x] == "X":
            xmas_count += num_xmas(word_matrix, x, y)

print("Xmas Count:", xmas_count)

cross_mas_count = 0
for y in range(len(word_matrix)):
    for x in range(len(word_matrix[y])):
        if word_matrix[y][x] == "M":
            cross_mas_count += num_cross_mas(word_matrix, x, y)

print("Cross Mas Count:", cross_mas_count)
