class SumOfPower(object):

     def findSum(self, arr):
         self.isValidArray(arr)

         total = 0
         outerIndex = 0
         while outerIndex < len(arr):
             innerIndex = 0
             while innerIndex + outerIndex + 1 <= len(arr):
                 total = total + sum(arr[innerIndex:innerIndex+outerIndex+1])
                 innerIndex = innerIndex + 1
             outerIndex = outerIndex + 1

         return total

     def isValidArray(self, arr):
         if len(arr) < 1 or len(arr) > 50:
             raise Exception("Array length should between 1 and 50")

         newArr = [element for element in arr if element < 1 or element > 100]

         if len(newArr) > 0:
             raise Exception("Invalid element on Array")

if __name__ == "__main__":
   sumOfPower = SumOfPower()
   print sumOfPower.findSum([1,1,1])
   print sumOfPower.findSum([1,2])
   print sumOfPower.findSum([1,2,3,4,5,6,7,8,9,10])
   print sumOfPower.findSum([3,14,15,92,65])
