class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        mul = 1
        add = 0
        for i in str(n):
            mul = mul * int(i)
            add += int(i)
        return mul-add