
from flask import Flask, render_template, request, jsonify
import numpy as np
from PIL import Image
from io import BytesIO
import tensorflow as tf
from flask_cors import CORS
from nutrient_analysis import analyze_nutrients
from plant_diseases import analyze_diseases

# from joblib import dump, load


app = Flask(__name__, static_url_path='/static')
CORS(app)


CNN_92_MODEL = tf.keras.models.load_model("cnnx9515.h5")
VGG_90_MODEL = tf.keras.models.load_model("VGG_90.50.h5")
DENSENET_MODEL = tf.keras.models.load_model("densenet.h5")

CLASS_NAMES = ["Corn Common Rust", "Corn Gray Leaf Spot", "Corn Healthy",
               "Potato Early Blight" , "Potato Late Blight","Potato Healthy",
              "Tomato Bacterial Spot", "Tomato Target Spot","Tomato Healthy"]

@app.route('/')
def index():
    return render_template('test.html')

# @app.route('/test')
# def test():
#     from nutrient_analysis import analyze_nutrients
#     n = request.args.get("n")
#     p = request.args.get("p")
#     k = request.args.get("k")
#     plant = request.args.get("plant")
#     print(n,p,k,plant)
#     result = analyze_nutrients(n, p, k, plant)
#     print(result)
#     return jsonify(result)

def read_file_as_image(data) -> np.ndarray:
    image = np.array(Image.open(BytesIO(data)))
    image = tf.image.resize(image, (256, 256))
    return image

@app.route('/predict', methods=['POST'])
def predict():
    file = request.files['file']
    n = request.form.get("n")
    p = request.form.get("p")
    k = request.form.get("k")
    

    image = read_file_as_image(file.read())
    img_batch = np.expand_dims(image, 0)

    #<---------------------CNN Predictions--------------------------->
    CNN_92_pred = CNN_92_MODEL.predict(img_batch)
    CNN_predicted_class = CLASS_NAMES[np.argmax(CNN_92_pred[0])]
    CNN_confidence = float(np.max(CNN_92_pred[0]))

    #<---------------------VGG Predictions--------------------------->
    VGG_90_pred = VGG_90_MODEL.predict(img_batch)
    VGG_predicted_class = CLASS_NAMES[np.argmax(VGG_90_pred[0])]
    VGG_confidence = float(np.max(VGG_90_pred[0]))


    #<---------------------NPK anal.--------------------------->
    pred_class =VGG_predicted_class.lower()
    plant = "corn" if "corn" in pred_class else "tomato" if "tomato" in pred_class else "potato"
    print(f"{n}, {p}, {k}, {plant}")
    npk_result = analyze_nutrients(int(n), int(p), int(k), plant)

    diseases_result = analyze_diseases(VGG_predicted_class)

    print(f"VGG pred -> {VGG_predicted_class} and diseases -> {diseases_result}")

    # #<---------------------DENSENET Predictions--------------------------->
    # DENSENET_pred = DENSENET_MODEL.predict(img_batch)
    # DENSENET_predicted_class = CLASS_NAMES[np.argmax(DENSENET_pred[0])]
    # DENSENET_confidence = float(np.max(DENSENET_predicted_class[0]))
    # DENSENET Predictions
    DENSENET_pred = DENSENET_MODEL.predict(img_batch)
    DENSENET_predicted_class_index = np.argmax(DENSENET_pred[0])
    DENSENET_predicted_class = CLASS_NAMES[DENSENET_predicted_class_index]
    DENSENET_confidence = float(np.max(DENSENET_pred[0]))

    


    print(f"CNN class -> {CNN_predicted_class , CNN_confidence} and VGG class-> {VGG_predicted_class , VGG_confidence}"
           +f"\n DENSENET class -> {DENSENET_predicted_class , DENSENET_confidence}")

    response_data = {
        'cnn_class': CNN_predicted_class,
        'cnn_confidence': float(CNN_confidence),
        'vgg_class': VGG_predicted_class,
        'vgg_confidence': float(VGG_confidence),
        'densenet_class': DENSENET_predicted_class,
        'densenet_confidence': float(DENSENET_confidence),
        'npk_result':npk_result,
        'diseases_result':diseases_result
    }

    return jsonify(response_data)

if __name__ == '__main__':
    app.run(debug=True)
