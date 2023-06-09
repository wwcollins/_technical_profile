import streamlit as st
import cv2
import numpy as np
import base64

# Function to encode the image as base64
def get_base64_of_array(arr):
    _, im_arr = cv2.imencode('.png', arr)
    im_bytes = im_arr.tobytes()
    im_b64 = base64.b64encode(im_bytes).decode("utf-8")
    return im_b64

# Class representing the floorplan
class Floorplan:
    def __init__(self, image):
        self.image = image
        self.objects = []

    def add_object(self, obj):
        self.objects.append(obj)

    def draw(self):
        image_with_objects = self.image.copy()
        for obj in self.objects:
            image_with_objects = obj.draw(image_with_objects)
        return image_with_objects

# Class representing a fire alarm object
class FireAlarm:
    def __init__(self, row, col):
        self.row = row
        self.col = col

    def draw(self, image):
        height, width = image.shape[:2]
        row_height = height // rows
        col_width = width // cols
        radius = min(row_height, col_width) // 4
        center_x = self.col * col_width + col_width // 2
        center_y = self.row * row_height + row_height // 2

        cv2.circle(image, (center_x, center_y), radius, (0, 0, 255), -1)

        return image

# Class representing a camera object
class Camera:
    def __init__(self, row, col):
        self.row = row
        self.col = col

    def draw(self, image):
        height, width = image.shape[:2]
        row_height = height // rows
        col_width = width // cols
        side_length = min(row_height, col_width) // 2
        center_x = self.col * col_width + col_width // 2
        center_y = self.row * row_height + row_height // 2

        cv2.rectangle(
            image,
            (center_x - side_length, center_y - side_length),
            (center_x + side_length, center_y + side_length),
            (0, 255, 0),
            -1,
        )

        return image

# Streamlit app
def main():
    st.title("Floorplan Grid Overlay")
    uploaded_file = st.file_uploader("Upload a floorplan image", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        # Read the uploaded image
        file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
        image = cv2.imdecode(file_bytes, 1)

        # Get grid parameters from the user
        rows = st.number_input("Number of rows:", min_value=1, value=5)
        cols = st.number_input("Number of columns:", min_value=1, value=5)

        # Create a floorplan object
        floorplan = Floorplan(image)

        # Get object coordinates from the user
        obj_row = st.number_input("Object Row:", min_value=0, max_value=rows - 1, value=0)
        obj_col = st.number_input("Object Column:", min_value=0, max_value=cols - 1, value=0)

        # Add fire alarm and camera objects to the floorplan
        if st.button("Add Fire Alarm"):
            fire_alarm = FireAlarm(obj_row, obj_col)
            floorplan.add_object(fire_alarm)
        if st.button("Add Camera"):
            camera = Camera(obj_row, obj_col)
            floorplan.add_object(camera)

        # Draw the floorplan with objects
        image_with_objects = floorplan.draw()

        # Display the image with objects and grid
        st.image(image_with_objects, channels="BGR")

        # Convert the image with objects to base64 for JavaScript integration
        encoded_image = get_base64_of_array(image_with_objects)
        js_code = f"""
            <script>
            const img = new Image();
            img.src = 'data:image/png;base64,{encoded_image}';
            img.onload = function () {{
                const canvas = document.getElementById("grid-canvas");
                const ctx = canvas.getContext("2d");
                ctx.drawImage(img, 0, 0);
            }};
            </script>
        """
        st.markdown(js_code, unsafe_allow_html=True)

        # Display the grid coordinate system
        st.markdown('<canvas id="grid-canvas"></canvas>', unsafe_allow_html=True)

if __name__ == "__main__":
    main()
