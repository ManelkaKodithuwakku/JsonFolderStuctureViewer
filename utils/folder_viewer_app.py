import tkinter as tk
from tkinter import ttk
from utils.folder_structure_parser import load_folder_structure_from_json

class FolderTreeView:
    def __init__(self, root, folder_structure):
        self.root = root
        self.folder_structure = folder_structure
        self.selected_files = []
        
        self.tree = ttk.Treeview(self.root)
        self.tree.pack(fill=tk.BOTH, padx=10, pady=10)
        
        self.attach_button = tk.Button(root, text="Attach", command=self.attach_files)
        self.attach_button.pack()

        self.detached_button = tk.Button(root, text="Detach", command=self.detach_files)
        self.detached_button.pack()
        
        self.text_area = tk.Text(root, height=10)
        self.text_area.pack(padx=10, pady=10)
        
        self.clear_button = tk.Button(root, text="Clear", command=self.clear_files)
        self.clear_button.pack(side=tk.BOTTOM)
        
        self.populate_treeview(self.folder_structure, "")
        
    def populate_treeview(self, items, parent):
        for item in items:
            name = item["name"]
            if "children" in item:
                folder_id = self.tree.insert(parent, "end", text=name, open=True)
                self.populate_treeview(item["children"], folder_id)
            else:
                self.tree.insert(parent, "end", text=name)
    
    def detach_files(self):
        selected_item_tuple = self.tree.selection()
        for selected_item in selected_item_tuple:
            selected_file = self.tree.item(selected_item, "text")
            if selected_file in self.selected_files:
                self.selected_files.remove(selected_file)
        self.update_text_area()
    
    def update_text_area(self):
        self.text_area.delete(1.0, tk.END)
        self.text_area.insert(tk.END, "\n".join(self.selected_files))
    
    def attach_files(self):
        selected_item_tuple = self.tree.selection()
        for selected_item in selected_item_tuple:
            selected_file = self.tree.item(selected_item, "text")
            if selected_file not in self.selected_files:
                self.selected_files.append(selected_file)
        self.update_text_area()
    
    def clear_files(self):
        self.selected_files = []
        self.update_text_area()

def main():
    root = tk.Tk()
    root.title("Folder Structure Visualizer")

    folder_structure = load_folder_structure_from_json("folder_structure.json")
    FolderTreeView(root, folder_structure)

    root.mainloop()

if __name__ == "__main__":
    main()
