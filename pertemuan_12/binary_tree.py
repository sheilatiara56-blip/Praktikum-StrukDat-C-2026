class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
class Gudang_tree:
    def __init__(self):
        self.root = None

    def traverse_inorder(self, root, hasil):
        if root:
            self.traverse_inorder(root.left, hasil)
            hasil.append(root.data)
            self.traverse_inorder(root.right, hasil)
        return hasil

    def traverse_preorder(self, root, hasil):
        if root:
            hasil.append(root.data)
            self.traverse_preorder(root.left, hasil)
            self.traverse_preorder(root.right, hasil)
        return hasil

    def traverse_postorder(self, root, hasil):
        if root:
            self.traverse_postorder(root.left, hasil)
            self.traverse_postorder(root.right, hasil)
            hasil.append(root.data)
        return hasil
    def get_leaves_node(self, root, hasil):
        if root:
            if not root.left and not root.right:
                hasil.append(root.data)
            self.get_leaves_node(root.left, hasil)
            self.get_leaves_node(root.right, hasil)
        return hasil

def insert_manual():
    root = Node("A")
    root.left = Node("B")
    root.right = Node("C")
    root.left.left = Node("D")
    root.left.right = Node("E")
    root.right.right = Node("F")
    return root

gudang = Gudang_tree()
gudang.root = insert_manual()
print("Struktur Audit:")
print("===================================")
print("[Info] Struktur pohon telah dibuat secara manual.")
print("\n 1. Hasil Traversal Inorder:", gudang.traverse_inorder(gudang.root, []))
print(" 2. Hasil Traversal Preorder:", gudang.traverse_preorder(gudang.root, []))
print(" 3. Hasil Traversal Postorder:", gudang.traverse_postorder(gudang.root, []))
print(" 4. Daftar Daun (Leaves) pada Pohon:", gudang.get_leaves_node(gudang.root, []))







