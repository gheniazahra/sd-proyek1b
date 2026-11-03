class TreeNode:
    def __init__(self, node_id, nama, jabatan):
        self.node_id = node_id
        self.nama = nama
        self.jabatan = jabatan
        self.children = []

    def add_child(self, child_node):
        self.children.append(child_node)

class OrganisasiTree:
    def __init__(self, root_node):
        self.root = root_node

    def insert_node(self, parent_jabatan, new_node):
        parent = self.search_node(self.root, parent_jabatan)
        if parent:
            parent.add_child(new_node)
            print(f"Berhasil menambahkan '{new_node.jabatan}' di bawah '{parent.jabatan}'")
        else:
            print(f"Gagal: Atasan dengan jabatan '{parent_jabatan}' tidak ditemukan.")

    def search_node(self, current_node, keyword):
        if current_node is None:
            return None
        
        # Pencarian berdasarkan Nama atau Jabatan
        if (current_node.nama.lower() == keyword.lower() or 
            current_node.jabatan.lower() == keyword.lower()):
            return current_node
        
        for child in current_node.children:
            found = self.search_node(child, keyword)
            if found:
                return found
        return None

    def preorder_traversal(self, node):
        if node is None:
            return
        print(f"[{node.node_id}] {node.jabatan} - {node.nama}")
        for child in node.children:
            self.preorder_traversal(child)

    def inorder_traversal(self, node):
        if node is None:
            return
        # Logika In-Order untuk General Tree: Anak pertama -> Induk -> Anak sisanya
        if not node.children:
            print(f"[{node.node_id}] {node.jabatan} - {node.nama}")
        else:
            self.inorder_traversal(node.children[0])
            print(f"[{node.node_id}] {node.jabatan} - {node.nama}")
            for i in range(1, len(node.children)):
                self.inorder_traversal(node.children[i])

    def postorder_traversal(self, node):
        if node is None:
            return
        for child in node.children:
            self.postorder_traversal(child)
        print(f"[{node.node_id}] {node.jabatan} - {node.nama}")

# --- CONTOH PENGGUNAAN (MAIN PROGRAM) ---
if __name__ == "__main__":
    # 1. Inisialisasi Root (Rektor)
    rektor = TreeNode("01", "Prof. Dr. Ahmad", "Rektor")
    tree = OrganisasiTree(rektor)

    # 2. Sisipkan Data (insert_node)
    tree.insert_node("Rektor", TreeNode("02", "Dr. Budi", "Senat Universitas"))
    tree.insert_node("Rektor", TreeNode("03", "Dr. Citra", "Wakil Rektor I"))
    tree.insert_node("Rektor", TreeNode("04", "Prof. Dina", "Dekan Fakultas Sains dan Teknologi"))
    tree.insert_node("Dekan Fakultas Sains dan Teknologi", TreeNode("05", "Dr. Eka", "Ketua Program Studi Teknik Informatika"))

    # 3. Pencarian Data (search_node)
    print("\n--- Hasil Pencarian ---")
    hasil = tree.search_node(tree.root, "Ketua Program Studi Teknik Informatika")
    if hasil:
        print(f"Ditemukan: {hasil.nama} menjabat sebagai {hasil.jabatan}")

    # 4. Traversal
    print("\n--- Pre-Order Traversal ---")
    tree.preorder_traversal(tree.root)

    print("\n--- In-Order Traversal ---")
    tree.inorder_traversal(tree.root)

    print("\n--- Post-Order Traversal ---")
    tree.postorder_traversal(tree.root)