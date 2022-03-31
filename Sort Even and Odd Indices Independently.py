class Solution:
    def sortEvenOdd(self, nums: List[int]) -> List[int]:
        n=len(nums)
        res=[0]*n
        odd=[]
        even=[]
        for i in range(0,n,2):
            even.append(nums[i])
        for j in range(1,n,2):
            odd.append(nums[j])
        even.sort()
        odd.sort(reverse=True)
        x=0
        y=0
        for k in range(n):
            if k&1:
                res[k]=odd[y]
                y+=1
            else:
                res[k]=even[x]
                x+=1
        return(res)
        
                    
        