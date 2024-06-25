# if theres 26 dict entries, add 27th

pln = input()
cph = input()
enc = input()

cipher = {}

for i, c in enumerate(cph):
    cipher[c] = pln[i]
        

def fndmis():
    alph = "ABCDEFGHIJKLMNOPQRSTUVWXYZ "
    for c in alph:
        if c not in cph:
            missingek = c
    for c in alph:
        if c not in pln:
            missingdk = c
    cipher[missingek] = missingdk
    
decrypted = ""

for c in enc:
    if c in cph:
        decrypted += cipher[c]
    elif len(cipher) == 26:
        fndmis()
        decrypted += cipher[c]
    else: decrypted += '.'

print(decrypted)