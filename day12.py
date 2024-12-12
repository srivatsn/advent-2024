map = []
with open("input.txt") as f:
    for line in f:
        map.append(list(line.strip()))

def dfs(map, x, y, type, visited):
    if x < 0 or y < 0 or x >= len(map) or y >= len(map[0]):
        return
    if (x,y) in visited:
        return
    if map[y][x] != type:
        return
    else:
        visited.append((x,y))
        dfs(map, x + 1, y, type, visited)
        dfs(map, x - 1, y, type, visited)
        dfs(map, x, y + 1, type, visited)
        dfs(map, x, y - 1, type, visited)

totalseen = []
regions = []

def get_perimeter(region):
    perimeter = 0
    for (x,y) in region:
        if (x + 1, y) not in region:
            perimeter += 1
        if (x - 1, y) not in region:
            perimeter += 1
        if (x, y + 1) not in region:
            perimeter += 1
        if (x, y - 1) not in region:
            perimeter += 1
    return perimeter

def get_sides(region):
    sides = 0
    visited = []
    for (x,y) in region:
        if (x + 1, y) not in region and (x, y, 'E') not in visited:
            visited.append((x, y, 'E'))
            i = 1
            while (x, y + i) in region and (x + 1, y + i) not in region:
                visited.append((x, y + i, 'E'))
                i += 1
            i = 1
            while (x, y - i) in region and (x + 1, y - i) not in region:
                visited.append((x, y - i, 'E'))
                i += 1
            sides += 1
        if (x - 1, y) not in region and (x, y, 'W') not in visited:
            visited.append((x, y, 'W'))
            i = 1
            while (x, y + i) in region and (x - 1, y + i) not in region:
                visited.append((x, y + i, 'W'))
                i += 1
            i = 1
            while (x, y - i) in region and (x - 1, y - i) not in region:
                visited.append((x, y - i, 'W'))
                i += 1
            sides += 1
        if (x, y + 1) not in region and (x, y, 'S') not in visited:
            visited.append((x, y, 'S'))
            i = 1
            while (x + i, y) in region and (x + i, y + 1) not in region:
                visited.append((x + i, y, 'S'))
                i += 1
            i = 1
            while (x - i, y) in region and (x - i, y + 1) not in region:
                visited.append((x - i, y, 'S'))
                i += 1
            sides += 1
        if (x, y - 1) not in region and (x, y, 'N') not in visited:
            visited.append((x, y, 'N'))
            i = 1
            while (x + i, y) in region and (x + i, y - 1) not in region:
                visited.append((x + i, y, 'N'))
                i += 1
            i = 1
            while (x - i, y) in region and (x - i, y - 1) not in region:
                visited.append((x - i, y, 'N'))
                i += 1
            sides += 1
    return sides

for y in range(len(map)):
    for x in range(len(map[y])):
        if (x,y) not in totalseen:
            type = map[y][x]
            visited = []
            dfs(map, x, y, type, visited)
            totalseen += visited
            area = len(visited)
            perimeter = get_perimeter(visited)
            sides = get_sides(visited)
            regions.append((type, area, perimeter, sides))

cost = sum([area*perimeter for (_, area, perimeter, _) in regions])
print(cost)
print(sum([area*sides for (_, area, _, sides) in regions]))