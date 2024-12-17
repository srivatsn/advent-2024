import heapq

map = []
with open('input.txt') as f:
    for line in f:
        map.append(list(line.strip()))

for i in range(len(map)):
    for j in range(len(map[0])):
        if map[j][i] == 'S':
            start_pos = (i, j)
        if map[j][i] == 'E':
            end_pos = (i, j)

def dijkstra(map, start_x, start_y, predecessors):
    min_scores = {}
    heap = []
    heapq.heappush(heap, (0, start_x, start_y, 'E'))

    while heap:
        score, x, y, prev_direction = heapq.heappop(heap)

        # Skip if we've already found a better path to this position
        if (x, y) in min_scores and score >= min_scores[(x, y)]:
            continue

        min_scores[(x, y)] = score

        # Check for the end condition
        if map[y][x] == 'E':
            return score

        # Explore neighboring positions
        for direction, (dx, dy) in {
            'E': (1, 0), 'W': (-1, 0),
            'S': (0, 1), 'N': (0, -1)
        }.items():
            nx, ny = x + dx, y + dy

            # Check boundaries
            if nx < 0 or ny < 0 or nx >= len(map[0]) or ny >= len(map):
                continue
            if map[ny][nx] == '#':
                continue

            # Calculate new score
            if prev_direction is None or direction == prev_direction:
                new_score = score + 1
            else:
                new_score = score + 1001  # Penalty for changing direction

            # Add the neighbor to the heap
            heapq.heappush(heap, (new_score, nx, ny, direction))

            # Keep track of predecessors
            if (nx, ny) not in predecessors:
                predecessors[(nx, ny)] = set()
            if new_score <= min_scores.get((nx, ny), float('inf')) or new_score == min_scores.get((nx, ny), float('inf')) + 1000:
                predecessors[(nx, ny)].add((x, y))
            

    return -1  # 'E' is not reachable

predecessors = {}
min_score = dijkstra(map, start_pos[0], start_pos[1], predecessors)

# Backtrack to find all tiles in at least one shortest path
tiles_in_paths = set()
stack = [end_pos]
while stack:
    current = stack.pop()
    tiles_in_paths.add(current)
    if current in predecessors:
        for pred in predecessors[current]:
            if pred not in tiles_in_paths:
                stack.append(pred)

# Print the map with
print(f"Number of tiles in at least one best path: {len(tiles_in_paths)}")
print(min_score)