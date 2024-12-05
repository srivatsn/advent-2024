rules = {}
pages = []

with open('input.txt', 'r') as file:
    for line in file:
        if (line == '\n'):
            break
        x,y = line.split('|')
        x,y = int(x), int(y)
        if rules.get(x) == None:
            rules[x] = [y]
        else:
            rules[x].append(y)
    
    for line in file:
        pages.append(list(map(int, line.split(','))))

def is_valid(page):
    for i in range(len(page) - 1):
        rule = rules.get(page[i])
        if rule == None:
            return False
        for j in range(i + 1, len(page)):
            if page[j] not in rule:
                return False
    return True


page_sum = 0
incorrect_pages = []
for page in pages:
    if is_valid(page):
        middle = page[len(page) // 2]
        page_sum += middle
    else:
        incorrect_pages.append(page)

print(page_sum)

# Part 2
def fix_page(page):
    for i in range(len(page) - 1):
        rule = rules.get(page[i])
        if rule == None:
            # No rule - put it in the end.
            return fix_page(page[:i] + page[i+1:] + [page[i]])
        for j in range(i + 1, len(page)):
            if page[j] not in rule:
                # Wrong position - swap it with the element for which we have the rule.
                return fix_page(page[:i] + [page[j]] + page[i + 1:j] + [page[i]] + page[j+1:])
               
    return page

page_sum = 0
for page in incorrect_pages:
    fixed_page = fix_page(page)
    middle = fixed_page[len(fixed_page) // 2]
    page_sum += middle

print(page_sum)