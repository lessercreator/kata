#sorts the odd numbers in ascending order while leaving the even numbers at their original positions

def sort_array(source_array):

    #creates array of odd values to check against
    basis = []
    for i in source_array:
        if i%2 != 0:
            basis.append(i)
    basis = sorted(basis)
    
    #builds new array with sorted odd values
    new_array = []
    count = 0
    for i in source_array:
        if i in basis and i%2 != 0:
            new_array.append(basis[count])
            count += 1
        else:
            new_array.append(i)

    return new_array
