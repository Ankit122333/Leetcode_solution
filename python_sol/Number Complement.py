class Solution:
    def findComplement(self, num: int) -> int:
        '''x=str(bin(num))
        for i in range(len(x)):
            if(x[i]==1):
                x[i]=0
            else:
                x[i]=1
                '''
        num =  bin(num)[2:]
        ans = ""
        for i in str(num):
            if i == '1':
                ans += '0'
            else:
                ans += '1'
        return int(ans,base=2)
                
