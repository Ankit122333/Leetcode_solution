class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        '''lst=[]
        for i in range(len(arr)):
            count=0
            for j in range(len(arr)):
                if(arr[j]==arr[i]):
                    count+=1
            lst.append(count)
        return True if set(lst)==lst else False'''
        d={}
        for i in arr:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        if len(set(d.values()))==len(d.values()):
            return True
        return False