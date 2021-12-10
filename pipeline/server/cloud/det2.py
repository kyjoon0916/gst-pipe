from detectron2.utils.logger import setup_logger
setup_logger()
import sys
import os
import cv2
from detectron2.engine import DefaultPredictor
from detectron2.config import get_cfg
from detectron2.utils.visualizer import Visualizer
from detectron2.data import MetadataCatalog
from pipeline.model.vovnet import add_vovnet_config
sys.path.insert(1, '/home/joon/code/gitpipeline/pipeline/')

## 설정 ##
config_file_path = "../../model/configs/faster_rcnn_V_19_FPNLite_3x.yaml"
weights_path = "../../model/weights/FRCN-V2-19-slim-FPNLite-3x/model_final.pth"
### 이미지
# image_path = "/home/joon/code/yolov5/test.jpg"
model = config_file_path
####이미지 사용
# im = cv2.imread(image_path)
cfg = get_cfg()
add_vovnet_config(cfg)
cfg.merge_from_file(config_file_path)
cfg.MODEL.WEIGHTS = weights_path
cfg.MODEL.ROI_HEADS.SCORE_THRESH_TEST = 0.8

cfg.DATASETS.TRAIN = ("aihub_train")
classes = ['black smoke', 'gray smoke', ' white smoke', 'fire']
MetadataCatalog.get("aihub_train").set(thing_classes = classes)
aihub_metadata = MetadataCatalog.get("aihub_train")
metadata = aihub_metadata


# thing_classes_path = '../../model/safety_classes.txt'
# with open(thing_classes_path) as f:
#     lines = f.readlines()
#     lines = [line.rstrip() for line in lines]
# thing_classes = lines[:7]
# MetadataCatalog.get(cfg.DATASETS.TRAIN[0]).thing_classes = thing_classes
# cfg.MODEL.ROI_HEADS.NUM_CLASSES = len(thing_classes) 

def detect(frame):
    ## 디택팅 ##
    frame = cv2.resize(frame, dsize=(640, 480), interpolation=cv2.INTER_AREA)
    predictor = DefaultPredictor(cfg)
    outputs = predictor(frame)

    v = Visualizer(frame[:, :, ::-1], MetadataCatalog.get(cfg.DATASETS.TRAIN[0]), scale=1)
    v = v.draw_instance_predictions(outputs["instances"].to("cpu"))
    vis_frame = v.get_image()[:, :, ::-1]
    # vis_frame = cv2.cvtColor(v.get_image()[:, :, ::-1],cv2.COLOR_RGB2BGR)
    return vis_frame

def main():
    cap = cv2.VideoCapture(2)
    if cap.isOpened():
        while True:
            ret_val, frame = cap.read()
            cv2.imshow("",detect(frame))
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
    else:
        print("Closed")
    cap.release()
    # cv2.detroyALLwindows()

if __name__== '__main__':
    main()


