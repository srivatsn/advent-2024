map = []
with open("input.txt") as f:
    for line in f:
        map.append([int(x) for x in line.strip()])

def find_trails(map, x, y, cur_val, trail_dest):
    if x < 0 or y < 0 or x >= len(map) or y >= len(map[0]):
        return
    if map[y][x] != cur_val:
        return
    if map[y][x] == 9:
        trail_dest[(x,y)] = trail_dest.setdefault((x, y), 0) + 1
        return

    find_trails(map, x + 1, y, cur_val + 1, trail_dest) 
    find_trails(map, x - 1, y, cur_val + 1, trail_dest)
    find_trails(map, x, y + 1, cur_val + 1, trail_dest)
    find_trails(map, x, y - 1, cur_val + 1, trail_dest)

    return

score = 0
gradient = 0
for i in range(len(map)):
    for j in range(len(map[i])):
        if map[i][j] == 0:
            trail_dest = {}
            find_trails(map, j, i, 0, trail_dest)
            score += len(trail_dest)
            gradient += sum([trail_dest[k] for k in trail_dest])

print(score)
print(gradient)