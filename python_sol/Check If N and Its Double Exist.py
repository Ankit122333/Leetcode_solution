class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        res = set()
        for i in arr:
            if 2 * i in res or i / 2 in res: 
                return True
            res.add(i)
        return False
        
        