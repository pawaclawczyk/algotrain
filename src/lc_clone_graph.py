""" Clone Graph

https://leetcode.com/explore/challenge/card/october-leetcoding-challenge/561/week-3-october-15th-october-21st/3501/

Note: The graph is given as adjacent nodes lists.
I didn't implement the serialization and deserialization of the representation.
That no tests as well.
"""


class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: "Node") -> "Node":
        if not node:
            return node

        def dfs(node: "Node", visited: dict) -> "Node":
            new_node = Node(node.val)
            visited[node.val] = new_node
            for n in node.neighbors:
                if n.val in visited:
                    new_node.neighbors.append(visited[n.val])
                else:
                    new_node.neighbors.append(dfs(n, visited))
            return new_node

        return dfs(node, {})
