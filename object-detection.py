from ultralytics import YOLO
import os
from PIL import Image

# Define directories and paths
model_name = 'yolov8s.pt'  # Pre-trained model name
input_dir = 'inputs'
output_dir = 'outputs'

# Check if the input directory exists, create it if not
if not os.path.exists(input_dir):
    print(f"Input directory '{input_dir}' not found. Creating directory...")
    os.makedirs(input_dir)

# Check if the output directory exists, create it if not
if not os.path.exists(output_dir):
    print(f"Output directory '{output_dir}' not found. Creating directory...")
    os.makedirs(output_dir)

# Load the pre-trained YOLO model
print("Loading pre-trained model...")
model = YOLO(model_name)  # The library will handle the download if necessary

# Get list of image files in the input directory
image_files = [f for f in os.listdir(input_dir) if f.lower().endswith(('.png', '.jpg', '.jpeg'))]

if not image_files:
    print(f"No images found in the '{input_dir}' directory. Please add images to perform detection.")
else:
    # Process all images in the input directory
    for img_file in image_files:
        img_path = os.path.join(input_dir, img_file)
        
        # Run inference
        results = model(img_path)

        # Save results with detection boxes
        for i, result in enumerate(results):
            # Create an output path for the image
            output_img_path = os.path.join(output_dir, f"{os.path.splitext(img_file)[0]}_result_{i}.jpg")
            
            # Plot the image with detections
            result.plot(save=True, filename=output_img_path)
            
        print(f"Processed {img_file}, results saved to {output_dir}")
