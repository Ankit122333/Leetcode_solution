class Solution:
    def sortSentence(self, s: str) -> str:
        x = s.split()
        res = {}
        for i in x :
            res[i[-1]] = i[:-1]
        return ' '.join([res[j] for j in sorted(res)])
        