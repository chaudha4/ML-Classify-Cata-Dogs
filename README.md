
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/chaudha4/ML-Classify-Cats-Dogs/master)

# Machine Learning with Python - Cat and Dog Image Classifier

This Project uses TensorFlow 2.0 and Keras to create a convolutional neural network that correctly classifies images of cats and dogs with at least 63% accuracy.

If you want to use a pre-trained model, just launch the [index.ipynb](./index.ipynb) notebook.

For training the model with additional dataset, go to the [cat_dog_image_classifier.ipynb](./cat_dog_image_classifier.ipynb)

# Python environment

A Binder-compatible repo with a `requirements.txt` file.

Access this Binder at the following URL

https://mybinder.org/v2/gh/chaudha4/ML-Classify-Cats-Dogs/master


## Install pip-tools
Before you can use `pip-compile`, you need to make sure that `pip-tools` is installed.

```
pip3 install pip-tools

```

## Generate requirements.txt

[pip-compile](https://github.com/jazzband/pip-tools/) is a handy
tool for combining loosely specified dependencies with a fully frozen environment.
You write a requirements.in with just the dependencies you need
and pip-compile will generate a requirements.txt with all the strict packages and versions that would come from installing that package right now.
That way, you only need to specify what you actually know you need,
but you also get a snapshot of your environment.

```
pip-compile
```
After you run `pip-compile`, your requirements.txt should be updated and is ready for use.

## Install packages
The `requirements.txt` file should list all Python libraries that your notebooks depend on, and they will be installed using:

```
pip3 install -r requirements.txt
```

The base Binder image contains no extra dependencies, so be as
explicit as possible in defining the packages that you need. This includes
specifying explicit versions wherever possible.

If you do specify strict versions, it is important to do so for *all*
your dependencies, not just direct dependencies.
Strictly specifying only some dependencies is a recipe for environments
breaking over time.
