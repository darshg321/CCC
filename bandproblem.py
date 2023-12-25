x = input()
string = ''
num = ""
for i in x:
    if not i.isnumeric() and num:
        print(string, num)
        string = ""
        num = ""

    if i == '+':
        string += " tighten"
    elif i == '-':
        string += " loosen"
    elif i.isnumeric():
        num += i     
    else: 
        string += i

print(string, num)