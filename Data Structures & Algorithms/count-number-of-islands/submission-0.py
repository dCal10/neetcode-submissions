class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        #convert adjancey matrix to list
        adjList = defaultdict(list) # tuple of (row, col) to list of neighbors of tuples (row, col)
        for i, row in enumerate(grid):
            for j, val in enumerate(row):
                if val != "1":
                    continue
                adjList[(i, j)] = []
                if j - 1 >= 0 and row[j - 1] == '1':
                    adjList[(i, j)].append((i, j - 1))
                if j + 1 < len(row) and row[j + 1] == '1':
                    adjList[(i, j)].append((i, j + 1))
                if i + 1 < len(grid) and grid[i + 1][j] == '1':
                    adjList[(i, j)].append((i + 1, j))
                if i - 1 >= 0 and grid[i - 1][j] == '1':
                    adjList[(i, j)].append((i - 1, j))
        print(len(adjList))
        
        seen = set()
        ans = 0


        def dfs_component(vertex: tuple(int, int)) -> None:
            if vertex in seen:
                return
            seen.add(vertex)
            for neighbor in adjList[vertex]:
                if neighbor not in seen:
                    dfs_component(neighbor)

        for node in adjList:
            if node in seen:
                continue
            print(node)
            ans += 1
            dfs_component(node)
        return ans


        
        