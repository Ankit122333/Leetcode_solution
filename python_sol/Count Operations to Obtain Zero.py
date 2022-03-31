class Solution:
    def countOperations(self, num1: int, num2: int) -> int:
        count=0
        while(min(num1,num2) > 0):
            if num1 >= num2:
                num1 -= num2
                count += 1
            else:
                num2 -= num1
                count += 1
        return count 