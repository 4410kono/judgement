from pathlib import Path
import streamlit as st
from ultralytics import YOLO
from utils_int_camera import *
from PIL import Image
import av

# setting page layout
# st.set_page_config(
#     page_title="Interactive Interface for YOLOv8",
#     page_icon="🤖",
#     layout="wide",
#     initial_sidebar_state="expanded"
#     )

st.set_page_config(
    page_title="Fall Detector",
    # page_icon=":abc:",
    # layout="wide",

    initial_sidebar_state="expanded"
)

# Load the image for the title
title_image = Image.open("camera_icon.png")

# Display the title image
st.image(title_image, use_column_width=True)

# sidebar
st.sidebar.header("Model Config")
# model = YOLO('yolov8s.pt')
model = YOLO('best.pt')

# image/video options
st.sidebar.header("Input Config")
source_selectbox = st.sidebar.selectbox(
    "Select Source",
    ["Webcam", "Image", "Video"]
)

# confidence = float(st.sidebar.slider(
#     "Select Model Confidence", 30, 100, 50)) / 100

source_img = None
if source_selectbox == "Video": # Video
    infer_uploaded_video(conf=0.5, model=model)
elif source_selectbox == "Image": # Image
    infer_uploaded_image(conf=0.5, model=model)
elif source_selectbox == "Webcam": # Webcam
    processed_image = create_processed_image()
    res = predict(model,processed_image, conf=0.5)
    judgement(res)
    play_webcam(video_frame_callback(res))
else:
    st.error("Currently only 'Image' and 'Video' source are implemented")
