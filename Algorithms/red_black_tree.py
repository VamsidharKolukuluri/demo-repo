BLACK = True
RED = False

class Node:
    def __init__(self, key):
        self.key = key
        self.p = None # parent
        self.color = RED # any node initially must be RED
        self.left = None
        self.right = None

    def print_color(self):
        if self.color == BLACK:
            return '(b)'
        return '(r)'

from collections import deque

class RedBlackTree:
    def __init__(self):
        self.NIL = Node(99999)
        self.NIL.color = BLACK
        self.NIL.left = None
        self.NIL.right = None
        self.root = self.NIL # Initialize the root as the NIL node.

    def left_rotate(self, x): # Perform a left rotation on the given node x.
        y = x.right
        x.right = y.left 

        if y.left != self.NIL:
            y.left.p = x
        
        y.p = x.p 

        if x.p is None:
            self.root = y
        elif x == x.p.left:
            x.p.left = y
        else:
            x.p.right = y 

        y.left = x 
        x.p = y

    def right_rotate(self, x): # Perform a right rotation on the given node x.
        y = x.left 
        x.left = y.right 

        if y.right != self.NIL:
            y.right.p = x

        y.p = x.p 

        if x.p is None:
            self.root = y 
        elif x == x.p.right:
            x.p.right = y 
        else:
            x.p.left = y 

        y.right = x 
        x.p = y

    def insert(self, key):
        z = Node(key) # Insert a new key into the Red-Black Tree.
        z.left = self.NIL
        z.right = self.NIL

        y = None 
        x = self.root
        
        while x != self.NIL:
            y = x
            if z.key < x.key:
                x = x.left 
            else:
                x = x.right 
        
        z.p = y 
        if y == None:
            self.root = z 
        elif z.key < y.key: 
            y.left = z 
        else:
            y.right = z

        self.insert_fixup(z)

    def insert_fixup(self, z):  # Fix any violations in the Red-Black Tree after insertion.
        while z.p and z.p.color == RED:
            if z.p == z.p.p.left:
                y = z.p.p.right 
                if y.color == RED:
                    z.p.color = BLACK
                    y.color = BLACK 
                    z.p.p.color = RED
                    z = z.p.p
                else:
                    if z == z.p.right:
                        z = z.p 
                        self.left_rotate(z)
                    z.p.color = BLACK
                    z.p.p.color = RED 
                    self.right_rotate(z.p.p)
            else:
                y = z.p.p.left 
                if y.color == RED:
                    z.p.color = BLACK
                    y.color = BLACK
                    z.p.p.color = RED
                    z = z.p.p
                else:
                    if z == z.p.left:
                        z = z.p 
                        self.right_rotate(z)
                    z.p.color = BLACK
                    z.p.p.color = RED
                    self.left_rotate(z.p.p)
            if z == self.root:
                break
        self.root.color = BLACK

    # Simple level-order tree traversal
    def print_tree(self, print_color=False):
        queue = deque()
        queue.append(self.root)

        while(queue):
            node = queue.popleft()

            if print_color:
                print(f'{node.key}{node.print_color()}', end=' ')
            else:
                print(node.key, end=' ')

            # Don't add NIL nodes
            if node.left != self.NIL:
                queue.append(node.left)
            if node.right != self.NIL:
                queue.append(node.right)

    # Checking the properties of Red Black Trees
    def check_properties(self):
        def is_red(node):
            return node is not None and node.color == RED

        # Property 1: Every node is either red or black.
        # Property 2: The root node is always black.
        # Property 3: Red nodes cannot have red children.
        def check_red_properties(node):
            if node is None:
                return True
            if is_red(node):
                if is_red(node.left) or is_red(node.right):
                    return False
            return check_red_properties(node.left) and check_red_properties(node.right)

        # Property 4: Every path from a node to its descendant leaves must have the same black depth.
        def check_black_depth(node):
            if node is None:
                return 1
            left_black_depth = check_black_depth(node.left)
            right_black_depth = check_black_depth(node.right)
            if left_black_depth != right_black_depth:
                return 0
            return left_black_depth + (1 if node.color == BLACK else 0)

        # Property 5: The leaves of the tree (NIL nodes) are considered black.
        if self.root.color != BLACK:
            return False

        return check_red_properties(self.root) and check_black_depth(self.root) > 0


def main():

    RB = RedBlackTree()

    # Define a list of elements to be inserted.
    print("Enter the Virtual time associated with the processes: ", end="")
    l = input().split(", ")
    
    # Insert elements into the Red-Black Tree.
    for i in l:
        RB.insert(int(i))

    # Print the Red-Black Tree structure in Level-Order.
    print("Level-Order of the Tree: ", end="")
    RB.print_tree()
    print()

    # Check and print whether Red-Black Tree properties are satisfied or violated.
    check = input("Do you want to check the five properties of Red-Black Trees? (Y/N)")
    if check == 'Y' and RB.check_properties():
        print("Red-Black Tree properties are satisfied.")
    elif check == 'N':
        print("Red-Black Tree properties are not checked.")
    else:
        print("Red-Black Tree properties are violated.")

main()
