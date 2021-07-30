############ Given an array of positive integers, return another array which contains two integers ################
############ where the first element is the sum of the odd number positioned integers #############################
############ and the second element is the sum of the even number positioned integers #############################


def alternatingSums(a):
    team2 = (a[0:len(a):2])
    team1 = (a[1:len(a):2])
    return sum(team2), sum(team1)
    


############## Test cases #########################
a = [50, 60, 60, 45, 70]

###################################################


print(alternatingSums(a))
