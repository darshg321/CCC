scores = []

for i in range(int(input())):
    scores.append(int(input()))
    
scores.sort(reverse=True)
nodupes = list(set(scores))
nodupes.sort(reverse=True)

third = nodupes[2]
count = 0

for score in scores:
    if score == third:
        count += 1

print(third, count)