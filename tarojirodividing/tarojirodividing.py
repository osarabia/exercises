class TaroJiroDividing(object):

    def getNumber(self, a, b):
       taro = self.divideResult(a)
       jiro = self.divideResult(b)

       print "taro:",taro
       print "jiro:",jiro

       return len(taro.intersection(jiro))


    def isEven(self, num):
        if num%2 == 0:
            return True
        return False

    def divideResult(self, num):
        results = []
        if self.validRange(num):
            results.append(num)
            while self.isEven(num):
                num = num / 2
                results.append(num)
            results.append(num)

        return set(results)

    def validRange(self, num):
        return num >= 1 and num <= 1000000

if __name__ == "__main__":
    tarojirodividing = TaroJiroDividing()
    print tarojirodividing.getNumber(7,4)
