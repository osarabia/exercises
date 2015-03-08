

import re

class DoubleLetter(object):


    def ableToSolve(self, string):
        self.isValidString(string)

        index = 0
        while len(string) > 0 and index < len(string)-1:
            if string[index] == string[index+1]:
                string = string.replace(string[index:index+2],"")
                index = 0
            else:
                index = index + 1

        print "string:",string
        if len(string) > 0:
            return "Impossible"
        return "Possible"


    def isValidString(self, string):
       if len(string) < 1 or len(string) > 50:
          raise Exception("String length should be between 1 and 50 characters")

       if not bool(re.compile('^[a-z]+$').match(string)):
          raise Exception("Inval string characters should be lowercase English letter ('a'-'z')")

if __name__ == "__main__":
   doubleLetter = DoubleLetter()
   #string = "aabccb"
   #string = "aabccbb"
   #string = "abcddcba"
   #string = "abab"
   #string = "aaaaaaaaaa"
   #string = "zzxzxxzxxzzx"
   string = "aababbabbaba"
   print doubleLetter.ableToSolve(string)
