// camera.js
document.addEventListener('DOMContentLoaded', function () {
    const startButton = document.getElementById('startButton');
    const stopButton = document.getElementById('stopButton');
    const videoFeed = document.getElementById('videoFeed');

    startButton.addEventListener('click', function () {
        startCamera();
    });

    stopButton.addEventListener('click', function () {
        stopCamera();
    });

    function startCamera() {
        // Mettez ici le code pour démarrer la caméra et obtenir le flux vidéo
        // Par exemple, vous pouvez utiliser la balise <video> pour afficher le flux vidéo
        // ou effectuer une requête AJAX pour obtenir le flux vidéo du serveur Flask
        // Assurez-vous que le chemin de la source vidéo correspond à votre endpoint Flask ('/video_feed')
        videoFeed.src = '/video_feed';
        startButton.style.display = 'none';
        stopButton.style.display = 'block';
    }

    function stopCamera() {
        // Mettez ici le code pour arrêter la caméra
        // Par exemple, vous pouvez arrêter la lecture du flux vidéo
        // Assurez-vous également que votre serveur Flask arrête la diffusion vidéo en temps réel
        videoFeed.src = '';
        startButton.style.display = 'block';
        stopButton.style.display = 'none';
    }
});