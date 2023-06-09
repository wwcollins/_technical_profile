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
    def __init__(self, image, rows, cols):
        self.image = image
        self.rows = rows
        self.cols = cols
        self.grid = self.create_grid()

    def create_grid(self):
        height, width = self.image.shape[:2]
        row_height = height // self.rows
        col_width = width // self.cols

        grid = np.zeros((self.rows, self.cols), dtype=int)
        for i in range(self.rows):
            for j in range(self.cols):
                grid[i, j] = i * self.cols + j

        return grid

    def move_object(self, obj, new_position):
        old_position = obj.position
        if old_position != new_position:
            self.grid[old_position[0], old_position[1]] = -1
            self.grid[new_position[0], new_position[1]] = obj.id
            obj.position = new_position

    def render(self):
        # Draw grid lines on the image
        image_with_grid = self.draw_grid()

        # Display the image with grid
        st.image(image_with_grid, channels="BGR")

        # Convert the image with grid to base64 for JavaScript integration
        encoded_image = get_base64_of_array(image_with_grid)
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

    def draw_grid(self):
        image = self.image.copy()
        height, width = image.shape[:2]
        row_height = height // self.rows
        col_width = width // self.cols

        for i in range(1, self.rows):
            cv2.line(image, (0, i * row_height), (width, i * row_height), (255, 0, 0), 1)
        for j in range(1, self.cols):
            cv2.line(image, (j * col_width, 0), (j * col_width, height), (255, 0, 0), 1)

        return image


# Class representing a fire alarm
class FireAlarm:
    def __init__(self, id, position):
        self.id = id
        self.position = position


# Class representing a camera
class Camera:
    def __init__(self, id, position):
        self.id = id
        self.position = position


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
        floorplan = Floorplan(image, rows, cols)

        # Create fire alarm and camera objects
        fire_alarm = FireAlarm(1, (0, 0))
        camera = Camera(2, (0, 1))

        # Get new positions for the objects
        new_fire_alarm_pos = st.selectbox("Select new position for the fire alarm:", floorplan.grid.flatten(),
                                          format_func=lambda val: f"({val // cols}, {val % cols})",
                                          key="fire_alarm_pos")
        new_camera_pos = st.selectbox("Select new position for the camera:", floorplan.grid.flatten(),
                                      format_func=lambda val: f"({val // cols}, {val % cols})", key="camera_pos")

        # Move objects to new positions
        floorplan.move_object(fire_alarm, (new_fire_alarm_pos // cols, new_fire_alarm_pos % cols))
        floorplan.move_object(camera, (new_camera_pos // cols, new_camera_pos % cols))

        # Render the floorplan with objects
        floorplan.render()


if __name__ == "__main__":
    main()
