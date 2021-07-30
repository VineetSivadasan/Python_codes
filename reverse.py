####################### Given an array list, reverse the terms in the list about the mid point ######################################################
####################### so that the last term appears first, the first term #########################################################################
####################### appears last, the second to last term appears second ########################################################################
####################### the second term appears second to last, etc... ##############################################################################




############################# Method 1 ##############################################################################################################
def reverse(lst):
    size = len(lst)           #actual number of characters in the list (1-n)
    pointer = size - 1           #characters are numbered 0 to n-1, maxpoint puts the pointer on last character in the list
    limit = size//2                #half the list size (use // otherwise limit is converted from an 'int' to a 'float')


    for i in range(0, limit):      #starting the for loop on the list from where i is the first character in the list through to halfway down the list 
        temp = lst[pointer]     #create a variable called temp starting from the end of the list
        lst[pointer] = lst[i]  #replace the last character in the list with the first character
        lst[i] = temp            #replace the first character in the list with the last character
        pointer -= 1             #move the pointer back by 1
    return lst
######################################################################################################################################################        




############################ Method 2 ################################################################################################################
def reverse2(lst):
    a = lst[::-1]
    return a
#############################################################



    
##################### Test case #######################      
a = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
b = [1,2,3,4,5]

print(reverse(a))

#print(reverse2(a))
#print(reverse2(b))
    


