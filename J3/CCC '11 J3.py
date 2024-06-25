t1 = int(input())
t2 = int(input())

seq = [t1, t2]

for i in range(10000):
    t3 = seq[-2] - seq[-1]
    if t3 > seq[-1]:
        seq.append(t3)
        break
    seq.append(t3)
    
print(len(seq))