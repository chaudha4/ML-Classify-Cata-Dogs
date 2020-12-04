from flask import Flask, render_template
from flask import flash, request, redirect, url_for

import os
from werkzeug.utils import secure_filename

import tensorflow as tf
import numpy as np

app = Flask(__name__)

@app.route("/")
def home():
    #return "Hello, World!"
    return render_template("template.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        # file is of type - werkzeug.datastructures.FileStorage
        file = request.files['file']
        print(file)
        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file:
            filename = secure_filename(file.filename)
            #filename = os.path.join(os.getcwd(), filename)
            filename = os.path.join("static", filename)
            file.save(filename)
            img_array = normalize_image(filename)
            pred_value = make_prediction(model, img_array, verbose=True)
            
            retStr = ""
            # Dog is 1
            print("Predicted Value is ", pred_value)
            if np.round(pred_value) == 1:
                retStr = "AI thinks that it is a Dog"
            else:
                retStr = "AI thinks that it is a Cat"
            
            return render_template("result.html", result=retStr, image=filename)

    # must be GET
    return render_template("upload.html")


def restore_model(name="trained_model_96percent_accurate.h5", verbose=False):
    if not os.path.exists(name):
        raise Exception(f"Cannot find {name} model to restore.")
    
    model = tf.keras.models.load_model(name)
    
    if verbose:
        print("\n")
        print(model.summary())
        print("\n")
    
    return model

def normalize_image(file, verbose=False):
    IMG_HEIGHT = 160    # should match model
    IMG_WIDTH = 160     # should match model
    
    img = tf.keras.preprocessing.image.load_img(file, target_size=(IMG_HEIGHT, IMG_WIDTH))
    img_array = tf.keras.preprocessing.image.img_to_array(img)
    if verbose:
        print(f"Image Shape is {img_array.shape}\n")
        print("\n")
        print("Before rescaling", img_array[0][:5], sep="\n")
        print("\n")
    
    # Our Model expects values to be between 0 and 1, not 0 to 255.
    img_array = img_array / 255.0
    if verbose:
        print("After rescaling", img_array[0][:5], sep="\n")
        print("\n")
    
    # Create batch axis
    img_array = tf.expand_dims(img_array, axis=0)
    if verbose:
        print(f"After Adding Batch Image Shape is {img_array.shape}")
        print("\n")
    
    return img_array

def make_prediction(model, img_array, verbose=False):
    predictions = model.predict(img_array)
    score = predictions[0]
    if verbose:
        print_prediction(predictions)
    return score

def print_prediction(predictions):
    score = predictions[0]
    print(score)
    print(
        "This image is %.2f percent cat and %.2f percent dog."
        % (100 * (1 - score), 100 * score)
    )

model = restore_model()

if __name__ == "__main__":
    app.run(debug=True)