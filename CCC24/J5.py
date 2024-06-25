# gets 1 point, not full
total = 0
rows = int(input())
columns = int(input())

for i in range(rows):
    for c in input():
        if c == "S":
            total += 1
            continue
        if c == "M":
            total += 5
            continue
        if c == "L":
            total += 10
            continue

print(total)