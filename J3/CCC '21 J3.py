codes = []
while True:
    code = input()
    if code == "99999":
        break
    codes.append(code)

for code in codes:
    lastchar = ""
    direction = ""
    units = ""
    for c in code:
        if direction:
            units += c
            continue
        
        if lastchar:
            if (int(lastchar) + int(c)) == 0:
                direction = lastdir
                continue
                
            if (int(lastchar) + int(c)) % 2 == 0:
                direction = "right"
            else: direction = "left"
        
        lastchar = c
            
    print(direction, units)
    
    lastdir = direction