# Definition for a undirected graph node
# class UndirectedGraphNode(object):
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []
from collections import deque

class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: UndirectedGraphNode
        :rtype: UndirectedGraphNode
        """
        node_map ={}
        if not node:
            return None
        cur = node
        q= deque([])
        q.append(cur)
        node_map[cur] = UndirectedGraphNode(node.label)
        while q:
            top = q.popleft()
            mappedNode = node_map[top]
            # to keep track of neighbor relationships
            for n in top.neighbors:
                # not visited 
                if n not in node_map:
                    newNeighbor =UndirectedGraphNode(n.label)
                    mappedNode.neighbors.append(newNeighbor)
                    node_map[n]=newNeighbor
                    q.append(n)
                # visited
                else:
                    mappedNode.neighbors.append(node_map[n])
                    
        return node_map[cur]
            
