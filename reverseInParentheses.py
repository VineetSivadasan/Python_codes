########################## For a given input string, reverse the characters in parentheses ##################################################


######## the principle here is to loop through inputString and store the positions of the opening brackets ##################################
######## then when coming across the first closing bracket, store all terms starting from its opening bracket to ############################
######## the closing bracket into a temporary variable which is then reversed and the inputString ###########################################
######## is re-built with the reversed bracket section. Next we need to delete the position of the last open bracket in the list ############
######## and repeat the process of collecting and storing terms from the next opening bracket to the next closing bracket ###################

def reverseInParentheses(inputString):
    a = inputString                                 #re-name the input string
    length = len(a)                                 #assign the length of the string
    
    br=[]                                           #list to store position of the empty bracket
    for i in range(length):
        if a[i] == '(':
            br.append(i)                            #store the position of the opening bracket

        elif a[i] == ')':                           #when a closing bracket is encountered
            temp = a[br[-1]:i + 1]                  #store in a 'temp' variable
                                                    #values of 'a' from the position of the
                                                    #inner most opening bracket (including the
                                                    #bracket), up to its closing bracket
            a = a[:br[-1]] + temp[::-1] + a[i + 1:] #re-build the input string as characters up to selected
                                                    #opening bracket followed by reversed bracket section and
                                                    #then followed by remaining characters
            del br[-1]                              #delete the last opening bracket in the bracket position list, i.e. move 
                                                    #outwards to the next opening bracket and repeat the above process

    ### now remove the brackets in the string  
    result = ""                                     #create an empty string
    for i in range(length):                         #loop through the re-built string 'a' 
        if (a[i] != ')' and a[i] != '('):           #and wherever a bracket is not encountered 
            result += (a[i])                        #add those terms in the string to the 'result'
    return result                                   #return the result 

        




############# Test cases #########################
a = "(bar)"
b = "foo(bar)baz"
c = "foo(bar)baz(blim)"
d = "foo(bar(baz))blim"
e = "fo(barl(hslm(nsh))nei)hwu"
#d = "foo(barzab)blim"
# foobazrabblim
##################################################  


print(reverseInParentheses(a))
print(reverseInParentheses(b))
print(reverseInParentheses(c))
print(reverseInParentheses(d))
print(reverseInParentheses(e))




