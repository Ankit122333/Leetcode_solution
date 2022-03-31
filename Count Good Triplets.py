class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        n=len(arr)
        count=0
        for i in  range(n):
            for j in range(i+1,n):
                for k in range(j+1,n):
                    xa=abs(arr[i] - arr[j])<=a 
                    xb= abs(arr[j] - arr[k])<=b 
                    xc= abs(arr[i] - arr[k])<=c
                    if all((xa,xb,xc)):
                        count+=1
        return count