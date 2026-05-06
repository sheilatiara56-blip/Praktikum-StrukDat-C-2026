class Node:
    def __init__(self, id_buku, judul_buku):
        self.id_buku = id_buku
        self.judul_buku = judul_buku # Gunakan nama ini secara konsisten
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, id_buku, judul_buku):
        if self.root is None: 
            self.root = Node(id_buku, judul_buku)
            print(f"[Info] Buku berhasil dimasukkan : ID {id_buku}") 
        else:
             self._insert_recursive(self.root, id_buku, judul_buku)

    def _insert_recursive(self, node, id_buku, judul_buku):
        if id_buku < node.id_buku:
            if node.left is None:
                node.left = Node(id_buku, judul_buku)
                print(f"[Info] Buku berhasil dimasukkan : ID {id_buku}")
            else:
                self._insert_recursive(node.left, id_buku, judul_buku)
        elif id_buku > node.id_buku:
            if node.right is None:
                node.right = Node(id_buku, judul_buku)
                print(f"[Info] Buku berhasil dimasukkan : ID {id_buku}")
            else:
                self._insert_recursive(node.right, id_buku, judul_buku)

    def search(self, id_buku): 
        
        return self._search_recursive(self.root, id_buku)

    
    def _search_recursive(self, current, id_buku):
        if current is None:
             return None
        if id_buku == current.id_buku:
            return current
        if id_buku < current.id_buku:
            return self._search_recursive(current.left, id_buku)
        return self._search_recursive(current.right, id_buku)

    def traversal_inorder(self):
        self._count = 1
        self._inorder_recursive(self.root)

    
    def _inorder_recursive(self, current):
        if current:
            self._inorder_recursive(current.left)
            # Pastikan panggil .judul_buku bukan .judul
            print(f"{self._count}. {current.id_buku} - {current.judul_buku}") 
            self._count += 1
            self._inorder_recursive(current.right)

    def get_min(self):
        if self.root is None:
            return None
        current = self.root
        while current.left:
            current = current.left
        return current.id_buku

    def get_max(self):
        if self.root is None:
            return None
        current = self.root
        while current.right:
            current = current.right
        return current.id_buku

    def height(self):
        return self._height_recursive(self.root)

    def _height_recursive(self, current):
        if current is None:
            return -1 
        return 1 + max(self._height_recursive(current.left), self._height_recursive(current.right))


print("SISTEM KATALOG PERPUSTAKAAN ILMU TERANG")
print("======================================= ")

katalog = BinarySearchTree()
data_buku = [
    (50, "Dasar Pemrograman"),
    (30, "Struktur Data"),
    (70, "Kecerdasan Buatan"),
    (20, "Matematika Diskrit"),
    (40, "Basis Data"),
    (60, "Jaringan Komputer"),
    (80, "Sistem Operasi")
]

for id_b, judul_b in data_buku:
    katalog.insert(id_b, judul_b)

print("\n[info] Katalog buku:")
katalog.traversal_inorder()

def cari_dan_tampilkan(id_target):
    print(f"\n[Search] Mencari ID {id_target}...")
    hasil = katalog.search(id_target)
    if hasil:
        # Pastikan panggil .judul_buku
        print(f"Ditemukan! Judul: {hasil.judul_buku}") 
    else:
        print("Data tidak ditemukan.")

cari_dan_tampilkan(60)
cari_dan_tampilkan(100)

print(f"\n[Statistik] ID Terkecil: {katalog.get_min()}")
print(f"[Statistik] ID Terbesar: {katalog.get_max()}")
print(f"[Info] Tinggi (Height) Tree: {katalog.height()}")

