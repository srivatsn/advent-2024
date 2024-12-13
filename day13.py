machines = []

with open("input.txt") as f:
    # read three lines at a time
    while True:
        line = f.readline()
        if not line:
            break
        _, c = line.split(':')
        ax, ay = map(lambda x: x.split('+')[1], c.split(','))

        line = f.readline().strip()
        _, c = line.split(':')
        bx, by = map(lambda x: x.split('+')[1], c.split(','))

        line = f.readline().strip()
        _, c = line.split(':')
        px, py = map(lambda x: x.split('=')[1], c.split(','))
        machines.append(((int(ax), int(ay)), (int(bx), int(by)), (int(px), int(py))))
        f.readline()

sum =0
for machine in machines:
    (a1, a2), (b1, b2), (p1, p2) = machine
    x = (p1*b2 - p2*b1)/(a1*b2 - a2*b1)
    y = (p2*a1 - p1*a2)/(a1*b2 - a2*b1)
    if x > 0 and y > 0 and x < 100 and y < 100 and (x, y) == (int(x), int(y)):
        tokens = 3*int(x) + int(y)
        sum += tokens

print(sum)

sum =0
for machine in machines:
    (a1, a2), (b1, b2), (p1, p2) = machine
    p1, p2 = p1 + 10000000000000, p2 + 10000000000000
    x = (p1*b2 - p2*b1)/(a1*b2 - a2*b1)
    y = (p2*a1 - p1*a2)/(a1*b2 - a2*b1)
    if x > 0 and y > 0 and (x, y) == (int(x), int(y)):
        tokens = 3*int(x) + int(y)
        sum += tokens
print(sum)