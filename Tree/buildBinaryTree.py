class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, val):
        if not self.root:
            self.root = TreeNode(val)
            return
        
        current = self.root
        while True:
            if val < current.val:
                if not current.left:
                    current.left = TreeNode(val)
                    return
                current = current.left
            else:
                if not current.right:
                    current.right = TreeNode(val)
                    return
                current = current.right

    def search(self, val):
        current = self.root
        while current:
            if val == current.val:
                return True
            elif val < current.val:
                current = current.left
            else:
                current = current.right
        return False

    def delete(self, val):
        def min_value_node(node):
            current = node
            while current.left:
                current = current.left
            return current

        def delete_node(root, val):
            if not root:
                return root

            if val < root.val:
                root.left = delete_node(root.left, val)
            elif val > root.val:
                root.right = delete_node(root.right, val)
            else:
                if not root.left:
                    return root.right
                elif not root.right:
                    return root.left

                root.val = min_value_node(root.right).val
                root.right = delete_node(root.right, root.val)

            return root

        self.root = delete_node(self.root, val)

class BuildBinaryTree:
    @staticmethod
    def build_tree(data):
        if not data:
            return None

        root = TreeNode(data[0])
        queue = [root]
        i = 1

        while queue and i < len(data):
            node = queue.pop(0)

            if i < len(data) and data[i] is not None:
                node.left = TreeNode(data[i])
                queue.append(node.left)
            i += 1

            if i < len(data) and data[i] is not None:
                node.right = TreeNode(data[i])
                queue.append(node.right)
            i += 1

        return root