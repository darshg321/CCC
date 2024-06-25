delivered = int(input())
coll = int(input())

points = delivered * 50 - coll * 10

if delivered > coll:
    points += 500
    
print(points)