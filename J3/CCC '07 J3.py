# 17:08
opened = input()

monlist = [100, 500, 1000, 5000, 10000, 25000, 50000, 100000, 500000, 1000000]

dealeramount = 0
popped = 0

for _ in range(100):
    x = int(input())
    if x > 10:
        dealeramount = x
        break
    monlist.pop(x-(1+popped))
    popped+=1
    
monlisttotal = 0
for val in monlist:
    monlisttotal += val
    
avg = monlisttotal / len(monlist)

if avg > dealeramount:
    print("no deal")
else:
    print("deal")