numppl = int(input())
schlist = []
daycount = [0, 0, 0, 0, 0]
for i in range(numppl):
    schlist.append(input())
    
for schedule in schlist:
    for day, c in enumerate(schedule):
        if c == "Y":
            daycount[day] += 1
            
# print(daycount.index(max(daycount))+1)

bestdays = []
max = max(daycount)
for i, day in enumerate(daycount):
    if day == max: bestdays.append(str(i+1))
    
print(','.join(bestdays))