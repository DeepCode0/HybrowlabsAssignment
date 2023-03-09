class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None
        self.count = 0

    def insert(self, item):
        if self.root is None:
            self.root = TreeNode(item)
            self.count += 1
        else:
            self._insert_helper(self.root, item)

    def _insert_helper(self, node, item):
        if item < node.value:
            if node.left is None:
                node.left = TreeNode(item)
                self.count += 1
            else:
                self._insert_helper(node.left, item)
        elif item > node.value:
            if node.right is None:
                node.right = TreeNode(item)
                self.count += 1
            else:
                self._insert_helper(node.right, item)

    def delete(self, item):
        self.root, deleted = self._delete_helper(self.root, item)
        if deleted:
            self.count -= 1

    def _delete_helper(self, node, item):
        if node is None:
            return node, False
        elif item < node.value:
            node.left, deleted = self._delete_helper(node.left, item)
        elif item > node.value:
            node.right, deleted = self._delete_helper(node.right, item)
        else:
            if node.left is None and node.right is None:
                node = None
                deleted = True
            elif node.left is None:
                node = node.right
                deleted = True
            elif node.right is None:
                node = node.left
                deleted = True
            else:
                min_node = self._find_min(node.right)
                node.value = min_node.value
                node.right, deleted = self._delete_helper(node.right, min_node.value)
        return node, deleted

    def _find_min(self, node):
        while node.left is not None:
            node = node.left
        return node

    def search(self, item):
        return self._search_helper(self.root, item)

    def _search_helper(self, node, item):
        if node is None:
            return False
        elif item == node.value:
            return True
        elif item < node.value:
            return self._search_helper(node.left, item)
        else:
            return self._search_helper(node.right, item)

    def size(self):
        return self.count
