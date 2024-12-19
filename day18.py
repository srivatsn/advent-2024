import heapq


bytes = []
with open('input.txt') as f:
    for line in f:
        bytes.append(list(map(int, line.strip().split(','))))

GRID_SIZE = 71
def map_after(num_bytes):
    map = [['.' for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]
    for i in range(num_bytes):
        x, y = bytes[i]
        map[y][x] = '#'
    return map

end_x, end_y = GRID_SIZE -1, GRID_SIZE -1
def dijkstra(map, start_x, start_y):
    min_scores = {}
    heap = []
    heapq.heappush(heap, (0, start_x, start_y))

    while heap:
        score, x, y = heapq.heappop(heap)

        # Skip if we've already found a better path to this position
        if (x, y) in min_scores and score >= min_scores[(x, y)]:
            continue

        min_scores[(x, y)] = score

        # Check for the end condition
        if end_x == x and end_y == y:
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

map = map_after(1024)
print(dijkstra(map, 0, 0))

prev_i = 0
prev_j = len(bytes)
while True:
    k = (prev_i + prev_j) // 2
    map = map_after(k)
    if dijkstra(map, 0, 0) != -1:
        prev_i = k
    else:
        prev_j = k
    if prev_j - prev_i == 1:
        break

print(bytes[prev_i])