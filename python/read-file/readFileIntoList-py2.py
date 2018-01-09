with open('text.txt') as f:
    lines = f.read().splitlines()

for line in lines:
    print(line)
