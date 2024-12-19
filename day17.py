with open('input.txt') as f:
    a, b, c = map(int, [f.readline().split(':')[1] for _ in range(3)])
    f.readline()
    program = list(map(int, f.readline().split(':')[1].split(',')))

def combo(x):
    if 0 <= x <= 3:
        return x
    if x == 4:
        return a
    if x == 5:
        return b
    if x == 6:
        return c
    raise ValueError(f'Invalid combo {x}')

out = []
ip = 0
while (ip < len(program)):
    instruction, operand = program[ip], program[ip+1]
    
    if instruction == 0:
        a = a // (2 ** combo(operand))
    elif instruction == 1:
        b = b ^ operand
    elif instruction == 2:
        b = combo(operand) % 8
    elif instruction == 3:
        if a != 0:
            ip = operand
            continue
    elif instruction == 4:
        b = b ^ c
    elif instruction == 5:
        out.append(combo(operand) % 8)
    elif instruction == 6:
        b = a // (2 ** combo(operand))
    elif instruction == 7:
        c = a // (2 ** combo(operand))
    ip += 2

print(','.join(map(str, out)))