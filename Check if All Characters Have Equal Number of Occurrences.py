class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        s = Counter(s)
        return len(set(s.values())) == 1