class Solution:
    def toHex(self, num: int) -> str:
        if num==0:
            return "0"
        dict = {10:"a", 11:"b", 12:"c", 13:"d", 14:"e", 15:"f"}
        res = ""
        if num<0:
            num+=4294967296
        while num>0:
            rem = num%16
            if rem>=10:
                res=dict[rem]+res
            else:
                res=str(rem)+res
            num//=16
        return res