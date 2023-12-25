thing = 0
teamlist = []
for i in range(int(input()) * 2):
    if thing == 1:
        starscore -= int(input()) * 3
        thing = 0
        teamlist.append(starscore)
        starscore = 0
        continue
    starscore = int(input()) * 5
    thing += 1
    
starplayers = 0
for score in teamlist:
    if score >= 40:
        starplayers += 1
        
if starplayers == len(teamlist):
    print(f"{starplayers}+")
else:
    print(starplayers)