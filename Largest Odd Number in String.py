class Solution:
    def largestOddNumber(self, num: str) -> str:
        n = len(num)-1
        while(n>0):
            if(int(num[n])%2 != 0):
                return num[0:n+1]
            else:
                n -= 1
        if(n == 0):
            if(int(num[n])%2 != 0):
                return num[0];
            else:
                return ""
        