class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
     
        ROWS, COLS = len(grid), len(grid[0])
        islands = 0
        def checkWholeComponent(rowIndex: int, colIndex: int) -> None:
        #base case: if not valid (out of bouds or 0), return
            #print(f"Recursion: rowIndex: {rowIndex} colIndex: {colIndex}")
            if colIndex < 0 or colIndex >= COLS or rowIndex < 0 or rowIndex >= ROWS or grid[rowIndex][colIndex] == '0':
                #print("Not valid")
                return
            #mark as 0, recurively cal in all 4 directions
            grid[rowIndex][colIndex] = '0'
            directions = [[-1, 0], [1, 0], [0, 1], [0, -1]]
            for rowDelta, colDelta in directions:
                newRowIndex = rowDelta + rowIndex
                newColIndex = colDelta + colIndex
                checkWholeComponent(newRowIndex, newColIndex)
        for rowIndex, row in enumerate(grid):
            for colIndex, val in enumerate(row):
                if val == "1":
                    islands += 1
                    checkWholeComponent(rowIndex,colIndex)
        return islands

