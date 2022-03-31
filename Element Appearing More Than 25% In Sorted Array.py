class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        dict = {}
        number = int(0.25*len(arr))
        for i in arr:
            if i not in dict:
                dict[i] = 1
            else: 
                dict[i]+=1
        for i,j in dict.items():
            if j>number:
                return i