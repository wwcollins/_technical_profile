import streamlit as st
import pandas as pd
import json

USER_DEFAULT_BOOKMARKS_PATH = r'C:\Users\willi\AppData\Local\Google\Chrome\User Data\Default\Bookmarks'


# TODO Allow user to add their custom path

# Function to recursively iterate through bookmark folders
def iterate_bookmarks(bookmarks, folder_name="", parent_folder=""):
    entries = []
    for item in bookmarks:
        if item["type"] == "folder":
            current_folder = f"{parent_folder}/{item['name']}" if parent_folder else item['name']
            entries.extend(iterate_bookmarks(item["children"], folder_name, current_folder))
        elif item["type"] == "bookmark":
            if folder_name == parent_folder:
                entries.append(item)
    return entries

# Function to search for keywords in bookmarks
def search_bookmarks(bookmarks, keyword):
    matching_entries = []
    for item in bookmarks:
        if item["type"] == "folder":
            matching_entries.extend(search_bookmarks(item["children"], keyword))
        elif item["type"] == "bookmark":
            if keyword in item["name"] or keyword in item["url"]:
                matching_entries.append(item)
    return matching_entries

# Load bookmark data from a JSON file
def load_bookmarks(file_path):
    with open(file_path, "r") as file:
        bookmarks = json.load(file)
    return bookmarks["roots"]["bookmark_bar"]["children"]

# Generate bookmark JSON file for the user
def generate_bookmark_file(file_path, bookmark_data):
    with open(file_path, "w") as file:
        json.dump(bookmark_data, file)

# Main function

def main():
    st.title("Bookmark Viewer")

    bookmark_file_path = st.text_input("Enter the path to your bookmark JSON file:", value=USER_DEFAULT_BOOKMARKS_PATH)

    if bookmark_file_path:
        bookmark_file_path = USER_DEFAULT_BOOKMARKS_PATH

    bookmarks = load_bookmarks(bookmark_file_path)

    if bookmarks:

        # List all bookmark folders
        folder_names = [item["name"] for item in bookmarks if item["type"] == "folder"]

        for each in bookmarks:
            st.write(f'{each["name"]}')

        st.write(f'folder_names={folder_names}')

        st.write(bookmarks)

        selected_folder = st.selectbox("Select a bookmark folder:", [""] + folder_names)

        if selected_folder:
            # Iterate and list all entries in the selected folder
            folder_entries = iterate_bookmarks(bookmarks, selected_folder)
            df = pd.DataFrame(folder_entries, columns=["name", "url"])
            st.dataframe(df)

            # Search for keywords across all bookmark folders
            keyword = st.text_input("Enter a keyword to search:")
            if keyword:
                matching_entries = search_bookmarks(bookmarks, keyword)
                if matching_entries:
                    df = pd.DataFrame(matching_entries, columns=["name", "url"])
                    st.subheader("Matching Entries")
                    st.dataframe(df)
                else:
                    st.info("No matching entries found.")

        # Option to generate bookmark JSON file
        generate_file = st.button("Generate Bookmark File")
        if generate_file:
            bookmark_data = {"roots": {"bookmark_bar": {"children": bookmarks}}}
            generated_file_path = st.text_input("Enter the path to save the generated bookmark JSON file:")
            generate_bookmark_file(generated_file_path, bookmark_data)
            st.success("Bookmark JSON file generated successfully.")

    else:
        st.warning("Invalid bookmark file path.")


# Run the application
if __name__ == "__main__":
    main()
