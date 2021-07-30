############################ given and integer array where all the integers are in the range [1,n] and each integer appears once or twice ############
############################ return an array of all the integers that appears twice ##################################################################

def findDuplicates(nums): 
    A = list(set(nums))
    print(A)
    B = sorted(nums)
    print(B)
    c =[]
    for i in A:
        count=0
        for j in B:
            if i == j:
                count+=1
        if count > 1:
            c.append(i)
    print(c)
    return c


########################### another method ###########################################################################################################
######################################################################################################################################################
def findDuplicates_2(nums):
    A = list(set(nums))
    B = sorted(nums)
    c =[]
    for i in range(0,len(A)-1):
        count=0
        #print(i)
        for j in range(0,len(B)-1):
            #print(j)
            if A[i] == B[j]:
                count+=1
        if count > 1:
            #print("YES")
            c.append(A[i])
    print(c)
    return c


nums  = [4,3,2,7,8,2,3,1]

findDuplicates_2(nums)
        
