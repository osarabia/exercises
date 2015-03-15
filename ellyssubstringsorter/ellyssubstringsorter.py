import re

class EllysSubstringSorter(object):

    def areValidInputs(self, S, L):
        if not bool(re.compile('^[A-Z]+$').match(S)):
            raise Exception("Invalid Input String")
 
        if not (len(S) >=2 and len(S) <= 50): 
            raise Exception("Invalid Input String Length")

        if not (len(S) >=L and len(S) <= 50): 
            raise Exception("Invalid Input String Length")


    def getMin(self, S, L):
        self.areValidInputs(S, L)
        index = 0
        while index <= len(S) - L:
            substring = "".join(sorted(S[index:L+index]))
            if ord(substring[0]) < ord(S[index]):
                return S.replace(S[index:L+index], substring)
            index = index + 1
        return S


if __name__ == "__main__":
    ellysSubstringSorter = EllysSubstringSorter()
    #print ellysSubstringSorter.getMin("TOPCODER",4)
    #print ellysSubstringSorter.getMin("ESPRIT",3)
    #print ellysSubstringSorter.getMin("AAAAAAAAA",2)
    #print ellysSubstringSorter.getMin("ABRACADABRA", 5) == "AAABCRDABRA"
    #print ellysSubstringSorter.getMin("BAZINGA", 6) == "ABGINZA"
    #print ellysSubstringSorter.getMin("AAAWDIUAOIWDESBEAIWODJAWDBPOAWDUISAWDOOPAWD", 21) == "AAAAAABDDDEEIIIJOOSUWWWWDBPOAWDUISAWDOOPAWD"
    #print ellysSubstringSorter.getMin("ZZZZZZZCBA", 10) == "ABCZZZZZZZ"
    print ellysSubstringSorter.getMin("OQPWEKPAFKPDOWAEKPRAAAAASSDS", 4) == "OEPQWKPAFKPDOWAEKPRAAAAASSDS"
 
