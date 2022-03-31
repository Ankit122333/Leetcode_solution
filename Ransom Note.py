class Solution:
    def canConstruct(self, ransomNote: str, magazine: str):
        for i in set(ransomNote):
                if ransomNote.count(i)> magazine.count(i):
                    return False
        return True