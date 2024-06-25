msglist = []
for i in range(int(input())):
    msglist.append(input())
    
for msg in msglist:
    print(msg[-1]*int(msg.split()[0]))