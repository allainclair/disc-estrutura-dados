class BinSearchTreeNode:
    def __init__(self, value):
        self.value = value

        self.left = None
        self.right = None

    def insert(self, new_value):
        if new_value < self.value:
            if self.left is None:
                self.left = BinSearchTreeNode(new_value)
            else:
                self.left.insert(new_value)
        else:
            if self.right is None:
                self.right = BinSearchTreeNode(new_value)
            else:
                self.right.insert(new_value)


def inorder(tree_node):
    if tree_node.left != None:
        inorder(tree_node.left)
    print(tree_node.value)
    if tree_node.right != None:
        inorder(tree_node.right)


def preorder(tree_node):
    print(tree_node.value)
    if tree_node.left != None:
        preorder(tree_node.left)
    if tree_node.right != None:
        preorder(tree_node.right)


def postorder(tree_node):
    if tree_node.left != None:
        postorder(tree_node.left)
    if tree_node.right != None:
        postorder(tree_node.right)
    print(tree_node.value)





def main():
    value = 10
    root = BinSearchTreeNode(value)

    value = 7
    root.insert(value)

    value = 2
    root.insert(value)

    value = 9
    root.insert(value)

    value = 15
    root.insert(value)

    print('INorder')
    inorder(root)
    print('PREorder')
    preorder(root)
    print('POSTorder')
    postorder(root)


if __name__ == '__main__':
    main()
