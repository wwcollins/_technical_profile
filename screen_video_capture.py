import streamlit as st
import pyautogui
import cv2 # pip install opencv-python

def main():
    # Set the dimensions of the video capture
    screen_width, screen_height = pyautogui.size()
    video_output = "screen_capture.mp4"

    # Create a video writer object
    fourcc = cv2.VideoWriter_fourcc(*"mp4v")
    video_writer = cv2.VideoWriter(video_output, fourcc, 20.0, (screen_width, screen_height))

    # Start the video capture
    st.title("Screen Video Capture")
    st.text("Press 'Start Capture' to begin recording the screen.")
    if st.button("Start Capture"):
        st.text("Recording started. Press 'Stop Capture' to end recording.")

        # Capture frames until 'Stop Capture' button is pressed
        while True:
            frame = pyautogui.screenshot()
            frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
            video_writer.write(frame)

            if st.button("Stop Capture"):
                st.text("Recording stopped.")
                break

    # Release the video writer and close the Streamlit app
    video_writer.release()

if __name__ == "__main__":
    main()
