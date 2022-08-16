#In this simple Kata your task is to create a function that turns a string into a Mexican Wave. 
#You will be passed a string and you must return that string in an array where an uppercase letter is a person standing up. 

def wave(people):
    people = list(people)
    wave = []
    
    count = 0
    for i in range(len(people)):
        var = ""
        for i in range(len(people)):
            if i == count:
                if people[i] == ' ':
                    check = 5
                else:
                    var += people[i].upper()
                    check = 0
            else: var += people[i]
        count += 1
        if check == 0:
            wave.append(var)
    return wave
