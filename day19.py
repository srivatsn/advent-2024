patterns = []
with open('input.txt') as file:
    towels = [x.strip() for x  in file.readline().strip().split(',')]
    file.readline()
    for line in file:
        patterns.append(line.strip())

def ispossible(pattern, towels):
    if len(pattern) == 0:
        return True
    if len(towels) == 0:
        return False
    str = ''
    for i in range(len(pattern)):
        str += pattern[i]
        if str in towels:
            if ispossible(pattern[i+1:], towels):
                return True
    return False

memo = {}
def count_possible(pattern, towels):
    if pattern in memo:
        return memo[pattern]
    if len(pattern) == 0:
        return 0
    str = ''
    count = 0
    for i in range(len(pattern)):
        str += pattern[i]
        if str in towels:
            if str == pattern:
                return count + 1
            else:
                count += count_possible(pattern[i+1:], towels)
    memo[pattern] = count
    return count

possible = 0
for pattern in patterns:
    if ispossible(pattern, towels):
        possible += 1
print(possible)

tc = 0
for pattern in patterns:
    tc += count_possible(pattern, towels)
print(tc)