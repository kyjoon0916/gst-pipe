import os
from tqdm.notebook import tqdm
import pandas as pd
import json 

from detectron2.structures import BoxMode

def get_image_file_names(IMAGE_DIR):
    # function
    file_names = os.listdir(IMAGE_DIR)
    image_file_names = []
    for file_name in tqdm(file_names):
        if file_name[-1] == 'g':
            image_file_names.append(file_name)
        else:
            pass    
    return image_file_names

def get_json_file_names(LABEL_DIR):
    file_names = os.listdir(LABEL_DIR)
    json_file_names = []
    for file_name in tqdm(file_names):
        if file_name[-1] == 'n':
            json_file_names.append(file_name)
        else:
            pass    
    return json_file_names

def open_txt(path):
    with open(path) as f:
        lines = f.readlines()
        lines = [line.rstrip() for line in lines]
    return lines

def convert_to_df(target_json_file_names, target_json_dir, target_image_dir, existing_image_names):
    df = pd.DataFrame()
    ids =[]
    widths = []
    heights = []
    bboxes_str = []
    for i in tqdm(range(len(target_json_file_names))):
        json_file_path = os.path.join(target_json_dir, target_json_file_names[i])

        with open(json_file_path, encoding='utf-8-sig') as f:
            json_data = json.load(f)
        
        # check file xist
        if json_data['images'][0]['file_name'] in existing_image_names:
            
            image_annos = json_data['annotations']

            bboxes = []
            class_ids = []
            # print(image_annos)
            for idx, anno in enumerate(image_annos):
                
                # print(anno)
                dict_keys = anno.keys()
                class_id = int(anno['category_id']) - 1
                
                if list(dict_keys)[0] == 'polygon':
                    pass
                    
                else:
                    bbox = anno['bbox']
                    bboxes.append(bbox)
                    class_ids.append(class_id)
            
            # create string 
            bbox_str = ""
            for b, c in zip(bboxes, class_ids):
                bbox_str += "{} {} {} {} {} ".format(c, b[0], b[1], b[2]+b[0], b[3]+b[1])

            # add
            id = json_data['images'][0]['file_name']
            # resolution = json_data['image']['resolution']
            
            ids.append(id)
            widths.append(json_data['images'][0]['width'])
            heights.append(json_data['images'][0]['height'])
            bboxes_str.append(bbox_str)
        else: 
            print("No image")
            continue
        
    df['id'] = ids    
    df['width'] = widths
    df['height'] = heights
    df['bbox'] = bboxes_str
    df['image_dir'] = target_image_dir
    
    return df

def get_dicts(df):
    print("Creating data...")
    dataset_dicts = []
    for i in tqdm(range(1,len(df))):
        image_dir = df.iloc[i]["image_dir"]
        image_name = df.iloc[i]["id"]
    
        try:
            image_path = '{}/{}'.format(image_dir, image_name)
            
            height = df.iloc[i]["height"]
            width = df.iloc[i]["width"]
            
            record = {}
            
            record["file_name"] = image_path
            record["height"] = height
            record["width"] = width
            record["image_id"] = image_name
            
            objs = []
            
            arr_bbox = df.loc[i, 'bbox'][:-1]
            arr = arr_bbox.split(' ')
            nums = len(arr) // 5
            # assert nums >0
            for i in range(nums):
                class_id_raw = int(arr[5*i])
                class_id = class_id_raw       
                
                x1 = float(arr[5*i+1])
                x2 = float(arr[5*i+2])
                x3 = float(arr[5*i+3])
                x4 = float(arr[5*i+4])
                bbox = [
                    x1, x2, x3, x4
                ]
                obj = {
                    "bbox": bbox,
                    "bbox_mode": BoxMode.XYXY_ABS,
                    "category_id": class_id, # class id have to change
                }
                objs.append(obj)
            record["annotations"] = objs
            dataset_dicts.append(record)
        except:
            print('error')
            break

    return dataset_dicts