def min_coins(change):
    valid_coins = [50, 25, 10, 5, 1]
    coins = []

    for i in valid_coins:
        division = change//i   #divide the change by the coin to calculate how many of those coins are needed giving only the digits that are left of the decimal point
        change = change % i   #produce the remainder of dividing the change by the coin
        print(change)

        for j in range(division): 
            coins.append(i)   # for the number of coins needed, append the coins list this many times with that particular coin
            print(coins)


        if(change == 0):#if the remainder has become zero then break the loop and return a list of all the coins used in giving the change
            break

    return coins


###########test case

A = 163


print(min_coins(A))
