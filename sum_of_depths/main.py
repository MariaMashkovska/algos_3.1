class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data


def sum_of_depths(def_root, depth=0):
    if not def_root:
        return 0
    return depth + sum_of_depths(def_root.left, depth + 1) + sum_of_depths(def_root.right, depth + 1)


root = Node(12)
root.left = Node(7)
root.right = Node(30)

result = sum_of_depths(root)
print(result)
