map = []

with open("input.txt") as f:
    for line in f:
        map.append(line.strip())

antennae = {}

for i in range(len(map)):
    for j in range(len(map[i])):
        char = map[i][j]
        if char != '.':
            antennae.setdefault(char, []).append((i, j))

def count_antinodes(anyposition = False):
    locations = set()
    antinode_count = 0
    for k, v in antennae.items():
        count = 0
        for i in range(len(v) - 1):
            for j in range(i + 1, len(v)):
                slopeY = v[j][0] - v[i][0]
                slopeX = v[j][1] - v[i][1]

                antinode1Y = v[i][0] - slopeY
                antinode1X = v[i][1] - slopeX
                antinode2Y = v[j][0] + slopeY
                antinode2X = v[j][1] + slopeX

                while (antinode1X >= 0 and antinode1X < len(map) and antinode1Y >= 0 and antinode1Y < len(map[0])):
                    if (antinode1X, antinode1Y) not in locations:
                        locations.add((antinode1X, antinode1Y))
                        count += 1
                    if not anyposition:
                        break
                    antinode1Y = antinode1Y - slopeY
                    antinode1X = antinode1X - slopeX
                while (antinode2X >= 0 and antinode2X < len(map) and antinode2Y >= 0 and antinode2Y < len(map[0])):
                    if (antinode2X, antinode2Y) not in locations:
                        locations.add((antinode2X, antinode2Y))
                        count += 1
                    if not anyposition:
                        break
                    antinode2Y = antinode2Y + slopeY
                    antinode2X = antinode2X + slopeX
        antinode_count += count
        if anyposition and len(v) > 1:
            for i in range(len(v)):
                if (v[i][1], v[i][0]) not in locations:
                    locations.add((v[i][1], v[i][0]))
                    antinode_count += 1

    return antinode_count

print(count_antinodes())
print(count_antinodes(True))

