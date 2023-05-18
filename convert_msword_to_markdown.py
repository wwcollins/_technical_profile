import streamlit as st

try:
    from docx import Document
except Exception as e:
    st.caption(f'error: {e}')

from markdownify import markdownify as md


def convert_docx_to_md(file_path):
    doc = Document(file_path)
    paragraphs = [p.text for p in doc.paragraphs]
    md_content = md('\n\n'.join(paragraphs))
    return md_content


import pypandoc

def convert_docx_to_text(file_path):
    docxFilename = file_path
    output = pypandoc.convert_file(docxFilename, 'plain', outputfile="somefile.txt")
    assert output == ""
    return output

def write_content_to_file(filepath, filename, content):
    # Concatenate the filepath and filename
    full_path = filepath + '/' + filename

    try:
        # Open the file in write mode
        with open(full_path, 'w') as file:
            # Write the content to the file
            file.write(content)
        print(f"Content successfully written to {full_path}")
    except IOError:
        print(f"An error occurred while writing to {full_path}")


def main():
    st.title("DOCX to Markdown Converter")
    uploaded_file = st.file_uploader("Upload a DOCX file", type="docx")

    if uploaded_file is not None:
        st.write(f"Converting file to markdown: \n{uploaded_file.name}")
        st.caption(f'file: {uploaded_file.name} size: {uploaded_file.size} type: {uploaded_file.type}')

        file_out = f'{uploaded_file.name.split(".")[0]}.md'
        st.caption(f'{file_out}')

        # Save the uploaded file to a temporary location
        with open(file_out, "wb") as f:
            f.write(uploaded_file.getbuffer())

        # Convert the file to Markdown
        markdown_content = convert_docx_to_md(file_out)
        # markdown_content = convert_docx_to_text()

        # Display the converted Markdown
        st.subheader("Converted Markdown:")
        st.caption(F':blue[Note: you can edit this content before saving...]')
        markdown_input = st.text_area(file_out, value=markdown_content, height=400)

        if markdown_input:
            # st.write("You entered: ", markdown_input)
            result = st.button('Save', markdown_input, 'text/csv')  # this does not allow for custom folder
            if result:
                # add code to handle file save ourselves since streamlit does not support
                filepath = "./content/"
                write_content_to_file(filepath, file_out, markdown_input)
                st.caption (f'file {file_out} written to {filepath}')


if __name__ == "__main__":
    main()
