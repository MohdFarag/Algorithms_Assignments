# Binary Search Tree Class Implementation
class BST:
	def __init__(self, key):
		self.left = None
		self.right = None
		self.Data = key

# Insert Element Function
def insert(root, key):
	if root is None:
		return BST(key)
	else:
		if root.Data == key:
			return root
		elif root.Data < key:
            # Bigger elements on right
			root.right = insert(root.right, key)
		else:
            # Smaller elements on right
			root.left = insert(root.left, key)
	return root

# Print elements in Inorder
def inorder(root):	
	if root:
		inorder(root.left)
		print(root.Data)
		inorder(root.right)

# Print elements in Preorder
def preorder(root):
	if root:
		print(root.Data)
		preorder(root.left)
		preorder(root.right)

# Print elements in Postorder
def postorder(root):
	if root:
		postorder(root.left)
		postorder(root.right)
		print(root.Data)

# By iteration
def find_minimum_element_iteration(root): 
    BST = root 

    while BST.left != None : 
        BST = BST.left 
    
    return BST.Data

# By Recursion
def find_minimum_element_recursion(root): 
    BST = root
    
    if BST.left == None:
        return BST.Data 
    
    return find_minimum_element_recursion(BST.left)

# Main File
if __name__ == "__main__":
	n= int(input())
	arr = input().split()
	r = BST(int(arr[0]))
	
	for i in arr[1:]:
		r = insert(r, int(i))

	Q1 = "The minimum using recursion ="
	Q2 = "The minimum using iteration ="
	print(Q1,find_minimum_element_recursion(r))
	print(Q2,find_minimum_element_iteration(r))

	"""To check the class work or not"""
	# print("-"*100)
	# inorder(r)
	# print("-"*100)
	
	# preorder(r)
	# print("-"*100)
	
	# postorder(r)
	