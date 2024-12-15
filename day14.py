robots = []
with open('input.txt') as f:
    for line in f:
        p, v = line.split(' ')
        px, py = p.split('=')[1].split(',')
        vx, vy = v.split('=')[1].split(',')
        robots.append((int(px), int(py), int(vx), int(vy)))

maxwidth = 101
maxheight = 103
totaltime = 100

def print_map(map):
    for row in map:
        print(''.join(row))

def count_quadrants(robots, totaltime):
    q1,q2,q3,q4 = 0,0,0,0
    for robot in robots:
        x, y = robot[0], robot[1]
        vx, vy = robot[2], robot[3]
        fx = (x + vx*totaltime) % maxwidth
        fy = (y + vy*totaltime) % maxheight

        if fx < maxwidth//2 and fy < maxheight//2:
            q1 += 1
        elif fx > maxwidth//2 and fy < maxheight//2:
            q2 += 1
        elif fx < maxwidth//2 and fy > maxheight//2:
            q3 += 1
        elif fx > maxwidth//2 and fy > maxheight//2:
            q4 += 1
    print(q1*q2*q3*q4)

def move_robots(robots, totaltime, map=None):
    points = []
    for robot in robots:
        x, y = robot[0], robot[1]
        vx, vy = robot[2], robot[3]
        fx = (x + vx*totaltime) % maxwidth
        fy = (y + vy*totaltime) % maxheight

        if map is not None:
            map[fy][fx] = '#'
        points.append((fx, fy))

    centroid = (sum([p[0] for p in points])//len(points), sum([p[1] for p in points])//len(points))
    avg_dist = sum([abs(p[0]-centroid[0]) + abs(p[1]-centroid[1]) for p in points])//len(points)
    return avg_dist


count_quadrants(robots, totaltime)

mindist = 1000000
min_iter = 1000000
for i in range(1, 10000):
    avg_dist = move_robots(robots, i)
    if avg_dist < mindist:
        mindist = avg_dist
        min_iter = i
        print(i, avg_dist)

map = [['.' for _ in range(maxwidth)] for _ in range(maxheight)]
move_robots(robots, min_iter, map)
print_map(map)