def isCapable(s, able):
    #checks if an array is capable of withstanding "able"
    charge = 1
    damage = 0
    for step in s:
        if step == "S":
            damage += charge
        if step == "C":
            charge *= 2
    
    if damage <= able:
        return True
    else:
        return False


def main(able, b):
    if isCapable(b, able):
        #if no swaps are required
        return 0
    swaps = 0
    beam = [s for s in b]
    n = len(beam)
    for i in range(n-1, -1, -1):
        for j in range(n-1, -1, -1):
            if beam[j]=="S" and beam[j-1]=="C":
                temp = beam[j]
                beam[j] = beam[j-1]
                beam[j-1] = temp
                swaps += 1               
            if isCapable(beam, able):
                return swaps
    if isCapable(beam, able) == False:
        #if all swaps are done but stil there's no way
        return "IMPOSSIBLE"
    return swaps


if __name__ == "__main__":
    t = int(input())
    output = []
    #store the output results in a list
    while t > 0:
        rec = input().split()
        o = main(   int(rec[0]), rec[1]    )
        output.append(o)
        t -=  1
    for i in range(len(output)):
        print("Case #" + str(i+1) + ": " + str(output[i]))
    
    
