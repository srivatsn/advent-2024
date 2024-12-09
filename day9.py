with open("input.txt") as f:
    diskmap = [int(x) for x in f.read().strip()]

id = 0
disklayout = []
for i in range(0, len(diskmap), 2):
    file_length = diskmap[i]
    free_length = diskmap[i + 1] if i + 1 < len(diskmap) else 0

    disklayout.append((id, file_length))
    disklayout.append((None, free_length))
    id += 1

def defrag(disklayout):
    reverse_index = len(disklayout) - 1
    new_layout = []
    for i in range(len(disklayout)):
        if i > reverse_index:
            break
        if disklayout[i][0] is not None:
            new_layout.append(disklayout[i])
            continue
        free_space = disklayout[i][1]
        while free_space > 0:
            if reverse_index < i:
                break
            if disklayout[reverse_index][0] is None:
                reverse_index -= 1
                continue
            if disklayout[reverse_index][1] <= free_space:
                free_space -= disklayout[reverse_index][1]
                item = disklayout[reverse_index]
                reverse_index -= 1
                new_layout.append((item[0], item[1]))
                continue
            else:
                disklayout[reverse_index] = (disklayout[reverse_index][0], disklayout[reverse_index][1] - free_space)
                new_layout.append((disklayout[reverse_index][0], free_space))
                free_space = 0
    return new_layout

def defrag_wholefile(disklayout):
    for i in range(len(disklayout) - 1, -1, -1):
        if disklayout[i][0] is None:
            continue
        
        #Find a free space that is at least as long as the file
        for j in range(0, i):
            if disklayout[j][0] is None and disklayout[j][1] >= disklayout[i][1]:
                #Move the file to the free space
                remaining = disklayout[j][1] - disklayout[i][1]
                disklayout[j] = (disklayout[i][0], disklayout[i][1])
                if remaining:
                    disklayout.insert(j + 1, (None, remaining))
                    i += 1
                disklayout[i] = (None, disklayout[i][1])
                break
    return disklayout

def compute_checksum(layout):
    checksum = 0
    checksum_index = 0
    for i in range(len(layout)):
        if layout[i][0] is None:
            checksum_index += layout[i][1]
            continue
        checksum += sum([layout[i][0] * (checksum_index + x) for x in range(0, layout[i][1])])
        checksum_index += layout[i][1]
    return checksum

disklayout2 = disklayout.copy()
new_layout = defrag(disklayout)
print(compute_checksum(new_layout))

new_layout2 = defrag_wholefile(disklayout2)
print(compute_checksum(new_layout2))