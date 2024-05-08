# Traffic Object Detection

## Definition
This computer vision project encompasses all machine learning pipelines, from data collection to model deployment.

## Summary
The goal of this project is to develop a robust object detection model capable of identifying various entities including humans, animals, traffic signs, motorbikes, and motorcycles. Data collection involved sourcing datasets from platforms like Kaggle and RobotFlow, followed by annotation of unannotated objects. The YOLOv8 model from Ultralytics was trained on this curated dataset. The model is intended for deployment on a website. 

For more detailed information, please refer to the project report within the repository.

## Using the Project

To utilize the features developed in this project, follow these steps:

1. Clone the repository to your local machine:
    ```bash
    git clone https://github.com/your-username/your-repository.git
    ```

2. Navigate to the project directory:
    ```bash
    cd Traffic-Object-Detection
    ```

3. Ensure you have all the necessary dependencies installed. You can install them using pip:
    ```bash
    pip install -r requirements.txt
    ```

4. Before running the application, make sure to set the path to the trained model file in the `app1.py` file.

5. Once you've set the model path, you can execute the `app1.py` file to run the website:
    ```bash
    python app1.py
    ```

6. Access the website by opening your web browser and navigating to `http://localhost:5000`.

7. Explore the developed features and functionalities of the website for traffic object detection.

## Dataset Used 
You can access the dataset used for this project [here](https://drive.google.com/drive/folders/1WEnw7vNTwdTWkjRwQpLsjmhskvbgZnlt?usp=sharing).

## Data Source Websites
- **Animals Dataset:** [Kaggle - Animals Detection Images Dataset](https://www.kaggle.com/datasets/antoreepjana/animals-detection-images-dataset)
- **Motorcycles Dataset:** [RoboFlow - Motorbike and Helmet Detect](https://universe.roboflow.com/karabuk-university-hqtax/motorbike-and-helmet-detect/browse)
- **Humans Data:** [RoboFlow](https://universe.roboflow.com)
- **Traffic Signs Dataset:** [Kaggle - Jordanian Traffic Signs](https://www.kaggle.com/datasets/khaledhweij/jordanian-traffic-signs)
- **Cars Dataset:** [RoboFlow - Cars Detecting and How Many](https://universe.roboflow.com/cars-fjcrk/cars-detecting-and-how-many)

## Model
The YOLOv8 model from Ultralytics was utilized for object detection tasks in this project. You can find more information about the YOLOv5 model [here](https://docs.ultralytics.com/).

## Annexes
For additional information, including detailed datasets and project documentation, please visit the provided links.

## demonstrative video :
https://github.com/H4ADriving/Traffic-Object-Detection/assets/155930494/c2f3eff8-6271-46c6-b25b-361d753ff698
