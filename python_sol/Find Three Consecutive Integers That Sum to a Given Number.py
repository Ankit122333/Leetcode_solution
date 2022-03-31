class Solution:
    def sumOfThree(self, num: int):
        lst=[]
        if num % 3 == 0:
            lst.append(num//3-1)
            lst.append(num//3)
            lst.append(num//3+1)
        return lst