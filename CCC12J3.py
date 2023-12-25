scale = int(input())

scaledstr1 = "*"*scale + "x"*scale + "*"*scale
scaledstr2 = " "*scale + "x"*scale + "x"*scale
scaledstr3 = "*"*scale + " "*scale + "*"*scale

for i in range(scale):
    print(scaledstr1)
for i in range(scale):
    print(scaledstr2)
for i in range(scale):
    print(scaledstr3)
