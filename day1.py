list1 = []
list2 = []

with open('input.txt', 'r') as file:
    for line in file:
        a, b = map(int, line.split())
        list1.append(a)
        list2.append(b)

list1.sort()
list2.sort()

# Part1: Calculate the total sum of all differences between corresponding items in the lists
total_difference = sum(abs(a - b) for a, b in zip(list1, list2))
print("Total Difference:", total_difference)

# Part2: Similarity score
list3 = [list2.count(a) for a in list1]
similarity_score = sum(a * b for a, b in zip(list1, list3))
print("Similarity Score:", similarity_score)
