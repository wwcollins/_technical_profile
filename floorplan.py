import streamlit as st
from PIL import Image
import pytesseract # https://github.com/UB-Mannheim/tesseract/wiki to install app
import cv2
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

class FloorplanApp:
    def __init__(self):
        self.floorplan_image = None
        self.grid_system = None
        self.text_data = None
        self.text_locations = []

    def run(self):
        st.title("Floorplan Analysis App")
        self.upload_image()
        self.create_grid()
        self.extract_text()
        self.visualize_locations()

    def upload_image(self):
        st.header("Upload Floorplan Image")
        self.floorplan_image = st.file_uploader("Choose an image", type=["jpg", "jpeg", "png"])

        if self.floorplan_image is not None:
            self.floorplan_image = Image.open(self.floorplan_image)
            st.image(self.floorplan_image, caption='Uploaded Image', use_column_width=True)

    def create_grid(self):
        if self.floorplan_image is None:
            st.warning("Please upload a floorplan image first.")
            return

        st.header("Create Locational Grid System")
        # Add code to create the grid system for the image

    def extract_text(self):
        if self.floorplan_image is None:
            st.warning("Please upload a floorplan image first.")
            return

        st.header("Extract Text from Image")
        # Convert the floorplan image to grayscale
        gray_image = self.floorplan_image.convert("L")

        # Perform thresholding or other image processing operations as needed
        # ...

        # Use Tesseract OCR to extract text from the image
        self.text_data = pytesseract.image_to_string(gray_image)

        st.write("Text extracted from the image:")
        st.write(self.text_data)

    def visualize_locations(self):
        if self.text_data is None or self.grid_system is None:
            st.warning("Please create a locational grid system and extract text first.")
            return

        st.header("Visualize Text Locations")
        # Add code to process the text data and determine its locations in the grid system

        # Example code to display the floorplan image with text locations marked
        fig, ax = plt.subplots()
        img = mpimg.imread(self.floorplan_image)
        ax.imshow(img)

        # Plot icons at the determined text locations
        for location in self.text_locations:
            ax.plot(location[0], location[1], 'ro')  # Use a red circle as the icon

        ax.axis('off')
        st.pyplot(fig)


# Create and run the app
app = FloorplanApp()
app.run()
