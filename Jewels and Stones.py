class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        '''count=0
        j=list(jewels)
        for i in j:
            if j[i] in stones:
                count+=1
        return count
        '''
        counter = collections.Counter(stones)
        count = 0
        for ch in jewels:
            count += counter[ch]
        return count