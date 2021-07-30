############### function to find out if two input words are anagrams of each other ############################################### 

def anagram(X,Y):
    z=""
    for i in X:
        for j in Y:
            if i == j:
                z+=i
                Y=Y.replace(j, '', 1) #make sure the same letter in Y is not sampled twice
                print(z)
                print(X)
                print(Y)
    if z==X or Y=='':   #all the letters taken from Y has filled z and if z = X or Y is empty
        return True
    else:
        return False


################## test cases
X = "silent"

Y = "listen"

print(anagram(X,Y))
