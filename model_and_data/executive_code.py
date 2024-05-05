import os
import assemblage_donnees
import shutil
import numpy as np
from labelling_data import annotation
from DeletingFiles import remove_files
from DeleteCoruptedFiles import remove_corrupted_files 
from DataRedestribution import repartition_data
from SuppressionLineVide import SupprimeLineVide
from ultralytics import YOLO
from preprocessing import regler, genere, take, rename
from SecondModelTrain import createdata, create_detection_model, train_detection_model

#-------------------------------------------------------------------#pipeline1---------------------------------------------------

#_________changing file names and and annotation class for humans, motorcycle, sign data
carsi = {
    "1": r'C:\Users\dell\Desktop\BDIA1\Apprentissage Automatique\Project_object_detection\data\cars\train\images',
    "2": r'C:\Users\dell\Desktop\BDIA1\Apprentissage Automatique\Project_object_detection\data\cars\test\images',
    "3": r'C:\Users\dell\Desktop\BDIA1\Apprentissage Automatique\Project_object_detection\data\cars\valid\images'
}

carsl = {
    "1": r'C:\Users\dell\Desktop\BDIA1\Apprentissage Automatique\Project_object_detection\data\cars\train\labels',
    "2": r'C:\Users\dell\Desktop\BDIA1\Apprentissage Automatique\Project_object_detection\data\cars\test\labels',
    "3": r'C:\Users\dell\Desktop\BDIA1\Apprentissage Automatique\Project_object_detection\data\cars\valid\labels'
}
signsi = {
    "1": r'C:\Users\dell\Desktop\BDIA1\Apprentissage Automatique\Project_object_detection\data\signs\train\images',
    "2": r'C:\Users\dell\Desktop\BDIA1\Apprentissage Automatique\Project_object_detection\data\signs\test\images',
    "3": r'C:\Users\dell\Desktop\BDIA1\Apprentissage Automatique\Project_object_detection\data\signs\valid\images'
}

signsl = {
    "1": r'C:\Users\dell\Desktop\BDIA1\Apprentissage Automatique\Project_object_detection\data\signs\train\labels',
    "2": r'C:\Users\dell\Desktop\BDIA1\Apprentissage Automatique\Project_object_detection\data\signs\test\labels',
    "3": r'C:\Users\dell\Desktop\BDIA1\Apprentissage Automatique\Project_object_detection\data\signs\valid\labels'
}
humansi = {
    "1": r'C:\Users\dell\Desktop\BDIA1\Apprentissage Automatique\Project_object_detection\data\humans\train\images',
    "2": r'C:\Users\dell\Desktop\BDIA1\Apprentissage Automatique\Project_object_detection\data\humans\test\images',
    "3": r'C:\Users\dell\Desktop\BDIA1\Apprentissage Automatique\Project_object_detection\data\humans\valid\images'
}

humansl = {
    "1": r'C:\Users\dell\Desktop\BDIA1\Apprentissage Automatique\Project_object_detection\data\humans\train\labels',
    "2": r'C:\Users\dell\Desktop\BDIA1\Apprentissage Automatique\Project_object_detection\data\humans\test\labels',
    "3": r'C:\Users\dell\Desktop\BDIA1\Apprentissage Automatique\Project_object_detection\data\humans\valid\labels'
}

motorsi = {
    "1": r'C:\Users\dell\Desktop\BDIA1\Apprentissage Automatique\Project_object_detection\data\motors\train\images',
    "2": r'C:\Users\dell\Desktop\BDIA1\Apprentissage Automatique\Project_object_detection\data\motors\test\images',
    "3": r'C:\Users\dell\Desktop\BDIA1\Apprentissage Automatique\Project_object_detection\data\motors\valid\images'
}

motorsl = {
    "1": r'C:\Users\dell\Desktop\BDIA1\Apprentissage Automatique\Project_object_detection\data\motors\train\labels',
    "2": r'C:\Users\dell\Desktop\BDIA1\Apprentissage Automatique\Project_object_detection\data\motors\test\labels',
    "3": r'C:\Users\dell\Desktop\BDIA1\Apprentissage Automatique\Project_object_detection\data\motors\valid\labels'
}

params=[([carsi,carsl],["car",0]),([signsi,signsl],["sign",3]),([humansi,humansl],["human",1]),([motorsi,motorsl],["motor",2])]

for k in range(len(params)) :
    regler(params[k][0][0],params[k][0][1],params[k][1][0],params[k][1][1])



