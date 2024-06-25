size = int(input())

while True:
    yo = int(input())
    if yo < size:
        size += yo
        continue
    break

print(size)