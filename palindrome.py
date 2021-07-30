############################ CODE TO TEST IF A WORD IS A PALINDROME (I.E.: SAME WORD SPELT BACKWARDS ##########################################

def checkPalindrome(inputString):
    stringSize = len(inputString)         #define the length of the input word
    outputString = ""                     #define a new word "outputString" which will be filled with characters
    for i in range(stringSize-1, -1, -1): #python counts from 0 therefore the pointer on the last term would be stringSize-1
        print(inputString[1])                                #2nd (-1) term gives the finishing point and the 3rd (-1) means that we work backwards
        outputString += inputString[i]    #fill "outputString" with characters from the input word but starting backwards
    return outputString                   #pass the outputString word back out







############################## test case words ############################################################################################### 
X = ('acddcabacddca')

Y = checkPalindrome(X)

if Y == X:
    print('pass')
else:
    print('fail')
    

############################# alternative method #############################################################################################
X = ["redivider","deified","civic","radar","level","rotor","giggity"]

for i in X:
    Y = i
    print(Y)
    Z = checkPalindrome(i)
    print(Z)
    if Y == Z:
        print('pass')
    else:
        print('fail')
    
###############################################################################################################################################
