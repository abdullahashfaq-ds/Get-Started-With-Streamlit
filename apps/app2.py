"""
Uploading, displaying, and saving images.
Displaying audio, and video files.
"""
from PIL import Image
import streamlit as st


# displaying title
st.title("Handling Media Files")

# handling images
file = st.file_uploader("Upload Image", type=["jpg", "jpeg", "png"])

if file:
    st.image(file, caption='Uploaded Image', use_column_width=True)
    if st.button("Save"):
        path = f"../media/{file.name}"
        with open(path, "wb") as f:
            f.write(file.getbuffer())
            st.success("Image saved successfully.")

# handling audios
audio_file = open("../media/audio.mp3", "rb")
audio_bytes = audio_file.read()

st.audio(audio_bytes, format='audio/mp3')

# handling videos
video_file = open('../media/video.mp4', 'rb')
video_bytes = video_file.read()

st.video(video_bytes)
