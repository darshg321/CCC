ops = []

while True:
    inp = input()
    ops.append(inp)
    if inp == '7':
        break
    
var = {'A': 0, 'B': 0}

for str in ops:
    match str[0]:
        case '1':
            var[str[2]] = int(str[3:])
        case '2':
            print(var[str[2]])
        case '3':
            var[str[2]] += var[str[4]]
        case '4':
            var[str[2]] *= var[str[4]]
        case '5':
            var[str[2]] -= var[str[4]]
        case '6':
            var[str[2]] = int(var[str[2]] / var[str[4]])
        case '7':
            break