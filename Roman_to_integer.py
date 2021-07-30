##################### Convert roman numerals to integer ################################################################################################
##################################################################################################################################

class Solution():
   def romanToInt(self, s):
      """
      :type s: str
      :rtype: int
      """

      #create a dictionary 
      roman = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000,'IV':4,'IX':9,'XL':40,'XC':90,'CD':400,'CM':900}    #a dictionary of roman numerals and the 6 subtraction cases
      
      
      i = 0         #set a counter to run through the characters of the roman numeral input
      num = 0       #integer translation of roman numeral input
      while i < len(s):  #construct a while loop running through the length of the input roman numeral
         if i+1<len(s) and s[i:i+2] in roman: #this if statement checks for the 6 subtraction cases ie: the two consective roman numerals
                                              #and that the loop position is still within the second to last characters of the input
            print(True)
            num+=roman[s[i:i+2]]    #if the above conditions are met then add the numerical value of roman numerals to num
            i+=2     #move along loop position by two
         else:
            print(False)
            num+=roman[s[i]]    #if the conditions are not met, then add roman numerical character value from the dictionary to num
            i+=1     #move along loop position by one
      return num
ob1 = Solution()
print(ob1.romanToInt("III"))
print(ob1.romanToInt("CDXLIII"))
