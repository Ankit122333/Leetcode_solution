class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        '''res=""
        count=len(s)
        for i in range(len(t)):
            if(t[i] not in s):
                res+=t[i]
            else:
                count-=1
        return res'''
        ans = 0
        for i in s:
            ans ^= ord(i)
        for i in t:
            ans ^= ord(i)           
        return chr(ans) 
        