chardict = {}

for i in range(int(input())):
    cenc = input()
    enclist = cenc.split(" ")
    
    chardict[enclist[1]] = enclist[0]
    
binarymsg = input()
msg = ""
submsg = ""

for c in binarymsg:
    submsg += c
    
    if submsg in chardict:
        msg += chardict[submsg]
        submsg = ""
        
print(msg)