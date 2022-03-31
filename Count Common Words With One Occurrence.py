class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        cnt1 = Counter(words1)
        cnt2 = Counter(words2)
        return sum(cnt1[i] == cnt2[i] == 1 for i in cnt1)
        