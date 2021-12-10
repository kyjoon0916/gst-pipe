1. EDGE PIPELINE

CAM -> JETSON -> CLOUD -> WEB
+ frame     detectd    webrtc
             frame


2. CLOUD PIPELINE

CAM -> JETSON -> CLOUD -> WEB
+ frame     frame  detected webrtc

3. 설치 환경

+ jetson -> Gstreamer, Cuda, pytorch

+ server -> Gstreamer, Cuda, pytorch, aiortc

