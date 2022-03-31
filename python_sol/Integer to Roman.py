class Solution:
    def intToRoman(self, num: int) -> str:
        ans=''
        dict={1: 'I', 4: 'IV', 5: 'V', 9: 'IX', 10: 'X', 40: 'XL', 50: 'L', 90: 'XC', 100: 'C', 400: 'CD', 500: 'D',                    900: 'CM', 1000: 'M'}
        for i in reversed(dict):
            n=num//i
            if n>=1:
                ans+=dict[i]*n
                num%=i
        return ans
        