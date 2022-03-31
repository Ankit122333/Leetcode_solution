class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        cnt = collections.Counter(heights)
        i, ans = 1, 0
        for h in heights:
            while cnt[i] == 0: 
                i += 1         
            if i != h:         
                ans += 1       
            cnt[i] -= 1        
        return ans
        