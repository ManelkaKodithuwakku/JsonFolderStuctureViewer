# Folder Structure Visualizer

This Python application allows users to visualize a folder structure in a tree view format using JSON input. Users can select one or more files from the tree view and attach them to a text area at the bottom of the screen. The application provides functionality for both attaching and detaching selected files.

## Getting Started

1. **Clone the project:**

   ```bash
   git clone https://github.com/ManelkaKodithuwakku/JsonFolderStuctureViewer.git
   ```

2. Navigate to the project directory:

   ```bash
   cd JsonFolderStuctureViewer
   ```

3. Install the required Python libraries:

   ```bash
   pip install -r requirements.txt
   ```

4. Before running the application, ensure that you have tkinter installed. You can install it using the following command:

   ```bash
   sudo apt-get install python3-tk
   ```

## Running the Application

```bash
python3 main.py
```

## Usage

1. JSON file representing the folder structure.
2. The folder structure will be displayed in a tree view format.
3. Select one or more files from the tree view by clicking on them.
4. Click the "Attach" button to list the names of the selected files in the text area at the bottom.
5. To remove selected attached files in the tree view, click the "Detach" button.
6. To remove all attached files in the text area, click the "Clear" button next to the text area.

## JSON File Sample

```json
[
    {
      "name": "Folder 1",
      "children": [
        {
          "name": "Subfolder 1",
          "children": [
            { "name": "File 1.txt" },
            { "name": "File 2.txt" }
          ]
        },
        { "name": "File 3.txt" }
      ]
    },
    {
      "name":"File 6.txt"
    },
    {
      "name": "Folder 2",
      "children": [
        { "name": "File 4.txt" },
        { "name": "File 5.txt" }
      ]
    },
    {
      "name":"Folder 3",
      "children":[]
    }
]
```