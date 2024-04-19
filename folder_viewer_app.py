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
        self.text_area.tag_configure("error", foreground="red")
        
        self.clear_button = tk.Button(root, text="Clear", command=self.clear_files)
        self.clear_button.pack(side=tk.BOTTOM)
        
        self.populate_treeview(self.folder_structure, "")
        
    def populate_treeview(self, items, parent):

        if items is None:
            self.text_area.insert(tk.END, "Error: Folder structure is empty", "error")
            return

        if not isinstance(items, list):
            self.text_area.insert(tk.END, "Error: Invalid Json Format", "error")
            return

        for item in items:
            if not isinstance(item, dict):
                self.tree.delete(*self.tree.get_children())
                self.text_area.insert(tk.END, "Error: Invalid JSON Format", "error")
                return
            elif "name" not in item:
                self.tree.delete(*self.tree.get_children())
                self.text_area.insert(tk.END, "Error: name is required field in JSON Format", "error")
                return

            name = item["name"]
            if "children" in item:
                folder_id = self.tree.insert(parent, "end", text=name, open=True)
                self.populate_treeview(item["children"], folder_id)
            else:
                self.tree.insert(parent, "end", text=name)
    

    def process_selected_files(self, action):
        selected_item_tuple = self.tree.selection()
        for selected_item in selected_item_tuple:
            selected_file = self.tree.item(selected_item, "text")
            if action == "attach":
                if selected_file not in self.selected_files:
                    self.selected_files.append(selected_file)
            elif action == "detach":
                if selected_file in self.selected_files:
                    self.selected_files.remove(selected_file)
        self.update_text_area()
    
    def update_text_area(self):
        self.text_area.delete(1.0, tk.END)
        self.text_area.insert(tk.END, "\n".join(self.selected_files))
    
    def attach_files(self):
        self.process_selected_files("attach")
    
    def detach_files(self):
        self.process_selected_files("detach")
    
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
