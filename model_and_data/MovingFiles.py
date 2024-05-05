import os
import random
import shutil


source_file = r"C:\Users\user\Desktop\New_folder\piplines\new_images"
destination_file_images = r"C:\Users\user\Desktop\New_folder\piplines\pipeline4\valid\images"
destination_file_labels = r"C:\Users\user\Desktop\New_folder\piplines\pipeline4\valid\labels"

def deplacer(source_file, nbr_file, destination_file_images, destination_file_labels):
    images_dir = os.path.join(source_file, 'images')
    labels_dir = os.path.join(source_file, 'labels')
    images_name = os.listdir(images_dir)
    theDest = os.listdir(destination_file_images)
    fichiers_a_deplacer = random.sample(images_name, nbr_file)
    for image in fichiers_a_deplacer:
        if image not in theDest:
            image_path = os.path.join(images_dir, image)
            label = os.path.splitext(image)[0]+'.txt'
            label_path = os.path.join(labels_dir, label)
            shutil.move(image_path, destination_file_images)
            shutil.move(label_path, destination_file_labels)
            print(f'{image} and {label} moved \n from {image_path} and {label_path} \n to {destination_file_images} and {destination_file_labels}')

#deplacer(source_file, destination_file_images, destination_file_labels)
direc = os.listdir(r"C:\Users\user\Desktop\New_folder\piplines\pipeline4\valid\images")
direc2 = os.listdir(r"C:\Users\user\Desktop\New_folder\piplines\pipeline4\train\images")
images_dir = r"C:\Users\user\Desktop\New_folder\piplines\pipeline4\train\images"
labels_dir = r"C:\Users\user\Desktop\New_folder\piplines\pipeline4\train\labels"
l = []
for i in direc:
    if i[0:11] == 'train_human':
        l.append(i)
l2 = []
for i in direc2:
    if i[0:11] == 'train_human':
        l2.append(i)
x=0
rep = False
for j in l:
    if j in l2:
        image_path = os.path.join(images_dir, j)
        label = os.path.splitext(j)[0]+'.txt'
        label_path = os.path.join(labels_dir, label)
        os.remove(image_path)
        os.remove(label_path)