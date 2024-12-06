map = []

with open("input.txt") as file:
    for line in file:
        map.append(list(line.strip()))
        if '^' in line:
            starting_x, starting_y = (line.index('^'), len(map) - 1)

def next_step(x, y, direction):
    moves = {'N': (0, -1), 'S': (0, 1), 'E': (1, 0), 'W': (-1, 0)}
    dx, dy = moves[direction]
    return x + dx, y + dy

def next_direction(direction):
    return {'N': 'E', 'E': 'S', 'S': 'W', 'W': 'N'}[direction]

def is_obstruction(x, y, direction, map):
    next_dir = next_direction(direction)
    next_x, next_y = next_step(x, y, next_dir)

    nodes = set([(next_x, next_y, next_dir)])
    while next_y >= 0 and next_y < len(map) and next_x >= 0 and next_x < len(map[next_y]):
        if next_dir in map[next_y][next_x]:
            return True
        if map[next_y][next_x] == '#':
            next_dir = next_direction(next_dir)
        next_x, next_y = next_step(next_x, next_y, next_dir)
        # if the set contains the next node, we have a loop
        if (next_x, next_y, next_dir) in nodes:
            return True
        nodes.add((next_x, next_y, next_dir))
    return False

obstructions_set = set()
def traceroute(starting_x, starting_y, direction, map):
    x, y = starting_x, starting_y
    obstructions = 0
    while True:
        next_x, next_y = next_step(x, y, direction)
        if next_y < 0 or next_y >= len(map) or next_x < 0 or next_x >= len(map[next_y]):
            break
        if map[next_y][next_x] == '#':
            direction = next_direction(direction)
        else:
            x, y = next_x, next_y
            if is_obstruction(x, y, direction, map):
                obstructions += 1
                next_x, next_y = next_step(x, y, direction)
                obstructions_set.add((next_x, next_y))
            map[y][x] = direction
    return obstructions

map[starting_y][starting_x] = 'N'
obstructions = traceroute(starting_x, starting_y, 'N', map)

print(sum([line.count('N') + line.count('E') + line.count('W') + line.count('S') for line in map]))
print(obstructions)
print(obstructions_set)