#_______changing file names and and annotation class for cars data
path_i=r"C:\Users\dell\Desktop\BDIA1\Apprentissage Automatique\Project_object_detection\data\cars\train\images"
path_l=r"C:\Users\dell\Desktop\BDIA1\Apprentissage Automatique\Project_object_detection\data\cars\train\labels"

path_ts_i=r"C:\Users\dell\Desktop\BDIA1\Apprentissage Automatique\Project_object_detection\data\cars\test\images"
path_ts_l=r"C:\Users\dell\Desktop\BDIA1\Apprentissage Automatique\Project_object_detection\data\cars\test\labels"
path_v_i=r"C:\Users\dell\Desktop\BDIA1\Apprentissage Automatique\Project_object_detection\data\cars\valid\images"
path_v_l=r"C:\Users\dell\Desktop\BDIA1\Apprentissage Automatique\Project_object_detection\data\cars\valid\labels"
n=3087
l=genere(path_i,n)

for i,element in enumerate(l):
    if i<1409 and element!=6473 :
        old_i=os.path.join(path_i,f"car{element}.jpg")
        shutil.move(old_i,path_ts_i)
        old_l=os.path.join(path_l,f"car{element}.txt")
        shutil.move(old_l,path_ts_l)
    else:
        old_i=os.path.join(path_i,f"car{element}.jpg")
        shutil.move(old_i,path_v_i)
        old_l=os.path.join(path_l,f"car{element}.txt")
        shutil.move(old_l,path_v_l)


#________changing stracture of animals folder, file name and class number
path1 =r"C:\Users\dell\Desktop\BDIA1\Apprentissage Automatique\Project_object_detection\data\new data\train"
path2=r"C:\Users\dell\Desktop\BDIA1\Apprentissage Automatique\Project_object_detection\data\new data\test"

path_it=r"C:\Users\dell\Desktop\BDIA1\Apprentissage Automatique\Project_object_detection\data\animals\train\images"
path_lt=r"C:\Users\dell\Desktop\BDIA1\Apprentissage Automatique\Project_object_detection\data\animals\train\labels"

path_itest=r"C:\Users\dell\Desktop\BDIA1\Apprentissage Automatique\Project_object_detection\data\animals\test\images"
path_ltest=r"C:\Users\dell\Desktop\BDIA1\Apprentissage Automatique\Project_object_detection\data\animals\test\labels"
j=0
m=rename(path1,j,path_lt,path_it)
rename(path2,m,path_ltest,path_itest, take)



#-------------------------------------------------------------------#pipeline2---------------------------------------------------
#for each object we have the bonding boxes cordinates only for it, but pictures may contains bounding boxes of other object
#and thats why we will add bounding boxes of the other object in the annotation files
def annotating(folders, annotation_func):
    for i in folders:
        sous_folder = os.path.join(r"C:\Users\user\Desktop\New_folder\couche1", i)
        sous_folders = os.listdir(sous_folder)
        for j in sous_folders:
            sous_folder1 = os.path.join(sous_folder, j)
            images_dir = os.path.join(sous_folder1, 'images')
            labels_dir = os.path.join(sous_folder1, 'labels')
            annotation_func(labels_dir, images_dir, i)
folders = os.listdir(r"C:\Users\user\Desktop\New_folder\couche1")
annotating(folders, annotation)

#after annotating the data w've notaiced that some annottion files contains empty lines 
folders = os.listdir(r"C:\Users\user\Desktop\New_folder\couche1") 
SupprimeLineVide(folders)


#l'ensemble de donnees de animaux contient beaucoup des images 
#et puisue on a limiter le nbre de donnees de chaque objet a 4000 image on doit supprimer pour attient le sample souhiatee
source_folder = r"C:\Users\user\Desktop\New_folder\piplines\couche2_annotated_problem_line_empty_solved\animals\train"
remove_files(source_folder, 457)



