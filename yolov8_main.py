from pathlib import Path
import PIL

# External packages
import streamlit as st

# Local Modules
import yolov8_config
import streamlit_yolo

# Setting page layout
st.set_page_config(
    page_title="Digit Number Detection using YOLOv8",
    page_icon=":100:",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Main page heading
st.title("Digit Detection using YOLOv8")


model_path = Path(yolov8_config.DETECTION_MODEL)
# Load Pre-trained ML Model
try:
    model = streamlit_yolo.load_model(model_path)
except Exception as ex:
    st.error(f"Unable to load model. Check the specified path: {model_path}")
    st.error(ex)

st.sidebar.header("Image for test")
source_radio = st.sidebar.radio(
    "Select Source Type", yolov8_config.SOURCES_LIST)

source_img = None
# If image is selected
if source_radio == yolov8_config.IMAGE:
    source_img = st.sidebar.file_uploader(
        "Choose an image...", type=("jpg", "jpeg", "png"))

    col1, col2 = st.columns(2)

    with col1:
        try:
            if source_img is None:
                default_image_path = str(yolov8_config.DEFAULT_IMAGE)
                default_image = PIL.Image.open(default_image_path)
                st.image(default_image_path, caption="Default Image",
                          use_column_width=True)
            else:
                uploaded_image = PIL.Image.open(source_img)
                st.image(source_img, caption="Uploaded Image",
                          use_column_width=True)
        except Exception as ex:
            st.error("Error occurred while opening the image.")
            st.error(ex)

    with col2:
        if source_img is None:
            default_detected_image_path = str(yolov8_config.DEFAULT_DETECT_IMAGE)
            default_detected_image = PIL.Image.open(
                default_detected_image_path)
            st.image(default_detected_image_path, caption='Detected Image',
                      use_column_width=True)
        else:
            if st.sidebar.button('Detect number'):
                res = model.predict(uploaded_image)
                boxes = res[0].boxes
                res_plotted = res[0].plot()[:, :, ::-1]
                st.image(res_plotted, caption='Detected Image',
                          use_column_width=True)

                


elif source_radio == yolov8_config.WEBCAM:
    streamlit_yolo.play_webcam(model)



elif source_radio == yolov8_config.YOUTUBE:
    streamlit_yolo.play_youtube_video(model)

else:
    st.error("Please select a valid source type!")