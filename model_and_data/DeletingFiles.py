import os
import random
import shutil

def remove_files(source_folder, nbr_of_files):

    images_folder = os.path.join(source_folder, 'images')
    labels_folder = os.path.join(source_folder, 'labels')

    images = os.listdir(images_folder)

    random_files = random.sample(images, nbr_of_files)

    x=0
    for image in random_files:
        image_to_remove = os.path.join(images_folder, image)
        os.remove(image_to_remove)
        label = os.path.splitext(image)[0] + '.txt'
        label_to_remove = os.path.join(labels_folder, label)
        os.remove(label_to_remove)
        print(x)
        x+=1
        print(f'{label} and {image}  removed')

