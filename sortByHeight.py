######################### Some people are standing in a row in a park #################
######################### There are trees between them which cannot be moved ##########
######################### Your task is to rerrange the people by their heights ########
######################### In a non-descending order without moving the trees. #########
######################### People can be very tall! ####################################


########### Test case ##############################
a = [-1, 150, 190, 170, -1, -1, 160, 180]
####################################################


############# Method 1 #############################
def sortByHeight(a):
    length = len(a)
    limit = len(a)-1

    lst =[]
    for i in range(0,length):
        if a[i] != -1:
            lst.append(a[i])
    lst_new = sorted(lst)

    ind = 0
    
    for j in range(0,length):
        if a[j] != -1:
            a[j] = lst_new[ind]
            ind += 1

    return a
####################################################  



############# Method 2 #############################
def sortByHeight2(a):
    new_list = sorted([i for i in a if i != -1])

    ind = 0
    
    for j in range(0,len(a)):
        if a[j] != -1:
            a[j] = new_list[ind]
            ind += 1
    return a
######################################################


print(sortByHeight2(a))
