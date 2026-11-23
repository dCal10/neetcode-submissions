class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        components = 0
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        def dfs(rowI, colI):
            grid[rowI][colI] = '0'
            for horizontal, vertical in directions:
                # check if dir is valid and if value is 1
                newH, newV = rowI + horizontal, colI + vertical
                if 0 <= newH < len(grid) and 0 <= newV < len(grid[0]) and grid[newH][newV] == '1':
                    # dfs on that modified value
                    dfs(newH, newV)


        for rowIndex, row in enumerate(grid):
            for colIndex, val in enumerate(row):
                if val == '1':
                    components += 1
                    dfs(rowIndex, colIndex)
        return components
        

