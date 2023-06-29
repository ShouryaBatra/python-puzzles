
with open('text.txt') as f:
    lines = f.readlines()

# print(lines)

for i in range(len(lines)):
    # lines[i] = lines[i].replace(lines[i][-2:-1], "")
    if lines[i][-1] == "\n":
        lines[i] = lines[i][:-1]
    print(lines[i] + " bob")