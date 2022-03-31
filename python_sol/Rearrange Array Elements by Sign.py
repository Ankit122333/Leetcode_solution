class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        n=len(nums)
        pos=[]
        neg=[]
        arr=[]
        for i in nums:
            if (i>0):
                pos.append(i)
            else:
                neg.append(i)
        pos.reverse()
        neg.reverse()
        for x in range(n):
            if (x%2==0):
                a=pos.pop()
            else:
                a=neg.pop()
            arr.append(a)
    
        return arr
        