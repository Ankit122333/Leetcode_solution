class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) < 3: 
            return False
        flag = 0
        for i in range(len(arr)-1):
            if arr[i] == arr[i+1]: 
                return False
            if flag == 0: 
                if arr[i] > arr[i+1]: 
                    flag = 1
            else:
                if arr[i] <= arr[i+1]: 
                    return False
        return True if arr[-2] > arr[-1] and arr[0] < arr[1] else False
        