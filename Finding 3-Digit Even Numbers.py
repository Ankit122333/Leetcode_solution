from itertools import permutations
class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        ans = set()
        perm = permutations(digits,3)
        for p in perm:
            if p[0]==0 or p[2]%2==1:
                continue
            ans.add((100*p[0])+(10*p[1])+p[2])
        
        return sorted(list(ans))
        