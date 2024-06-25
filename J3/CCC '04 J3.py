# 4:52

adjnum = int(input())
nounnum = int(input())

adjlist = []
nounlist = []


for i in range(adjnum):
    adjlist.append(input())
for i in range(nounnum):
    nounlist.append(input())
    
for adj in adjlist:
    for noun in nounlist:
        print(f"{adj} as {noun}")
