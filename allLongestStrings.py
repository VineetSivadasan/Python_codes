################################################# Given an array of strings, return an array containing all of its longest strings  #########################




def allLongestStrings(inputArray):
    array_max = max(inputArray, key=len)    #longest string in the array
    print(array_max)
    
    array_len = len(inputArray)    #size of the array
    print(array_len)
    
    array_max_len = len(array_max) #size of longest string in the array
    print(array_max_len)
    
    output = []

    for i in range(array_len):
        if len(inputArray[i]) == array_max_len:
            output.append(inputArray[i])
    return output

    print(output)


##############   Test cases     ##############################
A = ["aba", "aa", "ad", "vcd", "aba"]
B = ["enyky", "benyky", "yely", "varennyky"]
###############################################################


print(allLongestStrings(B))



