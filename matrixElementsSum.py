####### print out sum of numbers from a matrix where the numbers selected do not have a zero above it in the column #############################
#################################################################################################################################################
#################################################################################################################################################
#################################################################################################################################################



matrix = [[0, 1, 1, 2],[0, 5, 0, 0],[2, 0, 3, 3]]

rows_len = len(matrix)       #number of rows in the matrix
cols_len = len(matrix[0])    #number of columns in the matrix
#print(rows_len)
#print(cols_len)


######################### first go through the matrix and create a list of arrays that contain column values from top to bottom #################
list=[]
for i in range(cols_len):              #goes through each column in the matrix
    #print(matrix[i])                  #print row of the matrix
    col=[]
    for j in range(rows_len):          #goes through each item by row of that particular column
        col.append(matrix[j][i])       #for that column append "col" with each item
    list.append(col)                   #append "list" with "col" after each column has been done

print(list)                            #print list containing all column values
#################################################################################################################################################


######################## next go through the values in the arrays in the "list"  and add them up through count unless a zero is encountered######
count = 0                         #start the count with zero
for array in list:                #go through each array in the list
    for val in array:             #go through each value in each array
        if val ==0:               #if a zero is encountered then 
            break
        count += val

print(count)
        
