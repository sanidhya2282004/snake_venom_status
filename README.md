# Snake Classification: Venomous or Non-Venomous
##****first convert snake_predict.jpg to .pkl using online app****
##hoe to run : first create virtual env  and then use python app.py
## Overview
This project is a deep learning-based snake classification model that identifies whether a given snake is **venomous or non-venomous** and also predicts the **snake species** from an image. The model is trained using convolutional neural networks (CNNs) and can assist researchers, herpetologists, and the general public in snake identification.

## Features
- **Detects venomous or non-venomous snakes** from images
- **Uses deep learning (CNNs) for high accuracy**
- **Trained with PyTorch and Fastai**

## Dataset
link:https://drive.google.com/drive/folders/1jJiOIh0uTIybQBdXg_lUWH1tHJGukhpV?usp=drive_link

The model is trained on a dataset containing images of various snake species labeled as venomous or non-venomous. The dataset includes:
- Multiple species of snakes
- High-quality images for training and testing
- Annotations for classification

## Model Details
- **Architecture:** CNN-based model (possibly ResNet, EfficientNet, or a custom model)
- **Framework:** PyTorch & Fastai
- **Loss Function:** Cross-entropy for classification
- **Optimizer:** Adam / SGD
- **Training:** Trained on labeled snake images



## Usage
create a virtual environment using: 
pip install virtualenv
virtualenv snake_env --python=python3.11
cd snake_env
Scripts\activate

python app.py


## Example Prediction
```python
from model import predictsnake

image_path = "test_snake.jpg"
species, is_venomous = predict_snake(image_path)
print(f"Species: {species}, Venomous: {is_venomous}")
```

## Results
- The model achieves high accuracy on test data.
- Successfully distinguishes between venomous and non-venomous species.
- Works well in real-world snake identification.

## Contributing
Feel free to contribute by improving the model, dataset, or UI.

<img width="1887" height="817" alt="image" src="https://github.com/user-attachments/assets/1d22028d-e411-4a41-ab06-a21a7b5afd71" />




