<h1 align="center"><span>Digit Recognizing </span></h1>



[![Python 3.11.6](https://img.shields.io/badge/python-3.11.6-blue.svg)](https://www.python.org/downloads/release/python-3116/)
[![Git 2.39.1](https://img.shields.io/badge/git-2.39.1-red.svg)](https://git-scm.com/docs/git/2.39.0)

Digit recognition with YOLOv8 is an exceptional project designed to leverage the robust YOLOv8 object detection algorithm for recognizing digits in images or videos. Our repository offers an implementation of digit recognition using YOLOv8, comprising training scripts, pre-trained models, and inference tools.Als


# Digit Recognition

## Installation
Download the face detection repository:
``` shell
# Clone repo
git clone https://github.com/Yusuf-ozen/Digit_Recognizer.git
```

Navigate to the project directory:
``` shell
cd Digit_Recognizer
```



Install all necessary library:
``` shell
pip install -r requirements.txt
```




## Testing On Real-Time Webcam
Run this code at git bash or cmd:
``` shell
python yolo_live_test.py
```


## Testing on an Image
Run this code at git bash or cmd and change `/path/image` according your files. Using `--resize_width 400` and `--resize_height 400` the size of output image can change:


``` shell
python yolo_image_test.py /path/image.jpg --resize_width 400 --resize_height 300
```


![Resim Açıklaması](assets/images/num_detected.jpg)


## Testing on a Video
Run this code at git bash or cmd and change `/path/image` according your files. Using `--resize_width 400` and `--resize_height 400` the size of output of the video can change:

``` shell
python yolo_video_test.py /path/video.mp4 --resize_width 1280 --resize_height 720
```




<br>
<div class="gif">
<p align="center">
<img src='assets/videos/git_video.gif' align="center" width=800>
</p>
</div>
</div>



## Results
-This results produced after 50 epochs with yolov8s model and [Digit-Dataset](https://universe.roboflow.com/sambhavs-vision/number-extraction).


| F1 Curve | P Curve | PR Curve |
| :-: | :-: | :-: |
| ![](results/F1_curve.png) | ![](results/P_curve.png) | ![](results/PR_curve.png) |

| Confusion Matrix | R Curve | results |
| :-: | :-: | :-: |
| ![](results/conf_matrix.png) | ![](results/labels.jpg) | ![](results/results.png) |


### Predictions

| label | Prediction | 
| :-: | :-: |
| ![](results/val_batch0_label.jpg) | ![](results/val_batch0_preds.jpg) |


| label | Prediction | 
| :-: | :-: |
| ![](results/val_batch_label1.jpg) | ![](results/val_batch_preds1.jpg) |



## Test Model with Streamlit
-Using Streamlit framework we can show the results of yolov8 model in web application.

### Usage

``` shell
streamlit run yolov8_main.py
```


### Image Testing

![Resim Açıklaması](assets/images/test_img.jpg)


### My model Testing on mnist dataset

| test1 | test2 | 
| :-: | :-: |
| ![](assets/images/my_model_test1.jpg) | ![](assets/images/my_model_test2.jpg) |


## References
https://roboflow.com/

https://github.com/ultralytics/ultralytics
