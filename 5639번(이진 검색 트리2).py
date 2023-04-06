import sys
sys.setrecursionlimit(10**6)

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def create_bst(node_list):
    if len(node_list) == 0:
        return None
 
    root_value = node_list[0]
    root = Node(root_value)
    
    left_subtree = []
    right_subtree = []
    
    for node_value in node_list[1:]:
        if node_value < root_value:
            left_subtree.append(node_value)
        else:
            right_subtree.append(node_value)
    
    root.left = create_bst(left_subtree)
    root.right = create_bst(right_subtree)
    
    return root

def post_order(node):
    if not node:
        return
    post_order(node.left)
    post_order(node.right)
    print(node.value)

pre_order = []
while True:
    try:
        num = int(input())
        pre_order.append(num)
    except:
        break

root_node = create_bst(pre_order)
post_order(root_node)
