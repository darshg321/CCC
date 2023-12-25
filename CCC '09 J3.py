time = int(input())

def conv(diff):
    if time + diff < 0:
        return (time + diff) + 2400
    elif time + diff >= 2400:
        return (time + diff) - 2400
    return time + diff


print(conv(0), "in Ottawa")
print(conv(-300), "in Victoria")
print(conv(-200), "in Edmonton")
print(conv(-100), "in Winnipeg")
print(conv(0), "in Toronto")
print(conv(100), "in Halifax")
print(conv(130), "in St. John's")