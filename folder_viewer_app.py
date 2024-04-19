import tkinter as tk
from tkinter import ttk
from utils.folder_structure_parser import load_folder_structure_from_json

class FolderTreeView:
    def __init__(self, root, folder_structure):
        """
        Initialize the GUI application with the provided root and folder structure.

        Args:
            root (tk.Tk): The Tkinter root window.
            folder_structure (dict): The folder structure to display in the GUI.
        """
        self.root = root
        self.folder_structure = folder_structure
        self.selected_files = []
        
        # Create a treeview to display the folder structure
        self.tree = ttk.Treeview(self.root)
        self.tree.pack(fill=tk.BOTH, padx=10, pady=10)

        # Create a frame to contain the buttons
        button_frame = tk.Frame(root)
        button_frame.pack(fill=tk.X, pady=(0, 10))
        
        # Create buttons for attaching and detaching files
        self.attach_button = tk.Button(button_frame, text="Attach", command=self.attach_files)
        self.attach_button.pack(side=tk.LEFT, padx=(10,5))

        self.detach_button = tk.Button(button_frame, text="Detach", command=self.detach_files)
        self.detach_button.pack(side=tk.LEFT, padx=(5,10))
        
        # Create a text area for displaying error messages
        self.text_area = tk.Text(root, height=10)
        self.text_area.pack(fill=tk.BOTH, expand=True, padx=10, pady=(0, 10))
        self.text_area.tag_configure("error", foreground="red")

        # Create the Clear button
        self.clear_button = tk.Button(root, text="Clear", command=self.clear_files)
        self.clear_button.pack(side=tk.BOTTOM)
        
        # Populate the treeview with the provided folder structure
        self.populate_treeview(self.folder_structure, "")
        
    def populate_treeview(self, items, parent):
        """
        Populate the treeview with the provided folder structure items.

        Args:
            items (list): List of folder structure items.
            parent: The parent node in the treeview.
        """

        # Validate JSON Format
        if items is None:
            self.text_area.insert(tk.END, "Error: Folder structure is empty", "error")
            return

        if not isinstance(items, list):
            self.text_area.insert(tk.END, "Error: Invalid Json Format", "error")
            return

        for item in items:
            if not isinstance(item, dict):
                # Clear the treeview before displaying the error message
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
        """
        Process selected files based on the specified action.

        Args:
            action (str): The action to perform (attach or detach).
        """
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
        """
        Update the text area with the list of selected files.
        """
        # Enable text area for updating content
        self.text_area.config(state=tk.NORMAL)
        self.text_area.delete(1.0, tk.END)
        self.text_area.insert(tk.END, "\n".join(self.selected_files))
        # Disable text area to prevent manual editing
        self.text_area.config(state=tk.DISABLED)
    
    def attach_files(self):
        """
        Attach selected files to the list of selected files.
        """
        self.process_selected_files("attach")
    
    def detach_files(self):
        """
        Detach selected files from the list of selected files.
        """
        self.process_selected_files("detach")
    
    def clear_files(self):
        """
        Clear the list of selected files.
        """
        self.selected_files = []
        self.update_text_area()

def main():
    """
    Main function to initialize the application.

    This function creates a Tkinter root window, loads the folder structure
    from a JSON file, and initializes the FolderTreeView with the loaded structure.
    Finally, it starts the Tkinter event loop by calling `mainloop()`.

    """

    # Create a Tkinter root window
    root = tk.Tk()
    root.title("Folder Structure Visualizer")

    # Load folder structure from JSON file
    folder_structure = load_folder_structure_from_json("folder_structure.json")

    # Initialize FolderTreeView with the loaded folder structure
    FolderTreeView(root, folder_structure)

    # Start the Tkinter event loop
    root.mainloop()

if __name__ == "__main__":
    # If this script is run directly, execute the main function
    main()
