# Trees

## Problems

### I. Write a method for the `BinarySearchTree` class that returns the minimum in the binary search tree using recursion

```Python
def find_minimum_element_ recursion(root):
    Node = root
    if Node.left == None:
        return Node.Data
    return find_minimum_element_ recursion(Node.left)
```

---

### IV. Write a method for the `BinarySearchTree` class that returns the minimum in the binary search using iteration

```Python
def find_minimum_element_ iteration(root):
    Node = root
    while Node.left != None :
        Node = Node.left

    return Node.Data
```

---

#### Input Format

First line: 𝑛.
Second line: 𝑎1, 𝑎2, . . , 𝑎𝑛.

#### Output Format

The minimum using recursion = min
The minimum using iteration = min

#### Sample

```Terminal
9
8 3 10 1 6 14 4 7 13
```

#### Output

```Terminal
The minimum using recursion = 1
The minimum using iteration = 1
```

---

### V. A binary search tree has n nodes. Determine the worst-case runtime complexity using Big-O notation for the following operations on the BinarySearchTree if the tree is balanced and if the tree is not balanced. A binary tree is balanced if every level is full except possibly the last level.

- if tree is balanced : O(log n)

- if tree is not balanced : O(n)

## References

- algorithm - Time Complexity for Finding the Minimum Value of a Binary Tree - Stack Overflow

- Binary Search Tree | Set 1 (Search and Insertion) - GeeksforGeeks

- Tree Traversals (Inorder, Preorder and Postorder) - GeeksforGeeks
