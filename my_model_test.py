import streamlit as st
import cv2
from tensorflow.keras.models import load_model
import numpy as np
from PIL import Image

# Model yükleme
my_model = load_model('models/my_model/model.h5', compile=False)

def main():
    st.title('My Model Inference')
    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        # Resmi PIL formatına dönüştürme
        image = Image.open(uploaded_file)

        # Resmi OpenCV formatına dönüştürme (dizi)
        image_np = np.array(image)

        # Resmi gri tonlamalı yapma
        image_gray = cv2.cvtColor(image_np, cv2.COLOR_RGB2GRAY)

        # Resmi modele uygun şekle getirme
        resized_image = cv2.resize(image_gray, (28, 28))
        normalized_image = resized_image / 255.0

        # Tahmin
        pre = my_model.predict(np.expand_dims(normalized_image, axis=0), batch_size=1)
        predicted_class_index = np.argmax(pre)
        prob = np.max(pre)

        # Tahmin edilen sınıf ve olasılığı gösterme
        st.write("Predicted class index:", predicted_class_index)
        st.write("Probability:", prob)

        # Tahmin edilen görüntüyü görselleştirme
        st.image(image_np, caption='Uploaded Image', use_column_width=True)

if __name__ == "__main__":
    main()
