class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        row = len(mat)
        col = len(mat[0])
        newmat = []
        if row*col != r*c:
            return mat
        
        arr = []
        newcol = 0
        for i in range(row):
            for j in range(col):
                arr.append(mat[i][j])
                newcol += 1
                if newcol == c:
                    newmat.append(arr)
                    arr = []
                    newcol = 0
                    
        return newmat
                
        