#################### The Utopian Tree goes through 2 cycles of growth every year. Each spring, it doubles in height. Each summer, its height  ##################
#################### increases by 1m. A Utopian Tree sapling with a height of 1m is planted at the onset of spring. How tall will the tree be ##################
#################### after n growth cycles? For example, if the number of growth cycles is 5, the calculations are as follows: #################################


######  Period      Height  #######
######    0            1    #######
######    1            2    #######
######    2            3    #######
######    3            6    #######
######    4            7    #######
######    5           14    #######



def utopia_tree(n):
    result = 1
    two_cycles = n//2
    for i in range(two_cycles):
        result = result*2 + 1
    if n % 2!=0:
        result *= 2
    return result





################### test case ##################################################################################################################################
print(utopia_tree(8))
