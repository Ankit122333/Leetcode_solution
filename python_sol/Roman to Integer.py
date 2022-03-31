class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {'I' : 1, 'V' : 5, 'X' : 10, 'L' : 50, 'C' : 100, 'D' : 500, 'M' : 1000}
        i = len(s) - 1 
        num = 0
        while i >= 0:
            if i-1 >= 0 and roman[s[i-1]] < roman[s[i]]:
                num += (roman[s[i]] - roman[s[i-1]])
                i -= 2
            else:
                num += roman[s[i]]
                i -= 1
        return num
        