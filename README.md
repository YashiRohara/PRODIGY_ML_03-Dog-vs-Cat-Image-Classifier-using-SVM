🐶🐱 Cat vs Dog Image Classifier using SVM
📌 Project Overview

This project is a Machine Learning based Image Classification system that classifies images as either Cat or Dog using the Support Vector Machine (SVM) algorithm.

The model is trained on image data after preprocessing steps like:

Image resizing
Flattening image pixels
Label encoding
Train-test splitting

The project demonstrates how traditional Machine Learning algorithms can be used for image classification without Deep Learning.

🚀 Features

✅ Image preprocessing using OpenCV
✅ Resize images to fixed dimensions (64×64)
✅ Convert images into numerical feature vectors
✅ Train an SVM classifier
✅ Predict whether an image is a Cat or Dog
✅ Visualize prediction results using Matplotlib

🛠️ Technologies Used
Technology	Purpose
Python	Programming Language
OpenCV	Image Processing
NumPy	Numerical Operations
Matplotlib	Visualization
Scikit-learn	Machine Learning

📂 Dataset Structure

Dog-Cat-Classifier-master/
│
├── Data/
│   ├── Train_Data/
│   │   ├── cat/
│   │   └── dog/
│
├── main.py
└── README.md

⚙️ Workflow

📂 Load dataset images using OpenCV
🖼️ Resize all images to 64×64
🔢 Convert images into flattened feature vectors
🏷️ Assign labels:

0 → Cat
1 → Dog

✂️ Split dataset into training & testing sets
🧠 Train SVM classifier using Scikit-learn
🔍 Predict image classes on test data
📊 Evaluate model accuracy
🖼️ Visualize prediction results using Matplotlib

📊 Model Accuracy
Model Accuracy: 54.28%

Accuracy may improve with:

More training data
Better preprocessing
Deep Learning models like CNN

🖼️ Sample Prediction Output
![SAMPLE PREDICTION](output/Figure_1.png)
![SAMPLE PREDICTION](output/Figure_3.png)
![SAMPLE PREDICTION](output/Figure_5.png)

▶️ How to Run the Project
Step 1: Install Dependencies
pip install numpy matplotlib opencv-python scikit-learn

Step 2: Run the Program
python main.py

📚 Learning Outcomes
Through this project, I learned:

Basics of Image Classification
Image preprocessing techniques
Feature extraction
Working with SVM
Model training & testing
Data visualization


🔮 Future Improvements
✨ Improve accuracy using CNN
✨ Add real-time image prediction
✨ Build GUI/Web App
✨ Use larger datasets

👩‍💻 Author
Yashi Rohara
Aspiring Software Developer passionate about:
Machine Learning
Computer Vision
Real-world AI Projects