"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node is None:
            return None
        created_nodes = {} #storing node.val to node itself
        visited = set() #storing indices of visited nodes

        def dfs(node: 'Node') -> None:
            if node.val in visited:
                return 
            #check if node exists or create node
            if node.val not in created_nodes:
                created_nodes[node.val] = Node(node.val)
            new_node = created_nodes[node.val]


            # add node.val to visited
            visited.add(node.val)

            # for each neighbor in og node
            for neighbor in node.neighbors:
                # check if exists in created node
                if neighbor.val not in created_nodes:
                    # if not create that node
                    created_nodes[neighbor.val] = Node(neighbor.val)
                # add to neighbors of new node
                new_node.neighbors.append(created_nodes[neighbor.val])
                # dfs on that new node
                dfs(neighbor)
        # dfs node
        dfs(node)
        # return node
        return created_nodes[1]




            
        