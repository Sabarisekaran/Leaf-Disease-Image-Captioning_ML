from transformers import AutoImageProcessor, AutoModelForImageClassification
from PIL import Image
import torch

# Define the function to predict captions for plant disease images
def predict_caption(image_paths):
    images = []
    for image_path in image_paths:
        print(f"Attempting to open: {image_path}")
        i_image = Image.open(image_path)
        if i_image.mode != "RGB":
            i_image = i_image.convert(mode="RGB")
        images.append(i_image)
    
    # Load the pre-trained model for plant disease classification
    preprocessor = AutoImageProcessor.from_pretrained("your_pretrained_plant_disease_model")
    model = AutoModelForImageClassification.from_pretrained("your_pretrained_plant_disease_model")

    captions = []
    
    # Iterate over images and predict the class label (disease)
    for image in images:
        # Preprocess the image for the model
        inputs = preprocessor(images=image, return_tensors="pt")
        
        # Make predictions
        with torch.no_grad():  # Disable gradients for prediction
            outputs = model(**inputs)
        
        # Get the logits and predicted class index
        logits = outputs.logits
        predicted_class_idx = logits.argmax(-1).item()
        
        # Get the disease label (make sure your model has the correct disease classes)
        disease_class = model.config.id2label[predicted_class_idx]
        
        # Append the predicted caption (disease class)
        captions.append(disease_class)
    
    return captions

# Example usage
image_paths = ["corn.jpg", "patho.jpg"]
captions = predict_caption(image_paths)

for i, caption in enumerate(captions):
    print(f"Image {i+1}: Predicted Disease Caption: {caption}")
