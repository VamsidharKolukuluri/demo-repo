class Node:
    def __init__(self, data):
        self.data = data
        self.parent = None
        self.left = None
        self.right = None

class SplayTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        node = Node(key)
        y = None
        x = self.root

        while x is not None:
            y = x
            if node.data < x.data:
                x = x.left
            else:
                x = x.right

        node.parent = y
        if y is None:
            self.root = node
        elif node.data < y.data:
            y.left = node
        else:
            y.right = node

        self.__splay(node)

    def __splay(self, x):
        while x.parent is not None:
            if x.parent.parent is None:
                if x == x.parent.left:
                    self.__right_rotate(x.parent)
                else:
                    self.__left_rotate(x.parent)
            elif x == x.parent.left and x.parent == x.parent.parent.left:
                self.__right_rotate(x.parent.parent)
                self.__right_rotate(x.parent)
            elif x == x.parent.right and x.parent == x.parent.parent.right:
                self.__left_rotate(x.parent.parent)
                self.__left_rotate(x.parent)
            elif x == x.parent.right and x.parent == x.parent.parent.left:
                self.__left_rotate(x.parent)
                self.__right_rotate(x.parent)
            else:
                self.__right_rotate(x.parent)
                self.__left_rotate(x.parent)

    def __right_rotate(self, x):
        y = x.left
        x.left = y.right
        if y.right is not None:
            y.right.parent = x

        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y

        y.right = x
        x.parent = y

    def __left_rotate(self, x):
        y = x.right
        x.right = y.left
        if y.left is not None:
            y.left.parent = x

        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y

        y.left = x
        x.parent = y

    def preorder_traversal(self, node):
        result = []
        if node:
            result.append(node.data)
            result += self.preorder_traversal(node.left)
            result += self.preorder_traversal(node.right)
        return result

    def lookup(self, key):
        if not self.root:
            return None  # Tree is empty

        result = self._lookup(self.root, key)
        if result:
            self.__splay(result)  # Splay the found node to the root
        return result

    def _lookup(self, node, key):
        while node is not None:
            if key == node.data:
                return node
            elif key < node.data:
                node = node.left
            else:
                node = node.right
        return None

    def delete(self, key):
        if not self.root:
            return  # Tree is empty

        # Find the node with the key
        node = self.lookup(key)

        if not node:
            return  # Key not found

        # Splay the node to the root
        self.__splay(node)

        # Case 1: Node has no children
        if not node.left and not node.right:
            if node.parent:
                if node == node.parent.left:
                    node.parent.left = None
                else:
                    node.parent.right = None
            else:
                self.root = None  # If it's the root node, set the root to None

        # Case 2: Node has one child
        elif node.left and not node.right:
            if node.parent:
                if node == node.parent.left:
                    node.parent.left = node.left
                else:
                    node.parent.right = node.left
                node.left.parent = node.parent
            else:
                self.root = node.left  # Update the root if necessary

        elif not node.left and node.right:
            if node.parent:
                if node == node.parent.left:
                    node.parent.left = node.right
                else:
                    node.parent.right = node.right
                node.right.parent = node.parent
            else:
                self.root = node.right  # Update the root if necessary

        # Case 3: Node has two children
        else:
            # Find the maximum element in the left subtree
            max_left_subtree = self.__find_max(node.left)

            # Splay the maximum element to the root of the left subtree
            self.__splay(max_left_subtree)

            # Attach the right subtree as the right child of the maximum element
            max_left_subtree.right = node.right
            node.right.parent = max_left_subtree

            # Update the parent pointer of the root
            max_left_subtree.parent = None
            self.root = max_left_subtree

        return

    def __find_max(self, node):
        while node.right:
            node = node.right
        return node

def ip_to_decimal(ip_address):
    # Split the IP address into octets
    octets = ip_address.split('.')
    
    # Ensure there are 4 octets
    if len(octets) != 4:
        raise ValueError("Invalid IP address format")

    # Convert each octet to decimal and calculate the decimal equivalent
    decimal_ip = 0
    for octet in octets:
        decimal_ip = (decimal_ip << 8) | int(octet)

    return decimal_ip

# Example usage of the Splay Tree:
splay_tree = SplayTree()

ip_address = input("Enter IPs: ").split(", ")
dictionary = {}

for i in ip_address:
    decimal_ip = ip_to_decimal(i)
    dictionary[decimal_ip] = i

for val in dictionary.keys():
    splay_tree.insert(val)
    print("After inserting IP "+ str(dictionary.get(val)) + " Pre-Order Traversal is: ")
    print("IPs:", end=" ")
    for x in splay_tree.preorder_traversal(splay_tree.root):
        print(dictionary.get(x), end=", ")
    print()
    print()

delete_node = input("Enter the IP you want to delete: ")
splay_tree.delete(ip_to_decimal(delete_node))
for x in splay_tree.preorder_traversal(splay_tree.root):
        print(dictionary.get(x), end=", ")

print()
print()

search = input("Enter the IP you want to lookup: ")
splay_tree.lookup(ip_to_decimal(search))
for x in splay_tree.preorder_traversal(splay_tree.root):
        print(dictionary.get(x), end=", ")
