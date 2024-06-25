# 7:46

nrounds = int(input())

antscore = 100
davscore = 100

for i in range(nrounds):
    roll = input()
    ant = int(roll[0])
    dav = int(roll[-1])
    
    if ant > dav:
        davscore -= ant
    if ant < dav:
        antscore -= dav
    if ant == dav:
        continue
    
print(antscore)
print(davscore)