with open('input.txt') as f:
    a, b, c = map(int, [f.readline().split(':')[1] for _ in range(3)])
    f.readline()
    program = list(map(int, f.readline().split(':')[1].split(',')))



def eval(a,b,c):
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
    return out

print(','.join(map(str, eval(a, b, c))))


# def input_program(a, b, c):
#     out = []
#     while (a!=0):
#         b = a%8
#         b = b^1
#         c = a // 2 ** b
#         b = b^5
#         b = b^c
#         a = a // 8
#         out.append(b%8)
#     return out

def find(a, i):
    if eval(a, b, c) == program: print(a)
    if eval(a, b, c) == program[-i:] or not i:
        for n in range(8): find(8*a+n, i+1)

find(0, 0)
