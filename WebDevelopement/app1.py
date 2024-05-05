from flask import Flask, request, render_template, send_file, Response
from ultralytics import YOLO
import cv2
import os
import io
from pathlib import Path
import numpy as np

app = Flask(__name__)

# Initialisation du modèle YOLO
model = YOLO(r"C:\Users\user\Desktop\ObjectDetectionProject\codes\WebDevelopement\SecondTrain.pt")

# Fonction pour la détection en temps réel
def detect_objects_realtime():
    cap = cv2.VideoCapture(0)

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        result = model.predict(frame)

        # Si result est une liste, prenez simplement le premier élément
        if isinstance(result, list):
            result = result[0]

        annotated_frame = process_detection_result_static(result, frame)

        ret, buffer = cv2.imencode('.jpg', annotated_frame)
        frame_bytes = buffer.tobytes()

        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame_bytes + b'\r\n')

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

# Route pour la page d'accueil
@app.route('/')
def index():
    return render_template('htmlcode.html')

# Route pour le flux vidéo en temps réel
@app.route('/video_feed')
def video_feed():
    return Response(detect_objects_realtime(), mimetype='multipart/x-mixed-replace; boundary=frame')

# Route pour le téléchargement d'une image et sa détection
@app.route('/upload', methods=['POST'])
def upload():
    if 'image' not in request.files:
        return 'No image uploaded', 400

    image = request.files['image']
    if image.filename == '':
        return 'No selected image', 400

    # Sauvegarde temporaire de l'image téléchargée
    image_path = 'temp_image.jpg'
    image.save(image_path)

    # Détection des objets dans l'image
    img = cv2.imread(image_path)
    results = model(img)[0]


    # Traitement des résultats de détection
    annotated_image = process_detection_result_static(results, img)

    # Emplacement pour sauvegarder l'image annotée
    save_dir = str(Path.home() / "Desktop")
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)
    
    # Sauvegarde de l'image annotée sur le bureau
    annotated_image_path = os.path.join(save_dir, 'annotated_image.jpg')
    cv2.imwrite(annotated_image_path, annotated_image)

    # Conversion de l'image annotée en bytes buffer
    image_bytes = cv2.imencode('.jpg', annotated_image)[1].tobytes()

    # Envoi de l'image annotée comme réponse
    return send_file(
        io.BytesIO(image_bytes),
        mimetype='image/jpeg'
    )

# Fonction pour traiter les résultats de détection sur une image téléchargée
def process_detection_result_static(results, img):
    for result in results.boxes.data.tolist():
        x1, y1, x2, y2, score, class_id = result
        class_label = ''
        if int(class_id) == 0:
            cv2.rectangle(img, (int(x1), int(y1)), (int(x2), int(y2)), (255, 0, 0), 2)
            class_label += 'class is : car ' + f'score is : {round(score, 2)}'
        if int(class_id) == 1:
            cv2.rectangle(img, (int(x1), int(y1)), (int(x2), int(y2)), (0, 165, 255), 2)
            class_label += 'class is : human ' + f'score is : {round(score, 2)}'
        if int(class_id) == 2:
            cv2.rectangle(img, (int(x1), int(y1)), (int(x2), int(y2)), (0, 0, 255), 2) 
            class_label += 'class is : motorcycle or bicycle ' + f'score is : {round(score, 2)}'
        if int(class_id) == 3:
            cv2.rectangle(img, (int(x1), int(y1)), (int(x2), int(y2)), (0, 255, 255), 2)  
            class_label += 'class is : Traffic sign ' + f'score is : {round(score, 2)}'
        if int(class_id) == 4:
            cv2.rectangle(img, (int(x1), int(y1)), (int(x2), int(y2)), (0, 255, 0), 2) 
            class_label += 'class is : Animal ' + f'score is : {round(score, 2)}' 
        cv2.putText(img, class_label, (int(x1), int(y1) - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
    return img


# Route pour le téléchargement de l'image annotée
@app.route('/download_result')
def download_result():
    desktop_path = str(Path.home() / "Desktop")
    annotated_image_path = os.path.join(desktop_path, 'annotated_image.jpg')
    
    if os.path.exists(annotated_image_path):
        return send_file(annotated_image_path, as_attachment=True)
    else:
        return 'File not found', 404

if __name__ == '__main__':
    app.run(debug=True)
