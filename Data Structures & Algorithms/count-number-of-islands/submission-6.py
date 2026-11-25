class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
     
        ROWS, COLS = len(grid), len(grid[0])
        GRID_SIZE = ROWS * COLS
        parents = list(range(GRID_SIZE))
        islands = GRID_SIZE
        #takes parent index
        def find(node: int) -> int:
            if parents[node] != node:
                parents[node] = find(parents[node])
            return parents[node]
        def find_parent_index(row_index: int, col_index: int) -> int:
            return row_index * COLS + col_index
        #check if second nodes is valid and both 1s before passing into function
        #takes parent index paramters 
        def union(node1: int, node2: int) -> None:
            nonlocal islands
            parent_node_1 = find(node1)
            parent_node_2 = find(node2)
            if parent_node_1 == parent_node_2: 
                return
            islands -= 1
            parents[parent_node_2] = parent_node_1

        for row_index, row in enumerate(grid):
            for col_index, val in enumerate(row):
                if val == '0':
                    islands -= 1
                    continue
                #union down and right if valid

                #check right
                if col_index < COLS - 1 and grid[row_index][col_index + 1] == "1":
                    union(find_parent_index(row_index, col_index), find_parent_index(row_index, col_index + 1))          
                #check down
                if row_index < ROWS - 1 and grid[row_index + 1][col_index] == "1":
                    union(find_parent_index(row_index, col_index), find_parent_index(row_index + 1, col_index))     
        return islands
        
        
        
