import re

class TaroGrid(object):


    def __init__(self):
        self.maxNumMatches = 1

    def getNumber(self, arr):

        self.isValidInput(arr)
        outerIndex = 0
        while outerIndex < len(arr):

            innerIndex = 0
            numOfMatches = 1
            cellValue = arr[innerIndex][outerIndex]

            while innerIndex + 1 < len(arr):
                if cellValue == arr[innerIndex+1][outerIndex]:
                    numOfMatches = numOfMatches + 1
                    if numOfMatches > self.maxNumMatches:
                        self.maxNumMatches = numOfMatches
                else:
                    numOfMatches = 1

                cellValue = arr[innerIndex+1][outerIndex]
                innerIndex = innerIndex + 1

            if self.maxNumMatches == len(arr):
                break

            outerIndex = outerIndex + 1

        return self.maxNumMatches

    def isValidInput(self, array):
        for element in array:
            if not (len(element) >= 1 and len(element) <= 50\
                    and len(element) == len(array) and \
                    bool(re.compile('^[W|B]+$').match(element))):
                raise Exception("Invalid input Array")


if __name__ == "__main__":
    taroGrid = TaroGrid()
    #print taroGrid.getNumber(["W"])
    #print taroGrid.getNumber(["WB","BW"])
    #print taroGrid.getNumber(["BWW","BBB","BWB"])
    print taroGrid.getNumber(["BWB", "BBW", "BWW"])
    #print taroGrid.getNumber(["BBWWBBWW", "BBWWBBWW", "WWBBWWBB", "WWBBWWBB", "BBWWBBWW", "BBWWBBWW", "WWBBWWBB", "WWBBWWBB"])
