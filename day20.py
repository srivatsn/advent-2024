import heapq

with open('input.txt') as f:
    map = [list(line.strip()) for line in f]

def print_map(map):
    for i in range(len(map)):
        print(''.join(map[i]))

def find_start(map):
    for i in range(len(map)):
        for j in range(len(map[0])):
            if map[i][j] == 'S':
                return (j, i)

def dijkstra(map, start_x, start_y, min_scores):
    heap = []
    heapq.heappush(heap, (0, start_x, start_y))

    while heap:
        score, x, y = heapq.heappop(heap)

        # Skip if we've already found a better path to this position
        if (x, y) in min_scores and score >= min_scores[(x, y)]:
            continue

        min_scores[(x, y)] = score

        # Check for the end condition
        if map[y][x] == 'E':
            return score

        # Explore neighboring positions
        for (dx, dy) in [
            (1, 0), (-1, 0),
            (0, 1), (0, -1)
        ]:
            nx, ny = x + dx, y + dy

            # Check boundaries
            if nx < 0 or ny < 0 or nx >= len(map[0]) or ny >= len(map):
                continue
            if map[ny][nx] == '#':
                continue

            new_score = score + 1
            # Add the neighbor to the heap
            heapq.heappush(heap, (new_score, nx, ny))

    return -1 # If no path is found

start_x, start_y = find_start(map)
min_scores = {}
dijkstra(map, start_x, start_y, min_scores)

cheats = {}
N = 20
for y in range(len(map)):
    for x in range(len(map[y])):
        if map[y][x] == '#':
            continue
        cur_score = min_scores.get((x, y), float('inf'))
        for ny in range(y - N,  y + N + 1):
            for nx in range(x - N, x + N + 1):
                if nx < 0 or ny < 0 or nx >= len(map[0]) or ny >= len(map):
                    continue
                dist = abs(nx - x) + abs(ny - y)
                if map[ny][nx] == '#' or dist == 0 or dist > N:
                    continue
                new_score = min_scores.get((nx, ny), float('inf'))
                saving = new_score - cur_score - dist
                if saving > 0:
                    if saving not in cheats:
                        cheats[saving] = set([])
                    cheats[saving].add((x, y, nx, ny))

above100 = 0
for saving in sorted(cheats.keys()):
    #print(f'{saving}: {len(cheats[saving])}')
    if saving >= 100:
        above100 += len(cheats[saving])
print("Above 100:", above100)


