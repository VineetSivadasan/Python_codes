######### Construct a function that would take an array list and replace each number in the list #####################################
######### with a product of all the other numbers in the list ########################################################################

def productReplacement(lst):
    a = len(lst)                                             #length of the input list
    rep=[]                                                   #create an empty list to fill with product values

    for i in range(a):                                       #loop through each number in the list
        x = 1                                                #set the product to replace each term, starting at 1

        #get the product of the numbers up to ith term
        if i != 0:                                           #if not on the first term in the list then
            for j in range(i):                               #run a loop over a length i-1
                x *= lst[j]                                  #and multiply the terms in the list up to i-1, to x

        #get the product of the terms after the ith term, to the end of the list
        for k in range((i+1), a):                            #run a loop starting with terms i+1 up to length of the list -1
            x *= lst[k]                                      #and multiply all terms after the ith term also to x

        rep.append(x)                                        #append this product x to the rep list

    return rep

############### Test cases ####################

a = [1,2,3,4,5,6,7]

###############################################


print(productReplacement(a))
