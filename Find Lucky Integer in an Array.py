class Solution:
    def findLucky(self, arr: List[int]) -> int:
        lst=[]
        for i in range(0,len(arr)):
            x=arr[i]
            count=0
            for j in range(0,len(arr)):
                if(arr[j]==x):
                    count+=1
            if(count==x):
                lst.append(x)
        if(lst==[]):
            return -1
        else:
            return max(lst)