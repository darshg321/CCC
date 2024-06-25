# check if ispalindrome
# double for loop, subtracting from the left in the first loop, right in the second to check all combinations
# append to list

substrs = []

def ispalindrome(str):
    return str[::-1] == str

w = input()

while True:
    left = 0
    for i in range(len(w)):
        right = 0
        for j in range(len(w)):
            if ispalindrome(w[left:(len(w)-right)]):
                substrs.append(w[left:(len(w)-right)])
            right+=1
        left+=1
    break

maxlen = 0
for s in substrs:
    if len(s) > maxlen:
        maxlen = len(s)
print(maxlen)