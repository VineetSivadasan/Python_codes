######## You are given an array of integers. On each move you are allowed to #############
######## increase exactly one of its elemnt by one. Find the minimal number ##############
######## of moves required to obtain a strictly increasing sequence from the input #######

#################################### Method 1 ############################################
def arrayChange(inputArray):
    count = 0
    for i in range(len(inputArray)-1):
        if inputArray[i+1] <= inputArray[i]:
            x = inputArray[i+1]
            inputArray[i+1] = inputArray[i]+1
            count += inputArray[i+1] - x
    return count
##########################################################################################


##################################### Method 2 (computationally longer) ##################
def arrayChange2(inputArray):
    count = 0
    for i in range(len(inputArray)-1):
        while inputArray[i] >= inputArray[i+1]:
            inputArray[i+1] += 1
            count += 1
    return count
##########################################################################################




########################## Test cases ####################################################
inputArray = [2, 1, 10, 1]

inputArray2 = [-1000, 0, -2, 0]
##########################################################################################


print(arrayChange(inputArray))
print(arrayChange(inputArray2))
