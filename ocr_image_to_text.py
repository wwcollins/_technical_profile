import streamlit as st
from PIL import Image
import pytesseract
import os

# Specifies PATH of Tesseract
pytesseract.pytesseract.tesseract_cmd = r'C:/Program Files/Tesseract-OCR/tesseract.exe'

def main():
    st.title("Text Extraction from Image")
    uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

    st.sidebar.write("Teseract Setttings...")
    oem = st.sidebar.slider(f'oem', value= 3, min_value=0,max_value=10, key='oem')
    psm = st.sidebar.slider(f'psm', value=6, min_value=0, max_value=13, key='psm')

    with st.sidebar.expander(f'about psm modes 0-13...'):
        info_msg = """
    Page segmentation modes:
  0    Orientation and script detection (OSD) only.
  1    Automatic page segmentation with OSD.
  2    Automatic page segmentation, but no OSD, or OCR.
  3    Fully automatic page segmentation, but no OSD. (Default)
  4    Assume a single column of text of variable sizes.
  5    Assume a single uniform block of vertically aligned text.
  6    Assume a single uniform block of text.
  7    Treat the image as a single text line.
  8    Treat the image as a single word.
  9    Treat the image as a single word in a circle.
 10    Treat the image as a single character.
 11    Sparse text. Find as much text as possible in no particular order.
 12    Sparse text with OSD.
 13    Raw line. Treat the image as a single text line,
                        bypassing hacks that are Tesseract-specific.
                        """
        st.sidebar.caption(f'{info_msg}')


    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        # image = image.resize((300, 150))

        col1, col2 = st.columns(2)
        with col1:
            st.caption("Image:")
            st.image(image)
        # custom_config = r'-l eng --oem 3 --psm 6'

        custom_config = f"r'-l eng --oem {oem} --psm {psm}'"
        st.caption (f':blue[{custom_config}]')

        text = pytesseract.image_to_string(image, config=custom_config)
        with col2:
            st.caption("Extracted Text:")
            st.write(text)

        # Save the text to a text file
        filename = "demo.txt"
        with open(filename, "w") as f:
            f.write(text)
        st.success(f"Text saved to {filename}.")

if __name__ == "__main__":
    main()
