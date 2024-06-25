# gets 3 points, not full
origstr = input()
wronstr = input()

# compare two strings
# find differences


wrongchar = ""
rightchar = ""
skey = ""

# for i, c in enumerate(origstr):
#     if c == wronstr[i]:
#         continue
#     wrongchar = wronstr[i]
#     rightchar = c
#     break

# find silent char candidates and put in list
# pick most common one?

# know if silent char if char after is also wrong
# loop
# if char wrong:
#   if char after wrong:
#   silent char = char wrong
# wrong char = char wrong
# add right char in place

# for i, c in enumerate(origstr):
#     try:
#         if c == wronstr[i]:
#             continue
#     except IndexError:
#         skey = c
#         break
    
#     # not right char
#     #   silly key
#     if origstr[i+1] == wronstr[i+1] or wronstr[i+1] == wrongchar:
#         rightchar = c
#         wrongchar = wronstr[i]
#         continue
#     #   silent key
#     skey = origstr[i]
#     # wronstr = str(list(wronstr).insert(i, skey))

for i, c in enumerate(origstr):
    try:
        if c == wronstr[i]:
            continue
    except IndexError:
        skey = c
        break
    
    # not right char
    #   silly key
    if not wrongchar:
        if (origstr[i+1] == wronstr[i+1] or wronstr[i+1] == wrongchar):
            rightchar = c
            wrongchar = wronstr[i]
            for char in wronstr:
                wronstr = wronstr.replace(wrongchar, rightchar)
            continue
    #   silent key
    skey = origstr[i]
    # wronstr = str(list(wronstr).insert(i, skey))

print(rightchar, wrongchar)
if skey: print(skey)
else: print("-")