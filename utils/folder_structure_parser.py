import json

def load_folder_structure_from_json(json_file):
    """
    Load folder structure from a JSON file.

    Args:
        json_file (str): Path to the JSON file containing the folder structure.

    Returns:
        dict: The folder structure loaded from the JSON file.

    Raises:
        FileNotFoundError: If the specified JSON file is not found.
        json.JSONDecodeError: If the JSON file is invalid or cannot be decoded.
    """
    try:
        with open(json_file, "r") as f:
            folder_structure = json.load(f)
        return folder_structure
    except FileNotFoundError:
        print(f"Error: JSON file '{json_file}' not found.")
        return None
    except json.JSONDecodeError:
        print(f"Error: Invalid JSON format in file '{json_file}'.")
        return None
