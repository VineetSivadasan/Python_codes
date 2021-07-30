######### Two arrays are called similar if one can be obtained from another by swapping ###########################################
######### at most one pair of elements in one of the arrays #######################################################################

def areSimilar(a, b):
    lst1 = []                                               #this list will store the positions of the unmatched numbers
    lst2 = []                                               #this list will store the unmatched numbers from list "a" 
    lst3 = []                                               #this list will store the unmatched numbers from list "b"

    i = 0                                                   #start a count
    while i < len(a):                                       #start a while loop counting from i = 0 till len(a)-1
        if a[i] != b[i]:                                    #if at a position i, a[i] is not equal to b[i]
            lst1.append(i)                                  #then append lst1 with position number i
            lst2.append(a[i])                               #also append the value a at position i to lst2
            lst3.append(b[i])                               #and append the value b at position i to lst3
        i += 1                                              #move the count up by 1

    if len(lst1) == 2 and sorted(lst2) == sorted(lst3):     #if there are only two numbers i.e. a pair of unmatched numbers   
                                                            #and the sorted numbers from 'a' equals the sorted numbers from 'b'
        return True                                         #then 'a' and 'b' are similar                                   
    elif len(lst1) == 0:                                    #if lst1 is still empty then 'a' and 'b' are identical
        return True
    else:
        return False                                        #if neither conditions are met then 'a' and 'b' are not similar
                                                            #hence return false                                                                    


######################### Test cases ##############################################################################################
    
a = [2, 3, 1]
b = [1, 3, 2]
c = [2, 3, 1]

d = [1, 1, 4]
e = [1, 2, 3]

f = [4, 6, 3]
g = [3, 4, 6]

h = [832, 998, 148, 570, 533, 561, 894, 147, 455, 279]
i = [832, 570, 148, 998, 533, 561, 455, 147, 894, 279]
###################################################################################################################################


print(areSimilar(a, b))
print(areSimilar(a, c))
print(areSimilar(d, e))
print(areSimilar(f, g))
print(areSimilar(h, i))
