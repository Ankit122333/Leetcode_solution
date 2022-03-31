class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowcheck = [set() for _ in range(9)]
        colcheck = [set() for _ in range(9)]
        boxcheck = [[set() for __ in range(3)] for _ in range(3)]
        
        for i, row in enumerate(board):
            for j, ele in enumerate(row):
                if ele != '.':
                    if ele in rowcheck[i]:
                        return False
                    rowcheck[i].add(ele)
                    if ele in colcheck[j]:
                        return False
                    colcheck[j].add(ele)
                    if ele in boxcheck[i // 3][j // 3]:
                        return False
                    boxcheck[i // 3][j // 3].add(ele)
                    
        return True
