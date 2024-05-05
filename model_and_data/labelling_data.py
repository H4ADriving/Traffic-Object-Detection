import os
from ultralytics import YOLO
import cv2
import numpy as np
model = YOLO('yolov8n.pt')

def annotation(labels_dir, images_dir, genre_data):

    object_dict = {'person': 1, 'bicycle': 2, 
               'car': 0, 'motorcycle': 2, 'bus': 0, 
               'truck': 0, 'traffic light': 3, 
               'stop sign': 3, 'cat': 4, 'dog': 4, 'horse': 4, 
               'sheep': 4, 'cow': 4, 'elephant': 4, 'bear': 4, 
               'zebra': 4, 'giraffe': 4}
    
    images_names = os.listdir(images_dir)
    for image in images_names:
        image_path = os.path.join(images_dir, image)
        results = model(image_path)[0]
        image_height, image_width, _ = cv2.imread(image_path).shape

        detections = []
        scores = []
        class_ids = []
        for result in results.boxes.data.tolist():
            x1, y1, x2, y2, score, class_id = result
            x_centre = (x1 + x2) / (2 * image_width)
            y_centre = (y1 + y2) / (2 * image_height)
            width = (x2 - x1) / image_width
            height = (y2 - y1) / image_height
            print(f'[x_centre, y_centre, width, height] : {[x_centre, y_centre, width, height]}')

            #data to not annotate
            not_annotated_categories = []
            if genre_data == 'humans':
                not_annotated_categories.append('person')
            elif genre_data == 'motors':
                elemnt = ['bicycle', 'motorcycle']
                not_annotated_categories.extend(elemnt)
            elif genre_data == 'signs':
                elemnt = ['traffic light', 'stop sign']
                not_annotated_categories.extend(elemnt)
            elif genre_data == 'animals':
                elemnt = ['cat', 'dog', 'horse', 'sheep', 'cow', 'elephant', 'bear', 'zebra', 'giraffe']
                not_annotated_categories.extend(elemnt)
            elif genre_data == 'cars':
                elemnt = ['bus', 'truck', 'car']
                not_annotated_categories.extend(elemnt)

            if results.names[int(class_id)] in object_dict.keys() and results.names[int(class_id)] not in not_annotated_categories:
                detections.append([x_centre, y_centre, width, height])
                scores.append(score)
                class_ids.append(class_id)
        print(f'detections : {detections}')



        #verification of duplication
        filtered_detection = []
        filtered_class_id = []
        i=0
        while i < len(detections):
            duplicated = False
            for j in range(len(detections)):
                if i != j:
                    detections_rounded_i = [round(x, 1) for x in detections[i]]
                    detections_rounded_j = [round(x, 1) for x in detections[j]]
                    if detections_rounded_i == detections_rounded_j:
                        print(f'detections_rounded_i : {detections_rounded_i}')
                        duplicated = True
                        if scores[i] >= scores[j] and detections[i] not in filtered_detection:
                            filtered_detection.append(detections[i])
                            filtered_class_id.append(class_ids[i])
                        elif scores[i] < scores[j] and detections[j] not in filtered_detection:
                            filtered_detection.append(detections[j])
                            filtered_class_id.append(class_ids[j])
            if duplicated is False:
                filtered_detection.append(detections[i])
                filtered_class_id.append(class_ids[i])
            i+=1


        #l'ajoute des coordonn dans les fichier de l'annotat
        x = 0
        for box in filtered_detection:
            print(f'box : {box}')
            x_centre, y_centre, width, height = box
            class_id = filtered_class_id[x]
            x+=1
            label = os.path.splitext(image)[0] + '.txt'
            label_path = os.path.join(labels_dir, label)
            with open(label_path, 'a') as file:
                file.write('\n')
                file.write(f'{object_dict[results.names[int(class_id)]]} {x_centre} {y_centre} {width} {height}')
            print(f'{results.names[int(class_id)]} detected and added in {label} cordinates {results.names[int(class_id)]} {x_centre} {y_centre} {width} {height}')




