class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        '''str1=sorted(s)
        str2=sorted(t)
        if(str1==str2):
            return True
        else:
            return False'''
        return sorted(s)==sorted(t)
    