K = int(input())
msg = list(input())

upper = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
         'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

decoded = ""
msgpos = 1

for c in msg:
    for i, alphc in enumerate(upper):
        if alphc == c:
            pos = i
            break
    
    decryptedpos = pos - (3*(msgpos) + K)
    
    if decryptedpos < 0: decryptedpos += 26
    
    decoded += upper[decryptedpos]
    msgpos += 1

print(decoded)