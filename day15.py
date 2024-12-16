map = []
moves = ''
with open('input.txt') as f:
    for line in f:
        if line == '\n':
            break
        map.append(list(line.strip()))

    for line in f:
        moves += line.strip()
map2 = []
for i in range(len(map)):
    map2.append([])
    for j in range(len(map[i])):
        if map[i][j] == 'O':
            map2[i].append('[')
            map2[i].append(']')
        elif map[i][j] == '#':
            map2[i].append('#')
            map2[i].append('#')
        elif map[i][j] == '.':
            map2[i].append('.')
            map2[i].append('.')
        elif map[i][j] == '@':
            map2[i].append('@')
            map2[i].append('.')

def apply_move(map, x, y, dx, dy):
    if map[y + dy][x + dx] == '.':
        map[y][x] = '.'
        map[y + dy][x + dx] = '@'
        return (x + dx, y + dy)
    elif map[y + dy][x + dx] == '#':
        return (x, y)
    elif map[y + dy][x + dx] == 'O':
        i = 1
        while x + i * dx >= 0 and x + i *dx < len(map[y]) and y + i * dy > 0 and y + i * dy < len(map) and map[y + i*dy][x + i*dx] == 'O':
            i += 1
        if x + i * dx < 0 or x + i * dx >= len(map[y]) or y + i * dy < 0 or y + i * dy >= len(map) or map[y + i*dy][x + i*dx] == '#':
            return (x, y)
        else:
            map[y][x] = '.'
            map[y + dy][x + dx] = '@'
            map[y + i*dy][x + i*dx] = 'O'
            return (x+ dx, y + dy)

def apply_move_v2(map, x, y, dx, dy):
    if map[y + dy][x + dx] == '.':
        map[y][x] = '.'
        map[y + dy][x + dx] = '@'
        return (x + dx, y + dy)
    elif map[y + dy][x + dx] == '#':
        return (x, y)
    elif (map[y + dy][x + dx] == '[' or map[y + dy][x + dx] == ']') and dx != 0 and dy == 0:
        i = 1
        while x + i * dx >= 0 and x + i *dx < len(map[y]) and (map[y][x + i*dx] == '[' or map[y][x + i*dx] == ']'):
            i += 1
        if x + i * dx < 0 or x + i * dx >= len(map[y]) or map[y + i*dy][x + i*dx] == '#':
            return (x, y)
        else:
            map[y][x] = '.'
            for j in range(i, 1, -1):
                map[y][x + j*dx] = map[y][x + (j-1)*dx]
            map[y][x + dx] = '@'
            return (x+ dx, y + dy)
    elif (map[y + dy][x + dx] == '[' or map[y + dy][x + dx] == ']') and dx == 0 and dy != 0:
        xs = [x]
        i = 1
        while y + i * dy >= 0 and y + i *dy < len(map[y]):
            free = 0
            has_box = False
            for j in range(len(xs)):
                if map[y + i*dy][xs[j]] == '[':
                    xs.append(xs[j] + 1)
                    has_box = True
                elif map[y + i*dy][xs[j]] == ']':
                    xs.append(xs[j] - 1)
                    has_box = True
                elif map[y + i*dy][xs[j]] == '#':
                    break
                elif map[y + i*dy][xs[j]] == '.':
                    free += 1
                    continue
            if not has_box:
                is_blocked = free != len(xs)
                break
            i += 1
        if i < 0 or i >= len(map) or is_blocked:
            return (x, y)
        else:
            map[y][x] = '.'
            xs.sort()
            for j in range(i, 1, -1):
                for k in range(len(xs) - 1):
                    if map[y + (j-1)*dy][xs[k]] == '[' and map[y + (j-1)*dy][xs[k] + 1] == ']':
                        map[y + j*dy][xs[k]] = map[y + (j-1)*dy][xs[k]]
                        map[y + j*dy][xs[k] + 1] = map[y + (j-1)*dy][xs[k] + 1]
                        map[y + (j-1)*dy][xs[k]] = '.'
                        map[y + (j-1)*dy][xs[k] + 1] = '.'
            map[y + dy][x] = '@'
            return (x+ dx, y + dy)

for i in range(len(map)):
    for j in range(len(map[i])):
        if map[i][j] == '@':
            pos = (j, i)

for move in moves:
    if move == '<':
        pos = apply_move(map, pos[0], pos[1], -1, 0)
    elif move == '>':
        pos = apply_move(map, pos[0], pos[1], 1, 0)
    elif move == '^':
        pos = apply_move(map, pos[0], pos[1], 0, -1)
    elif move == 'v':
        pos = apply_move(map, pos[0], pos[1], 0, 1)

score = 0
for i in range(len(map)):
    for j in range(len(map[i])):
        if map[i][j] == 'O':
            score += 100*i + j

print(score)

for i in range(len(map2)):
    for j in range(len(map2[i])):
        if map2[i][j] == '@':
            pos = (j, i)

for move in moves:
    print(move)
    if move == '<':
        pos = apply_move_v2(map2, pos[0], pos[1], -1, 0)
    elif move == '>':
        pos = apply_move_v2(map2, pos[0], pos[1], 1, 0)
    elif move == '^':
        pos = apply_move_v2(map2, pos[0], pos[1], 0, -1)
    elif move == 'v':
        pos = apply_move_v2(map2, pos[0], pos[1], 0, 1)
    for line in map2:
        print(''.join(line))

for line in map2:
    print(''.join(line))

score = 0
for i in range(len(map2)):
    for j in range(len(map2[i])):
        if map2[i][j] == '[':
            score += 100*i + j
print(score)