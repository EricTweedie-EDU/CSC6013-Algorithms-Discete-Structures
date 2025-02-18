# Program that takes the file numbers.txt and reads the file, takes the data and inputs it into a binary tree
# program takes the tree and outputs an adjacency matrix that represents the graph equivalent of the tree
# considering an edge from the node to its child with weight being the absolute value of the difference between the numbers of the nodes, using the preorder of the nodes

# opening the numbers.txt file
with open('numbers.txt', 'r') as file:
    # reading the file
    data = file.read()
    # splitting the data into an array of strings
    data = data.split()
    # converting the array of strings into an array of integers
    data = [int(i) for i in data]
    # printing the array of integers
    print(data)

# Binary tree function
class Node:
    def __init__(self, d):
        self.Data, self.Left, self.Right = d, None, None

class Tree:
    def __init__(self, d=None):
        if (d == None): # an empty tree
            self.Root = None
        else:
            self.Root = Node(d)
    def insert(self, d):
        def __insertHere__(n, d):
            if (n.Data > d):   # if no node left insert here
                if (n.Left == None):
                    n.Left = Node(d)
                else:          # or try left child
                    __insertHere__(n.Left, d)
            elif (n.Data < d): # if no node right insert here
                if (n.Right == None):
                    n.Right = Node(d)
                else:          # or try right child
                    __insertHere__(n.Right, d)
        if (self.Root == None): # it was an empty tree
            self.Root = Node(d)
        else:
            if (self.Root.Data > d):          # try left child
                if (self.Root.Left == None):  # if empty insert here
                    self.Root.Left = Node(d)
                else:                         # try left subtree
                    __insertHere__(self.Root.Left, d)
            elif (self.Root.Data < d):        # try right child
                if (self.Root.Right == None): # if empty insert here
                    self.Root.Right = Node(d)
                else:                         # try right subtree
                    __insertHere__(self.Root.Right, d)
    def check(self, d):
        def __check__(n, d):
            if (n == None):
                return False
            elif (n.Data == d):
                return True
            elif (n.Data > d):
                return __check__(n.Left, d)
            elif (n.Data < d):
                return __check__(n.Right, d)
        return __check__(self.Root, d)
    def printInorder(self):
        def __visit__(n):
            if (n != None):
                __visit__(n.Left)
                print(n.Data, end=" ")
                __visit__(n.Right)
        print("\n--------")
        __visit__(self.Root)
        print("\n--------")
    def printPreorder(self):
        def __visit__(n, h):
            if (n != None):
                print("---"*h, n.Data)
                __visit__(n.Left, h+1)
                __visit__(n.Right, h+1)
        print("^^^^^^^^^^")
        __visit__(self.Root, 1)
        print("^^^^^^^^^^")
    def printPostorder(self):
        def __visit__(n, h):
            if (n != None):
                __visit__(n.Left, h+1)
                __visit__(n.Right, h+1)
                print("---"*h, n.Data)
        print("==========")
        __visit__(self.Root, 1)
        print("==========")

# adjacency matrix output from tree using the preorder of the elements
    def adjacencyMatrix(self):
        matrix = []
        for i in range(len(data)):
            matrix.append([])
            for j in range(len(data)):
                matrix[i].append(0)
        
        for i in range(len(data)):
                for j in range(i, len(data)):
                    matrix[i][j] = abs(data[i] - data[j])
                
        print(matrix)

# main function
def main():
    tree = Tree()
    for i in data:
        tree.insert(i)
    tree.printPreorder()
    tree.adjacencyMatrix()

main()  