instructions = []
while True:
    inst = input()
    if inst == "SCHOOL": break
    instructions.append(inst)
    
numinst = len(instructions)
rev_inst = instructions
rev_inst.reverse()
newinst = []

for inst in rev_inst:
    if inst == "SCHOOL":
        continue
    if inst == "R":
        newinst.append("LEFT")
    elif inst == "L":
        newinst.append("RIGHT")
    else:
        newinst.append(inst)

for i, inst in enumerate(newinst):
    if inst == "LEFT" or inst == "RIGHT":
        try:
            if not newinst[i+1]:
                print(f"Turn {newinst[i]} into your HOME.")
                break
        except:
            print(f"Turn {newinst[i]} into your HOME.")
            break
            
        print(f"Turn {newinst[i]} onto {newinst[i+1]} street.")
    else: continue