athrees =  int(input())
atwos =  int(input())
aones =  int(input())
bthrees =  int(input())
btwos =  int(input())
bones =  int(input())

ascore = athrees*3 + atwos*2 + aones
bscore = bthrees*3 + btwos*2 + bones

if ascore > bscore:
    print("A")
elif ascore == bscore:
    print("T")
else:
    print("B")