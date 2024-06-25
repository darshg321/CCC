totalmin = int(input())
numchores = int(input())
times = []
for x in range(numchores):
    time = int(input())
    times.append(time)
    
times.sort()

compchores = 0
totaltime = 0

for time in times:
    if totalmin >= totaltime + time:
        totaltime += time
        compchores += 1
        
print(compchores)