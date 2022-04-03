class Solution:
    def convertTime(self, current: str, correct: str) -> int:
#here I have split the the string in two half first one is of hours and second of minutes.
        a = current.split(":")
        b = correct.split(":")
	
	#calculating difference between correct and current in minutes.
        diff = (int(b[0])-int(a[0]))*60 + (int(b[1])-int(a[1]))
        count = 0
        for i in [60,15,5,1]:
            if i <= diff:
                count += diff//i       #finding how many minutes we can use from the given time and add it in count
                diff = diff%i
            if diff == 0:
                return count
            
        return count
        