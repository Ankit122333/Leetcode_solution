class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        res=[-1]*len(arr)
        for i in range(len(arr)-1):
            res[i]=max(arr[i+1:])
        return res
        