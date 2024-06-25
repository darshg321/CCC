msglist = []
for i in range(int(input())):
    msglist.append(input())

encodedlist = []
for msg in msglist:
    count = 0
    sym = ""
    enc = []
    firstchar = True
    for i, c in enumerate(msg):
        if firstchar:
            sym = c
            count += 1
            firstchar = False
            continue
        if sym == c:
            if i == len(msg)-1:
                enc.append(str(count+1) + " " + sym)
                continue
            count += 1
            continue
        if not (sym == c):
            enc.append(str(count) + " " + sym + " ")
            sym = c
            count = 1
            if i == len(msg)-1:
                enc.append(str(1) + " " + sym)
                continue
            continue
 
        
    string = ""
    for thing in enc:
        string += thing
    encodedlist.append(string)

for encmsg in encodedlist:
    print(encmsg)