import re

#read line from input.txt
with open("input.txt", "r") as file:
    input_line = ''.join(file.readlines())

def mul(program):
    pattern = r"mul\((\d{1,3}),(\d{1,3})\)"
    matches = re.findall(pattern, program)
    total = sum([int(x) * int(y) for x, y in matches])
    return total

print("Executed mul:", mul(input_line))

def enabled_mul(program):
    pattern = r"(do\(\)|don't\(\)|^)(.*?)(?=do\(\)|don't\(\)|$)"
    matches = re.findall(pattern, input_line, re.DOTALL)
    total = sum(mul(x[1]) for x in matches if (x[0] == "do()" or x[0] == ""))
    return total

print("Executed only enabled mul:", enabled_mul(input_line))