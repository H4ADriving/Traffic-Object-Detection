import yaml



train_path=r"/content/gdrive/My Drive/pipeline3/data/train"
valid_path=r"/content/gdrive/My Drive/pipeline3/data/valid"
num_classes = 5 # modifiable par la suite 
img_size = 416 

# Créer un dictionnaire pour stocker les paramètres
data_config = {
    'train': train_path,
    'val': valid_path,
    'nc': num_classes,
    'img_size': img_size,
    'names': ["cars","humans","motors","signs","animals"]
} 

yaml_file_path = 'ex1.yaml'
with open(yaml_file_path, 'w') as file:
    yaml.dump(data_config, file)