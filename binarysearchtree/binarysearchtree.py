import csv

# Define the Node class
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# Function to insert a node into the binary search tree
def insert(root, data):
    if root is None:
        return Node(data)
    if data < root.data:
        root.left = insert(root.left, data)
    else:
        root.right = insert(root.right, data)
    return root

# Function to print the binary search tree in in-order traversal
def print_tree_inorder(node):
    if node is not None:
        print_tree_inorder(node.left)
        print(node.data)
        print_tree_inorder(node.right)

# Read the CSV file
with open('E:\\python\\trabalhofinal\\notas.csv', 'r') as file:
    reader = csv.reader(file, delimiter=';')
    next(reader)
    data = [float(row[2]) for row in reader]

# Sort the data
data.sort()

# Create the binary search tree
root = None
for element in data:
    root = insert(root, element)

# Print the binary search tree in in-order traversal
print_tree_inorder(root)
