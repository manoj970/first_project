
from collections import deque
class Tree:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None
root = Tree(20)
root.left = Tree(10)
root.right = Tree(25)
root.left.left = Tree(5)
def max_depth(root):
    if not root:
        return 0
    queue = deque([root]) 
    depth = 0
    while queue:
        for i in range(len(queue)):
            node = queue.popleft()
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        depth +=1
    return depth
print(max_depth(root) )                      