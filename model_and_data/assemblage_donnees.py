import os 
import shutil

def assemblage(path, t_i, t_l, ts_i, ts_l, v_i, v_l):
    end_points = [d for d in os.listdir(path)]
    path1 = [os.path.join(path, point) for point in end_points]

    images = {"train": [], "test": [], "valid": []}
    labels = {"train": [], "test": [], "valid": []}

    for p in path1:
        for t in images.keys():    
            image = os.path.join(p, t, "images")
            label = os.path.join(p, t, "labels")
            images[t].append(image)
            labels[t].append(label)
    for key in images.keys():
        for image, label in zip(images[key], labels[key]):
            files_i = os.listdir(image)
            files_l = os.listdir(label)
        
            if key == "train":
                for file_i, file_l in zip(files_i, files_l):
                    old_i = os.path.join(image, file_i)
                    old_l = os.path.join(label, file_l)
                    shutil.copy(old_i, t_i)
                    shutil.copy(old_l, t_l)
                    print("moved_train")

            elif key == "test":
                for file_i, file_l in zip(files_i, files_l):
                    old_i = os.path.join(image, file_i)
                    old_l = os.path.join(label, file_l)
                    shutil.copy(old_i, ts_i)
                    shutil.copy(old_l, ts_l)
                    print("moved_test")

            elif key == "valid":
                for file_i, file_l in zip(files_i, files_l):
                    old_i = os.path.join(image, file_i)
                    old_l = os.path.join(label, file_l)
                    shutil.copy(old_i, v_i)
                    shutil.copy(old_l, v_l)
                    print("moved_valid")




