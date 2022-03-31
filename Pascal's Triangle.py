class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result=[]
        pre=[]
        pre.append(1)
        result.append(pre)
        for i in range(0, numRows-1):
            x = []
            x.append(1)
            for j in range(0, len(pre)-1):
                x.append(pre[j]+pre[j+1])    
            x.append(1)
            result.append(x)
            pre = x

        return result