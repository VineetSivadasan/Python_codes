############################### Given two strings, s1 and s2, find the number of common characters between them #####################

#########  Test case   #####################
s1 = "aabcc"
s2 = "adcaa"
#############################################


def commonCharacterCount(s1, s2):
    lst = []               #create a list called "lst"
    s1_list = list(s1)     #turn the string of characters into a list
    s2_list = list(s2)     #turn the string of characters into a list

    #print(s1_list)
    #print(s2_list)
    
    for i in range(len(s1_list)):          #"for loop" starting with the first character in s1
        for j in range(len(s2_list)):      #nested "for loop" taking the term in s1 and going through s2, term by term 
            if s1_list[i] == s2_list[j]:   #see if terms in s1 match with terms in s2
                lst.append(s1_list[i])     #if so, then append "lst" with the terms from s1
                s2_list.pop(j)             #remove the term that was matched from s2 list so that it doesn't get picked up again
                break                      #break the nested "for loop" for that particular s2 term and
                                           #move on to the next s1 term
    return len(lst)                        #return the length of the "lst" list
                


print(commonCharacterCount(s1,s2))
