###### sort a jumbled sentence that contains numbers at the end of each word and remove the number ############

def sortSentence(s):
    word = s.split()
    print(word) #print the individual words in the sentence which are separated by a space
    print(len(word)) #print the number of words in a sentence
    final = [None]*len(word)
    print(final)
    for i in range(len(word)):
        print(int(word[i][-1])) #print out the number at the end of each word
        print(word[i][:-1]) #print each word without the number
        final[int(word[i][-1]) - 1] = word[i][:-1]
    return " ".join(final)




sentence = "is2 This1 sentence4 a3"


print(sortSentence(sentence))
