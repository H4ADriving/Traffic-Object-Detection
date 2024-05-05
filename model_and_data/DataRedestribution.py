import os
import random
import shutil

def repartition_data(source_folder, destination_folder, nbr_of_files):

    images_folder = os.path.join(source_folder, 'images')
    labels_folder = os.path.join(source_folder, 'labels')

    images = os.listdir(images_folder)

    random_files = random.sample(images, nbr_of_files)

    x=0
    for image in random_files:
        x+=1
        image_path = os.path.join(images_folder, image)
        label = os.path.splitext(image)[0] + '.txt'
        label_path = os.path.join(labels_folder, label)

        destination_images = os.path.join(destination_folder, 'images')
        destination_labels = os.path.join(destination_folder, 'labels')

        shutil.move(image_path, destination_images)
        shutil.move(label_path, destination_labels)
        print(f"{image} moved from {image_path} to {destination_images}")
        print(f"{label} moved from {label_path} to {destination_labels}")
        print(f'iteration {x}')
        






