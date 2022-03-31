class Solution:
    def countEven(self, num: int) -> int:
        count=0
        for i in range(2,num+1):
            add=0
            for x in str(i):
                add+=int(x)
            if(add%2==0):
                count+=1
                
        return count
            
            
            
        