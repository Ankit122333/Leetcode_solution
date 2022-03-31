'''class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        lst=[]
        for i in s1:
            if s1[i] not in s2:
                lst.append(s1[i])
        return lst'''


class Solution:
    def uncommonFromSentences(self, A: str, B: str) -> List[str]:
        A = A.split() + B.split() 
        resLis = [] 
        for i in A:  
            if A.count(i) == 1: 
                resLis.append(i)
        return resLis 
    
        