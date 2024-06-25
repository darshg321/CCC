ostr = input()
wstr = input()

wchar = ""
rchar = ""
schar = ""

olist = list(ostr)
wlist = list(wstr)

# find char that is in wstr but not in ostr
for c in wlist:
    if c not in olist:
        wchar = c
        break
    
# for c in olist:
#     if c not in wlist:
#         rchar = c
#         break

fixedwstr = str(wlist).replace(wchar, rchar)
print(fixedwstr)
# find schar
for c in olist:
    if c not in fixedwstr:
        schar = c
        
print(rchar, wchar)
if schar: 
    print(schar)
else: 
    print("-")