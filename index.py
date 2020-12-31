# DFS Tree for Searching Node!

# // Import library
import csv
from collections import deque

# // Get data
CsvPath = '/home/nufik/Documents/Kuliah/Tugas/AI/data.csv'
getData = open(CsvPath)
initData = csv.reader(getData)
documents = []

# // Get from CSV and assign them to List
for row in initData:
    documents.append(row)
# // Convert data type of few elements from List
for index, row in enumerate(documents):
    if index != 0:
        row[0] = int(row[0])
        row[3] = float(row[3])
        row[4] = int(row[4])
# // Result of Data Book!
# print(bookData)

# Python code to insert a node in AVL tree

class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.height = 1

class AVL_Tree(object):

    def insert(self, root, key):
        if not root:
            return TreeNode(key)
        elif key < root.val:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)
        root.height = 1 + max(self.getHeight(root.left),
                              self.getHeight(root.right))
        balance = self.getBalance(root)
        if balance > 1 and key < root.left.val:
            return self.rightRotate(root)
        if balance < -1 and key > root.right.val:
            return self.leftRotate(root)
        if balance > 1 and key > root.left.val:
            root.left = self.leftRotate(root.left)
            return self.rightRotate(root)
        if balance < -1 and key < root.right.val:
            root.right = self.rightRotate(root.right)
            return self.leftRotate(root)
        return root

    def leftRotate(self, z):
        y = z.right
        T2 = y.left
        y.left = z
        z.right = T2
        z.height = 1 + max(self.getHeight(z.left),
                           self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left),
                           self.getHeight(y.right))
        return y

    def rightRotate(self, z):
        y = z.left
        T3 = y.right
        y.right = z
        z.left = T3
        z.height = 1 + max(self.getHeight(z.left),
                           self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left),
                           self.getHeight(y.right))
        return y

    def getHeight(self, root):
        if not root:
            return 0
        return root.height

    def getBalance(self, root):
        if not root:
            return 0
        return self.getHeight(root.left) - self.getHeight(root.right)

    def depthFirstSearch(self, root, target):
        global isDocumentExist
        if not root:
            return
        if root.val == target:
            isDocumentExist = True
        print(f'Node yang ditelusuri -> {root.val}')
        self.depthFirstSearch(root.left, target)
        self.depthFirstSearch(root.right, target)

    def bestFirstSearch(self, root, target):
        queue = deque()
        queue.append(root)
        while queue:
            global isDocumentExist
            curr = queue.popleft()
            # print(curr.val, end=' ')
            if curr.val == target:
                isDocumentExist = True
            if curr.left:
                queue.append(curr.left)
            if curr.right:
                queue.append(curr.right)

# // Init the Tree
myTree = AVL_Tree()
root = None

# // Properties!
target = 739322206
isDocumentExist = False

# // Create the AVL Tree! (Insertion)
for index, document in enumerate(documents):
    if index != 0:
        isbn = document[4]
        root = myTree.insert(root, isbn)

# // Search a document with Dept First Search
# // myTree.depthFirstSearch(root, target)
myTree.bestFirstSearch(root, target)

# // The result
if isDocumentExist == True:
    print('-------------------------------------------------------------------------------')
    print("Document status : Ditemukan")
    for document in documents:
        if document[4] == target:
            print(document)
else:
    print('-------------------------------------------------------------------------------')
    print("Document status : Tidak ditemukan")
