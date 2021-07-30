####################### Ticket numbers usually consist of an even number of digits. A Ticket is considered lucky if the #############
####################### sum of the first half of the digits is equal to the sum of the second half ##################################
####################### Given a ticket number, determine if it is lucky or not ######################################################

 


def isLucky(n):
    #turn the number into a list of individual digits
    num = [int(d) for d in str(n)]      #loop through n in string format and turn the iterator d into an integer
    print(num)


    length = len(num)                   #full length of "num" list
    print(length)
    first_half = length//2              #half length of "num" list
    print(first_half)
    
    x=[]                                #list to fill with the first half of the ticket numbers
    y=[]                                #list to fill with the second half of the ticket numbers

    ######## in "for loop "range" function" the first term in the brackets is either zero or the starting point (remember python starts
    ######## counting from zero) and the last term in the bracket is not included; i.e. in python range goes up to max_value-1
    
    for i in range(0,first_half):       #"for loop" to iterate through the length of the first half of "num" list 
        x.append(num[i])                #append x with digits up to the first half of "num" list

    for j in range(first_half,length):  #"for loop" to iterate through the length of the second half of "num" list 
        y.append(num[j])                #append y with digits from the second half of the "num" list

    print(x)
    print(y)

    print(sum(x))
    print(sum(y))

    if sum(x) == sum(y):                #boolean statement, if the sum of x equals the sum of y 
        return True                     #then print true
    else:
        return False                    #else print false



################### test case 1 #############################
n = 1230
print(isLucky(n))



################### test case 2 #############################
n = 239017
print(isLucky(n))  
