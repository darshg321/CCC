heat = {"Poblano": 1500,
"Mirasol": 6000,
"Serrano": 15500,
"Cayenne": 40000,
"Thai": 75000,
"Habanero": 125000}

total = 0

chillis = []

for i in range(int(input())):
    chillis.append(input())
    
for p in chillis:
    total += heat[p]
    
print(total)