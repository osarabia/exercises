import re

class DecipherabilityEasy(object):


    def check(self, s, t):
        self.areValidInputs(s, t)
        if len(s) == len(t) + 1:
            index = 0
            while index < len(s):
                if index == 0:
                    newString = s[1:]
                elif index == len(s) -1:
                    newString = s[:-1]
                else:
                    newString = s[:index] + s[index+1:]

                if newString == t:
                    return "Possible"

                index = index + 1

        return "Impossible"


    def areValidInputs(self, s, t):
        if not (len(s) > 0 and len(s) < 51):
            raise Exception("Invalid String length")

        if not (len(t) > 0 and len(t) < 51):
            raise Exception("Invalid String length")

        if not bool(re.compile('^[a-z]+$').match(s)):
            raise Exception("Inval string characters")

        if not bool(re.compile('^[a-z]+$').match(t)):
            raise Exception("Inval string characters")


if __name__ == "__main__":
    decipherabilityEasy = DecipherabilityEasy()
    #print decipherabilityEasy.check("sunuke", "snuke")
    #print decipherabilityEasy.check("snuke", "skue")
    #print decipherabilityEasy.check("snuke", "snuke")
    #print decipherabilityEasy.check("snukent", "snuke")
    #print decipherabilityEasy.check("aaaaa", "aaaa")
    #print decipherabilityEasy.check("aaaaa", "aaa")
    #print decipherabilityEasy.check("topcoder", "tpcoder")
    print decipherabilityEasy.check("singleroundmatch", "singeroundmatc")
