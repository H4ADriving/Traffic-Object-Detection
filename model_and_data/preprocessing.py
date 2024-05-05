import os 
import re
import random
import shutil
from PIL import Image


def regler(directories, labels, name, num_class):
    counter = 1
    for key in directories.keys():  
        image = directories[key]
        label = labels[key]
        for imagename, labelname in zip(os.listdir(image), os.listdir(label)):
            image_name = name + str(counter) + ".jpg"  
            label_name = name + str(counter) + ".txt"    
            old_pathi = os.path.join(image, imagename) 
            new_pathi = os.path.join(image, image_name)
            old_pathl = os.path.join(label, labelname) 
            new_pathl = os.path.join(label, label_name)
            os.rename(old_pathi, new_pathi)
            os.rename(old_pathl, new_pathl)
            with open(new_pathl, "r") as fichier:
                lignes = fichier.readlines()
            for i, ligne in enumerate(lignes):
                lignes[i] = re.sub(r'^\d+', str(num_class), ligne)
            with open(new_pathl, "w") as fichier:
                fichier.writelines(lignes)
            counter += 1


def genere(path,num_samples):
    max=len(os.listdir(path))
    samples=random.sample(range(1,max+1),num_samples)
    return samples


def take(path):
    end_points=[d for d in os.listdir(path)]
    path1=[]
    for point in end_points:
        path1.append(os.path.join(path,point))
    return path1



def rename(path,j,path_l,path_i, take):
    images,labels=take(path),take(path)
    for i,p in enumerate(images):
        images[i]=os.path.join(p,'images')
    for i,p in enumerate(labels):
        labels[i]=os.path.join(p,'Label')
    for p,l in zip(images,labels) :
        for image,label in zip(os.listdir(p),os.listdir(l)):
            old_path_i=os.path.join(p,image)
            new_path_i=os.path.join(p,"animal"+str(j)+".jpg")
            old_path_l=os.path.join(l,label)
            new_path_l=os.path.join(l,"animal"+str(j)+".txt")
            os.rename(old_path_i,new_path_i)
            os.rename(old_path_l,new_path_l)
            with open(new_path_l, "r") as file:
                contenu = file.read()
            nouveau_contenu = re.sub(r"\b[a-zA-Z]+\b", "4", contenu)
            with open(new_path_l, "w") as file:
                file.write(nouveau_contenu)

            image = Image.open(new_path_i)
            largeur, hauteur = image.size
            image.close()
            with open(new_path_l,"r") as file:
                lines=file.readlines()
                contents=[]
                for line in lines :
                    cordonate = line.split()
                    _,x_min,y_min,x_max,y_max=cordonate
                    x_min,y_min,x_max,y_max=float(x_min),float(y_min),float(x_max),float(y_max)
                    xc=(x_min+x_max)/(2*largeur)
                    yc=(y_min+y_max)/(2*hauteur)
                    w=(x_max-x_min)/largeur
                    h=(y_max-y_min)/hauteur
                    content=f"{_} {xc} {yc} {w} {h} \n"
                    contents.append(content)
            with open(new_path_l,"w") as file:
                for line in contents:
                    file.write(line)
            shutil.move(new_path_i,path_i)
            shutil.move(new_path_l,path_l)
            j+=1
    return j

