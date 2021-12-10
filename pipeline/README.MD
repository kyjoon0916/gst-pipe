# 파이프라인은 추론 영상또는 영상을 전송하여 웹으로 표식을 한다.

1. 라이브러리 설치

+ Gstreamer 설치 

$ sudo apt install libgstreamer1.0-0 libgstreamer1.0-dev gstreamer1.0-tools gstreamer1.0-doc gstreamer1.0-x gstreamer1.0-plugins-base gstreamer1.0-plugins-good gstreamer1.0-plugins-bad gstreamer1.0-plugins-ugly  gstreamer1.0-alsa gstreamer1.0-libav gstreamer1.0-gl gstreamer1.0-gtk3 gstreamer1.0-qt5 gstreamer1.0-pulseaudio libgstreamer-plugins-base1.0-dev  

-> 지스트리머 설치 

$ sudo apt-get install gir1.2-gst-rtsp-server-1.0 
 
-> rtsp 서버 설치 

+ Detectron2 설치 

Install Pre-Built Detectron2 (Linux only) 

Choose from this table to install v0.6 (Oct 2021): 

python -m pip install detectron2 -f \ 
https://dl.fbaipublicfiles.com/detectron2/wheels/cu111/torch1.8/index.html 

-> torch 1.8 & cuda 11.1 

python -m pip install detectron2 -f \ 
https://dl.fbaipublicfiles.com/detectron2/wheels/cu102/torch1.8/index.html 

-> torch 1.8 & cuda 10.2 

python -m pip install detectron2 -f \ 
https://dl.fbaipublicfiles.com/detectron2/wheels/cu101/torch1.8/index.html 

-> torch 1.8 & cuda 10.1 

python -m pip install detectron2 -f \ 
https://dl.fbaipublicfiles.com/detectron2/wheels/cu111/torch1.9/index.html 

-> torch 1.9 & cuda 11.1 
 
python -m pip install detectron2 -f \ https://dl.fbaipublicfiles.com/detectron2/wheels/cu102/torch1.9/index.html 

-> torch 1.9 & cuda 10.2 

+ Yolov5

pip install requirements.txt
