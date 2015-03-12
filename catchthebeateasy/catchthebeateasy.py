class CatchTheBeatEasy(object):

    def getDistance(self, source, dest):
        increment = 1
        if source > dest:
            increment = -1
        return len(range(source, dest, increment)) 

    def ableToCatch(self, x, y):
        coordinates = sorted(zip(x,y),key=lambda h:h[1])
        sourcePoint = [0,0]
        timeHappend = 0
        for dest in coordinates:
            print "source:", sourcePoint
            print "Fruta:", dest
            destinationPoint = [dest[0],0]
            print "destinationPoint", destinationPoint
            distance = self.getDistance(sourcePoint[0], destinationPoint[0])
            print "distance:", distance

            if distance == dest[1] - timeHappend:
                timeHappend = timeHappend + distance
            elif distance > dest[1] - timeHappend:
                return "Not able to catch"
            else:
                waitingTime = dest[1] - timeHappend - distance
                print "waitingTime:",waitingTime
                timeHappend = timeHappend + distance + waitingTime
                print "timeHappend:",timeHappend

            sourcePoint = destinationPoint

        return "Able to catch"

if __name__ == "__main__":
   catchthebeateasy = CatchTheBeatEasy()
   #print catchthebeateasy.ableToCatch([-175,-28,-207,-29,-43,-183,-175,-112,-183,-31,-25,-66,-114,-116,-66],
   #                                   [320,107,379,72,126,445,318,255,445,62,52,184,247,245,185])
   #print catchthebeateasy.ableToCatch([0,0,0,0],
   #                                   [0,0,0,0])
   #print catchthebeateasy.ableToCatch([70,-108,52,-70,84,-29,66,-33],
   #                                   [141,299,402,280,28,363,427,232])
   #print catchthebeateasy.ableToCatch([0, -1, 1],
   #                                   [9, 1, 3]) 
   #print catchthebeateasy.ableToCatch([-1, 1, 0],
   #                                   [1, 2, 4]) 
   #print catchthebeateasy.ableToCatch([-3],
   #                                   [2])
   print catchthebeateasy.ableToCatch([-1, 1, 0],
                                      [1, 3, 4])