#-------------------------------------------------------------------#pipeline3---------------------------------------------------
#delete corrupted annotation files rised as error during training------------
names_train = ['humans142', 'humans143', 'humans144', 'humans160', 'humans161', 'humans162', 'humans208', 'humans209', 'humans210', 'humans241', 'humans242', 
               'humans243', 'humans256', 'humans257', 'humans258', 'humans259', 'humans260', 'humans261', 'humans268', 'humans269', 'humans270', 'humans289', 
               'humans2895', 'humans2896', 'humans2897', 'humans2898', 'humans2899', 'humans290', 'humans2900', 'humans2901', 'humans2902', 'humans2903', 'humans291', 
               'humans2910', 'humans2911', 'humans2912', 'humans2925', 'humans2926', 'humans2927', 'humans2928', 'humans2929', 'humans2930', 'humans2931', 'humans2932', 
               'humans2933', 'humans2937', 'humans2938', 'humans2939', 'humans2943', 'humans2944', 'humans2945', 'humans2946', 'humans2947', 'humans2948', 'humans2949', 
               'humans2950', 'humans2951', 'humans2958', 'humans2959', 'humans2960', 'humans2961', 'humans2962', 'humans2963', 'humans2964', 'humans2965', 'humans2966', 
               'humans2967', 'humans2968', 'humans2969', 'humans2970', 'humans2971', 'humans2972', 'humans2973', 'humans2974', 'humans2981', 'humans2982', 'humans2983', 
               'humans2984', 'humans2985', 'humans2986', 'humans2987', 'humans2988', 'humans2989', 'humans2993', 'humans2994', 'humans2995', 'humans2996', 'humans2997', 'humans2998', 'humans3008', 
               'humans3009', 'humans301', 'humans3010', 'humans3011', 'humans3012', 'humans3013', 'humans3014', 'humans3015', 'humans3016', 'humans3017', 'humans3018', 'humans3019', 'humans302', 
               'humans3020', 'humans3021', 'humans3022', 'humans3029', 'humans303', 'humans3030', 'humans3031', 'humans3032', 'humans3033', 'humans3034', 'humans3035', 'humans3036', 'humans3037', 
               'humans3038', 'humans3039', 'humans3040', 'humans3044', 'humans3045', 'humans3046', 'humans3050', 'humans3051', 'humans3052', 'humans3053', 'humans3054', 'humans3055', 'humans3065', 
               'humans3066', 'humans3067', 'humans3074', 'humans3075', 'humans3076', 'humans3077', 'humans3078', 'humans3079', 'humans3080', 'humans3081', 'humans3082', 'humans3086', 'humans3087', 
               'humans3088', 'humans3092', 'humans3093', 'humans3094', 'humans3095', 'humans3096', 'humans3097', 'humans3107', 'humans3108', 'humans3109', 'humans3110', 'humans3111', 'humans3112', 
               'humans3116', 'humans3117', 'humans3118', 'humans3122', 'humans3123', 'humans3124', 'humans3125', 'humans3126', 'humans3127', 'humans3131', 'humans3132', 'humans3133', 'humans3134', 
               'humans3135', 'humans3136', 'humans3140', 'humans3141', 'humans3142', 'humans3143', 'humans3144', 'humans3145', 'humans3146', 'humans3147', 'humans3148', 'humans3152', 'humans3153', 
               'humans3154', 'humans3158', 'humans3159', 'humans3160', 'humans3161', 'humans3162', 'humans3163', 'humans3167', 'humans3168', 'humans3169', 
               'humans3170', 'humans3171', 'humans3172', 'humans3197', 'humans3198', 'humans3199', 'humans3215', 'humans3216', 'humans3217', 'humans3245', 'humans3246', 'humans3247', 'humans3248', 
               'humans3249', 'humans3250', 'humans511', 'humans512', 'humans513', 'humans517', 'humans518', 'humans519', 'humans550', 'humans551', 'humans552', 'humans553', 'humans554', 'humans555', 
               'humans613', 'humans614', 'humans615', 'humans67', 'humans68', 'humans69', 'humans706', 'humans707', 'humans708', 'humans715', 'humans716', 'humans717', 'humans739', 'humans740', 'humans741', 
               'humans745', 'humans746', 'humans747', 'humans748', 'humans749', 'humans750', 'humans754', 'humans755', 'humans756', 'humans760', 'humans761', 'humans762', 'humans766', 'humans767', 'humans768', 
               'humans769', 'humans770', 'humans771', 'humans772', 'humans773', 'humans774', 'humans784', 'humans785', 'humans786', 'humans787', 'humans788', 'humans789', 'humans796', 'humans797', 'humans798', 
               'humans802', 'humans803', 'humans804', 'humans805', 'humans806', 'humans807', 'humans808', 'humans809', 'humans810', 'humans811', 'humans812', 'humans813', 'humans814', 'humans815', 'humans816', 
               'humans823', 'humans824', 'humans825', 'humans826', 'humans827', 'humans828', 'humans3353', 'humans3356', 'humans3357', 'humans3358', 'humans3362', 'humans3373', 'humans3387', 'humans3392', 'humans3393', 'humans3412', 'humans3413']
