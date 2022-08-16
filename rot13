#Deciphers ROT13 encoded messages

def rot13(message):
    
    alf = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"
    ALF = "ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ"
    
    rotten = []
    
    split = list(message)

    for char in split:
        if char in alf:
            for i in range(len(alf)):
                if char == alf[i]:
                    rotten.append(alf[i+13])
                    break
        elif char in ALF:
            for i in range(len(ALF)):
                if char == ALF[i]:
                    rotten.append(ALF[i+13])
                    break
        else:
            rotten.append(char)
                    
    return ''.join(rotten)
