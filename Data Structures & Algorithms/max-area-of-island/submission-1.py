class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        GRID_SIZE = ROWS * COLS
        parents = list(range(GRID_SIZE))
        sizes = [1] * GRID_SIZE

        def find_grid_index(row_index: int, col_index: int) -> int:
            return row_index * COLS + col_index
        
        def find_parent(grid_index: int) -> int:
            if parents[grid_index] != grid_index:
                parents[grid_index] = find_parent(parents[grid_index])
            return parents[grid_index]
        def union(index1: int, index2: int) -> None:
            parent1, parent2 = find_parent(index1), find_parent(index2)
            if parent1 == parent2:
                return
            if sizes[parent2] > sizes[parent1]:
                parent1, parent2 = parent2, parent1
            parents[parent2] = parent1
            sizes[parent1] += sizes[parent2]
        allZeros = True
        for row_index, row in enumerate(grid):
            for col_index, val in enumerate(row):
                if val == 0:
                    continue
                # check if right and up are valid and then union them
                allZeros = False
                for dr, dc in [[1, 0], [0, 1]]:
                    newr, newc = dr + row_index, dc + col_index
                    if newr < ROWS and newc < COLS and grid[newr][newc] == 1:
                        union(find_grid_index(row_index, col_index), find_grid_index(newr, newc)) 
        return 0 if allZeros else max(sizes)       
        
    
        
        
        
        