names_val = ['humans3676', 'humans3677', 'humans3679', 'humans3681', 'humans3683', 'humans3684', 
             'humans3685', 'humans3687', 'humans3689', 'humans3690', 'humans3691', 'humans3692', 'humans3693', 'humans3695', 'humans3698', 
             'humans3699', 'humans3701', 'humans3702', 'humans3703', 'humans3704', 'humans3706', 'humans3711', 'humans3715', 'humans3719', 'humans3748', 
             'humans3756', 'humans3768', 'humans3777', 'humans3784', 'humans3794', 'humans3801', 'humans3352', 
             'humans3354', 'humans3364', 'humans3399'] #we extract these names from the error
source_foulder = r"C:\Users\user\Desktop\New_folder\piplines\pipeline3\train"
remove_corrupted_files(source_foulder, names_train)
remove_corrupted_files(source_foulder, names_val)


#the data is not correctly distributed so we redistribute it in order to have 70% for training and 30% for validation---------------
source_folder = r"C:\Users\user\Desktop\New_folder\couche1\animals\test"
destination_folder = r"C:\Users\user\Desktop\New_folder\couche1\animals\valid"
repartition_data(source_folder, destination_folder, 760)


#assemblage de donnes en une folder contient tous les donnnes car on a pour chaque classe d'objet un folder 
#continet ces donnees
path = r"C:\Users\user\Desktop\New_folder\piplines\pipeline2"
t_i, t_l = r"C:\Users\user\Desktop\New_folder\piplines\pipeline3\train\images", r"C:\Users\user\Desktop\New_folder\piplines\pipeline3\train\labels"
ts_i, ts_l = r"C:\Users\user\Desktop\New_folder\piplines\pipeline3\test\images", r"C:\Users\user\Desktop\New_folder\piplines\pipeline3\test\labels"
v_i, v_l = r"C:\Users\user\Desktop\New_folder\piplines\pipeline3\valid\images", r"C:\Users\user\Desktop\New_folder\piplines\pipeline3\valid\labels"
assemblage_donnees.assemblage(path, t_i, t_l, ts_i, ts_l, v_i, v_l)



#-------------------------------------------------------------------#first training---------------------------------------------------
model = YOLO('yolov8n.yaml')  
model = YOLO('yolov8n.pt')  
model = YOLO('yolov8n.yaml').load('yolov8n.pt')  

if isinstance(model, YOLO):  
    model = model.train(data='ex1.yaml', epochs=20, imgsz=640)


#-------------------------------------------------------------pipeline4 : add anstances and retrain the model----------------------------------------
#we notice that our model detect very close humans pictures as animals and thats because we dont have close humans pictures in our data 
#we start by adding instances of close human to our dataset
#we need to annotate the data as we did previousely because the only thing annotated in this new data is humans and 
#it may contains another objects
images_dir = r"C:\Users\user\Desktop\New_folder\piplines\pipeline4\new_images\images"
labels_dir = r"C:\Users\user\Desktop\New_folder\piplines\pipeline4\new_images\labels"
annotation(labels_dir, images_dir, 'humans')

#now the data is in the pipeline4
#suppression des lignes vide
labels_dir = r"C:\Users\user\Desktop\New_folder\piplines\pipeline4\new_images\labels"
SupprimeLineVide(labels_dir)

#-----------------------------------------------------------------------------------second training------------------------
model = YOLO('yolov8n.yaml')  # build a new model from YAML
model = YOLO('FirstTrain.pt')  # load a pretrained model (recommended for training)
model = YOLO('yolov8n.yaml').load('yolov8n.pt')  # build from YAML and transfer weights

# Train the model
if isinstance(model, YOLO):  # Check if model is built from YAML
    model = model.train(data='ex1.yaml', epochs=10, imgsz=640)

model.save('SecondTrain.pt')


#-------------------------------------------------------------pipeline : Seconde Model---------------------------------------------
path = r"C:\Users\user\Desktop\New_folder\piplines\pipeline3\train\labels"
path_i = r"C:\Users\user\Desktop\New_folder\piplines\pipeline3\train\images"
vl = r"C:\Users\user\Desktop\New_folder\piplines\pipeline3\valid\labels"
vi = r"C:\Users\user\Desktop\New_folder\piplines\pipeline3\valid\images"

train_images, train_labels, _ = createdata(path, path_i)
val_images, val_labels, _ = createdata(vl, vi)
# The number of classes should be the maximum class value plus 1
num_classes = max(np.max(train_labels[0]), np.max(val_labels[0])) + 1
max_objects = max(len(labels) for labels in train_labels[0])
input_shape = train_images[0].shape
model = create_detection_model(input_shape, max_objects, num_classes)
train_detection_model(model, (train_images, train_labels), (val_images, val_labels), num_epochs=20, max_objects=max_objects)
model.save('my_model.keras')