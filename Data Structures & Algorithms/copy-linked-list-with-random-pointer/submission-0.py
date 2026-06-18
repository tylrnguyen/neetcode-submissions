"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        list_nodes = {}

        if not head:
            return None

        copy = head
        while copy:
            node = Node(x=copy.val)
            list_nodes[copy] = node
            copy = copy.next
        
        copy = head
        while copy: 
            new_node = list_nodes[copy]
            if copy.next:
                new_node.next = list_nodes[copy.next]
            else:
                None
            if copy.random: 
                new_node.random = list_nodes[copy.random]
            else:
                None
            
            copy = copy.next
        
        return list_nodes[head]



