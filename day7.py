import math


problems = []
with open("input.txt") as file:
    for line in file:
        test, equation = line.split(':')
        numbers = list(map(int, equation.split()))
        problems.append((int(test), numbers))

def is_solvable(problem, concat=False):
    test, numbers = problem
    
    intermediate = [numbers[0]]
    for i in range(1, len(numbers)):
        newList = []
        for j in intermediate:
            newList.append(j + numbers[i])
            newList.append(j * numbers[i])
            if concat:
                #newList.append(int(str(j) + str(numbers[i])))
                newList.append(j * (10 ** (math.floor(math.log10(numbers[i])) + 1)) + numbers[i])
        intermediate = newList

    if test in intermediate:
        return True
    return False

result = 0
resultWithConcat = 0
for problem in problems:
    if is_solvable(problem):
        result += problem[0]
    if is_solvable(problem, True):
        resultWithConcat += problem[0]

print(result)
print(resultWithConcat)
    
