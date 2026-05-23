import os
import numpy as np
import matplotlib.pyplot as plt
import cv2
from sklearn.model_selection import train_test_split 
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay

# Path to dataset
cat_path = "Dog-Cat-Classifier-master/Data/Train_Data/cat"
dog_path = "Dog-Cat-Classifier-master/Data/Train_Data/dog"

'''sample_image = os.path.join(cat_path,"cat.0.jpg")

# Load image
img = cv2.imread(sample_image)

# Convert BGR to RGB
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
# Print image shape
#print("Image Shape:", img.shape)

# Resize image to 64x64
resized_img = cv2.resize(img_rgb, (64, 64))
# Print old and new shapes
print("Original Shape:", img_rgb.shape)
print("Resized Shape:", resized_img.shape)'''

X=[]
y=[]
for img_name in os.listdir(cat_path):
    img_path = os.path.join(cat_path,img_name)
    img = cv2.imread(img_path)

    if img is None:
        continue
    try:
        gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        resized_img = cv2.resize(gray_img, (64,64))
        flattened_img = resized_img.flatten()

        X.append(flattened_img)
        y.append(0)
    except Exception as e:
        print("Error processing:", img_path)

for img_name in os.listdir(dog_path):
    img_path = os.path.join(dog_path,img_name)
    img = cv2.imread(img_path)

    if img is None:
        continue
    try:
        gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        resized_img = cv2.resize(gray_img, (64,64))
        flattened_img = resized_img.flatten()

        X.append(flattened_img)
        y.append(1)
    except Exception as e:
        print("Error processing:", img_path)

X = np.array(X)
y = np.array(y)

# Print dataset information
print("Feature Shape:", X.shape)
print("Label Shape:", y.shape)

print("Unique labels:", set(y))
print("Total labels:", len(y))

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Print shapes
print("X_train shape:", X_train.shape)
print("X_test shape:", X_test.shape)

print("y_train shape:", y_train.shape)
print("y_test shape:", y_test.shape)

svm_model = SVC(kernel = "rbf")
# Train model
svm_model.fit(X_train, y_train)

print("SVM Model Trained Successfully!")

# Predictions
y_predict = svm_model.predict(X_test)

# Accuracy
accuracy = accuracy_score(y_test, y_predict)

print("Model Accuracy:", accuracy)

# Confusion Matrix
cm = confusion_matrix(y_test, y_predict)

disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=["Cat", "Dog"])

disp.plot()

plt.title("Confusion Matrix")
plt.show()

# Predict some test images
predictions = svm_model.predict(X_test)

for i in range(15):

    img = X_test[i].reshape(64, 64)

    plt.imshow(img, cmap="gray")

    predicted = "Cat" if predictions[i] == 0 else "Dog"
    actual = "Cat" if y_test[i] == 0 else "Dog"

    plt.title(f"Predicted: {predicted} | Actual: {actual}")

    plt.axis("off")
    plt.show()
'''# Display image
plt.imshow(img_rgb)
plt.title("Sample Cat Image")
plt.axis("off")
plt.show()'''