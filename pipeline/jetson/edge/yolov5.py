# -*- coding: utf-8 -*-

import torch
import cv2
import numpy as np
#from yolov5.utils.torch_utils import model_info

# User Input
threshold = 0.5

# setting device on GPU if available, else CPU
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
print('Using device:', device)
print()

#Additional Info when using cuda
if device.type == 'cuda':
    print(torch.cuda.get_device_name(0))

# Model
model = torch.hub.load('../../yolov5', 'custom', path='../../model/weights/yolov5s.pt', source='local')  # local repo

#model = torch.load('/home/joon/code/yolo_simple/yolov5s.pt')

def inference(frame):   
    
    # Inference
    results = model(frame)
    img = np.array(results.imgs)[0]
    names = results.names
    
    # Adding Box
    # xyxy의 결과값은 startx, starty, endx, endy, confidenc, class
    boxes = results.xyxy[0].cpu().numpy() 
    # print(boxes.shape)
    
    for box in boxes:
        if box[4]> threshold :
            cv2.rectangle(img, (int(box[0]), int(box[1])), (int(box[2]),int(box[3])), (0, 0, 255), 2)                  
            title = names[int(box[5])]
            prob = round(box[4] * 100,1)
            img = cv2.putText(img, title + ' ' + str(prob) + '%', (int(box[0]), int(box[1])-10), 
                              cv2.FONT_HERSHEY_SIMPLEX, 0.5, (36,255,12), 1)
        
    return img

def main():
    cap = cv2.VideoCapture(1)
    if cap.isOpened():
        while True:
            ret_val, frame = cap.read()
            # print(inference(frame).shape)
            # print(type(inference(frame)))
            cv2.imshow("",inference(frame))
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
    else:
        print("Closed")
    cap.release()
    # cv2.detroyALLwindows()

if __name__== '__main__':
    main()
    
