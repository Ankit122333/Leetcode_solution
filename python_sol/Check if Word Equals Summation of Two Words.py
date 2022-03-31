class Solution:
    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
	    x, y, z = "", "", ""

	    for char in firstWord:
		    x += str(ord(char) - ord('a'))

	    for char in secondWord:
		    y += str(ord(char) - ord('a'))

	    for char in targetWord:
		    z += str(ord(char) - ord('a'))

	    return int(x) + int(y) == int(z)
        