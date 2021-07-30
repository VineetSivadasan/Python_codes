############### Given a rectangular matrix of characters, add a border of asterisks (*) to it ############################
##########################################################################################################################
################ e.g. ["abc",  ###########################################################################################
###############        "def"]  ###########################################################################################
##########################################################################################################################
############### becomes: ["*****", #######################################################################################
###############           "*abc*", #######################################################################################
###############           "*def*", #######################################################################################
###############           "*****"] #######################################################################################
##########################################################################################################################


################################### Method 1 ##################################################################################################
def addBorder(picture):
    border_size = 1

    max_substring_length = max(map(len, picture))                    #determines the max number of "columns" in the input string

    ############# '*' Top border ##################################################################################################################
    result =['*' * (max_substring_length + border_size * 2)]         #create a list of '*', where list length is the number of columns plus two
    print(result)


    ############# '*' Border in front of and behind the string matrix #############################################################################
    for substring in picture:                                        #go through each row in the input string matrix 
        #print(substring)
        diff = max_substring_length - len(substring)                 #take the difference between the max number of columns in the input string and
                                                                     #the length of the selected string row to see how many '*' are needed
        print(diff)
        additional_length, extra = divmod(diff, 2)                   #determine the additional '*' needed before and after the string by dividing the
                                                                     #difference between max string length and actual string strength, by 2 
        print(additional_length)
        print(extra)
        prepend = '*' * (border_size + additional_length + extra)    #place the required no. of '*' before the string  
        append = '*' * (border_size + additional_length)             #and after the string
        result.append(prepend + substring + append)                  #append the result list with string row along with the '*' before and after the string

    result.append('*' * (max_substring_length + border_size * 2))    #append a list of '*' to result list, where list length is the number of columns plus two

    return result
    



#################################### Method 2 (not quite correct) #############################################################################
def addBorder2(picture):
    rows = len(picture)                                               #assign the number of rows
    columns = len(picture[0])                                         #assign the number of columns
    star_rows = rows + 2                                              #the new number of rows is the existing number of rows plus 2
    star_columns = columns + 2                                        #the new number of columns is the existing number of columns plus 2
    #print(star_columns)
    #print('-'*(star_columns))

    ############ create a matrix which contain two extra columns and rows compared to the input picture and is populated fully with '*' #######
    star_matrix = [['*'*(star_columns)]for y in range(star_rows)]     #create rows of the same length as star_rows where all
                                                                      #columns are of the same length as star_columns and
                                                                      #are populated with '*'


    for idx,text in enumerate(picture):
        star_matrix[idx+1] = '*' + text+ '*'
            
            
    return star_matrix



##################################### Test cases ##############################################################################################
picture = ["abc",
           "ded"]

picture2 = ["abc",
           "def",
           "ghi"]

picture3 = ["abcd",
           "efg",
           "hijk"]

#print(addBorder(picture))
#print(addBorder(picture2))
print(addBorder(picture3))
