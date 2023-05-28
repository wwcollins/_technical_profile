
import streamlit as st
from docx2pdf import convert

def convert_to_pdf(input_file, output_file):
    # Convert the Word document to PDF
    convert(input_file.name, output_file.name)

def main():
    st.title("Word to PDF Converter")

    # File upload
    st.header("Upload Word Document")
    input_file = st.file_uploader("Choose a Word document", type=["docx"])

    if input_file:
        # Convert button
        if st.button("Convert to PDF"):
            output_file = f"{input_file.name.split('.')[0]}.pdf"
            with st.spinner("Converting..."):
                with open(output_file, "wb") as out_file:
                    convert_to_pdf(input_file, out_file)
                st.success("Conversion complete!")

            # Download link for the converted PDF file
            st.markdown(f"Download [converted PDF file]({output_file})")

if __name__ == "__main__":
    main()
