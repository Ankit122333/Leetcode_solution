class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        maxi,sum1=0,0
        for i in range(len(accounts)):
            sum1=sum(accounts[i])
            maxi=max(sum1,maxi)
        return maxi