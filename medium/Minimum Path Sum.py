class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        row, col = len(grid), len(grid[0])
        check = [[float("inf")]*(col+1) for r in range(row+1)]
        check[row-1][col] = 0

        for i in range(row-1,-1,-1):
            for j in range(col-1,-1,-1):
                check[i][j] = grid[i][j] + min(check[i+1][j], check[i][j+1])
        return(check[0][0])