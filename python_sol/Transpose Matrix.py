class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        m,n=len(matrix),len(matrix[0])
        mat=[]
        for i in range(n):
            temp=[]
            for j in range(m):
                temp.append(matrix[j][i])
            mat.append(temp)
        return mat
        
        
        '''sol = []
        
        for c in range(len(A[0])):
            tmp = []
            for r in range(len(A)):
                tmp.append(A[r][c])
            
            sol.append(tmp)
        
        return sol'''