import streamlit as st

try:
    from docx import Document
except Exception as e:
    st.caption(f'error: {e}')

from markdownify import markdownify as md


def convert_docx_to_md(file_path):
    doc = Document(file_path)
    paragraphs = [p.text for p in doc.paragraphs]
    md_content = md('\n'.join(paragraphs))
    return md_content


import pypandoc

def convert_docx_to_text(file_path):
    docxFilename = file_path
    output = pypandoc.convert_file(docxFilename, 'plain', outputfile="somefile.txt")
    assert output == ""
    return output


def main():
    st.title("DOCX to Markdown Converter")
    uploaded_file = st.file_uploader("Upload a DOCX file", type="docx")

    if uploaded_file is not None:
        st.caption("Converting...")

        # Save the uploaded file to a temporary location
        with open("temp.docx", "wb") as f:
            f.write(uploaded_file.getbuffer())

        # Convert the file to Markdown
        markdown_content = convert_docx_to_md("temp.docx")
        # markdown_content = convert_docx_to_text()

        # Display the converted Markdown
        st.subheader("Converted Markdown:")
        st.text_area("", value=markdown_content, height=400)



        # Clean up the temporary file
        # os.remove("temp.docx")


if __name__ == "__main__":
    main()
