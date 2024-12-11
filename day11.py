import math

stones = []
with open("input.txt") as f:
    stones = [int(x) for x in f.read().split()]

seen = {}
def count_stones(number, depth):
    if (number, depth) in seen:
        return seen[(number, depth)]
    if depth == 75:
        seen[(number, depth)] = 1
        return 1
    
    numdigits = 1 if number == 0 else math.floor(math.log(number, 10) + 1)
    if number == 0:
        count = count_stones(1, depth + 1)
    elif numdigits%2 == 0:
        part1, part2 = number//(10**(numdigits//2)), number - (number//(10**(numdigits//2)))*(10**(numdigits//2))
        count = count_stones(part1, depth + 1) + count_stones(part2, depth + 1)
    else:
        count = count_stones(number*2024, depth + 1)
    seen[(number, depth)] = count
    return count

sum = 0
for i in range(0, len(stones)):
    sum += count_stones(stones[i], 0)
print(sum)