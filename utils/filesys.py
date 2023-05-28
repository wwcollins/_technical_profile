import os
import glob

def get_newest_file(directory, doc_type=""):
    """
    Get newest file in a target path by doctype or newest file overall.

    Parameters:
    - **directory** (str): File path including file
    - **doc_type** (str):  document type e.g. docx, pdf, xls, etc

    Returns:
    - **newest_file**: The name of the newest file in the directory, including by doctype
    """
    if doc_type:
        files = glob.glob(os.path.join(directory, f"*.{doc_type}"))
    else:
        files = glob.glob(os.path.join(directory, "*"))
    if not files:
        return None
    newest_file = max(files, key=os.path.getctime)
    return newest_file

"""
# Example usage
directory_path = '/path/to/directory'
document_type = ""  # Set document type as empty to find the newest file among all file types
newest_file = get_newest_file(directory_path, document_type)
if newest_file:
    print("Newest file:", newest_file)
else:
    print("No files found in the directory.")
"""
