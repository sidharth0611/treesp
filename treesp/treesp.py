class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

# This function creates binary search tree
def insert(root, key):
    if root is None:
        return Node(key)
    else:
        # If key exists return root
        if root.val == key:
            return root
        # If key is smaller than root check left sub-Tree
        elif root.val < key:
            root.right = insert(root.right, key)
        # If key is greater than root check left sub-Tree
        else:
            root.left = insert(root.left, key)
    return root

# maxDepth of a Tree
def maxDepth(node):
    if node is None:
        return 0 
    else :
        # Compute the depth of each subtree
        lDepth = maxDepth(node.left)
        rDepth = maxDepth(node.right)
 
        # Use the larger one
        if (lDepth > rDepth):
            return lDepth+1
        else:
            return rDepth+1

# Inorder traversal
def inorder(root):
    if root == None:
        return []
    # Traverse to left sub-Tree
    left = inorder(root.left)
    # Traverse to right sub-Tree
    right = inorder(root.right)

    # Return addition of left, root, right
    return left + [root.val] + right # Inorder traversal of BST returns a sorted array

# Postorder traversal
def postorder(root):
    if root == None:
        return []
    # Traverse to left sub-Tree
    left = inorder(root.left)
    # Traverse to right sub-Tree
    right = inorder(root.right)

    # Return addition of left, right, root
    return left + right + [root.val]

# Preorder traversal
def preorder(root):
    if root == None:
        return []
    # Traverse to left sub-Tree
    left = inorder(root.left)
    # Traverse to right sub-Tree
    right = inorder(root.right)

    # Return addition of root, left, right
    return [root.val] + left + right 

# Level order Traversal
def levelorder(root):
    if root == None:
        return None

    result = []
    tmplist = []

    # If the root is a leaf append it to tmplist traverse
    # return the value, again it will check in next 
    # sub-Tree, it will append it to tmplist and then append it to
    # result
    if root.left == None and root.right == None:
        tmplist.append(root.val)
        result.append(tmplist)
        return result

    # This will help to find number of nodes inside the new root 
    # which is a root of subTree of main root
    nodes = []
    nodes.append(root)
    
    while(len(nodes)>0):
        tmplist = []
        length = len(nodes)
        for i in range(length):
            node = nodes.pop(0)
            tmplist.append(node.val)
            if node.left:
                nodes.append(node.left)
            if node.right:
                nodes.append(node.right)

        result.append(tmplist) # It will return list which will have list of each level of tree

    return result

def findLCA(root, n1, n2):
    if root is None:
        return None
 
    # If either n1 or n2 matches with root's key, report
    #  the presence by returning root (Note that if a key is
    #  ancestor of other, then the ancestor key becomes LCA
    if root.val == n1 or root.val == n2:
        return root
 
    # Look for keys in left and right subtrees
    left_lca = findLCA(root.left, n1, n2)
    right_lca = findLCA(root.right, n1, n2)
 
    # If both of the above calls return Non-NULL, then one key
    # is present in one subtree and other is present in other,
    # So this node is the LCA
    if left_lca and right_lca:
        return root.val
 
    # Otherwise check if left subtree or right subtree is LCA
    return left_lca if left_lca is not None else right_lca



