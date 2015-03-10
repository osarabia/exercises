class CostOfDancing(object):


    def minimum(self, k, danceCost):
        self.validatingInput(k, danceCost)
        if k == len(danceCost):
            return sum(danceCost)
        else:
            total = 0 
            outerIndex = 0
            while outerIndex < k:
                innerIndex = 1 
                minimumValue = danceCost[0]
                minimumIndex = 0
               
                while innerIndex < len(danceCost):
                    if danceCost[innerIndex] < minimumValue:
                        minimumValue = danceCost[innerIndex]
                        minimumIndex = innerIndex
                    innerIndex = innerIndex + 1

                total = total + minimumValue
                danceCost[minimumIndex] = 1001

                outerIndex = outerIndex + 1
            return total

    def validatingInput(self, k, danceCost):
        danceCostLength = len(danceCost)
        if  danceCostLength < 1 or danceCostLength > 1000:
            raise Exception("Invalid danceCost length")

        for element in danceCost:
            if element < 1 or element > 1000:
                raise Exception("Invalid danceCost Element")

        if not(k >= 1 and k <= 1000 and k <= len(danceCost)):
            raise Exception("invalid number of learning dances")

if __name__ == "__main__":
    costOfDancing = CostOfDancing()
    #print costOfDancing.minimum(2,[1,5,3,4])
    #print costOfDancing.minimum(2,[2,2,4,5,3])
    #print costOfDancing.minimum(1,[2, 2, 4, 5, 3])
    print costOfDancing.minimum(39,[973, 793, 722, 573, 521, 568, 845, 674, 595, 310, 284, 794, 913, 93, 129, 758, 108, 433, 181, 163, 96, 932,
 703, 989, 884, 420, 615, 991, 364, 657, 421, 336, 801, 142, 908, 321, 709, 752, 346, 656, 413, 629, 801])
