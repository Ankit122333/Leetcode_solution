class Solution:
    def isPalindrome(self, s: str) -> bool:
        s1 = ''.join(ch for ch in s if ch.isalnum())
        s2=s1.lower()
        string = "".join(reversed(s2))
        if(s2==string):
            return True
        else:
            return False