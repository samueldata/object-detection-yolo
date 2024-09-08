# YOLOv8 Object Detection

This project uses the YOLOv8 model for object detection. The script automatically downloads a pre-trained YOLOv8 model if it is not present and processes images to detect objects, saving the results in a designated output directory.

## Features

- **Automatic Model Download:** If the YOLOv8 pre-trained model is not found, it will be downloaded automatically.
- **Image Processing:** Detect objects in images from the input directory and save the results with bounding boxes in the output directory.
- **Directory Management:** Automatically creates necessary directories if they do not exist.

## Installation

1. **Set Up Python Environment:**

   Make sure you have Python 3.8 or later installed. It is recommended to use a virtual environment to manage dependencies. Create and activate a virtual environment using the following commands:

   ```bash
   python -m venv venv        # Create a virtual environment
   venv\Scripts\activate      # On Windows
   source venv/bin/activate  # On macOS/Linux
   ```
   
   1. **Install Required Packages:**
   
      Install the required package using pip:
   
      ```bash
      pip install -r requirements.txt
      ```
   
      The `requirements.txt` file should include:
   
      ```tex
      ultralytics
      pillow
      ```
   
   ## Usage
   
   1. **Prepare Directories:**
   
      Ensure you have an `inputs` directory with images you want to process. The output will be saved in the `outputs` directory.
   
   2. **Run the Script:**
   
      Execute the Python script to start processing images:
   
      ```bash
      python object_detection.py
      ```
   
   3. **Review Results:**
   
      Processed images with detected objects will be saved in the `outputs` directory.
   
   ## Directory Structure
   
   ```bash
   object-detection-yolo/
   │
   ├── inputs/              # Input images for object detection
   ├── outputs/             # Results with bounding boxes will be saved here
   ├── object_detection.py  # Main script to run YOLOv8
   ├── requirements.txt     # Python package dependencies
   └── README.md            # Project documentation
   ```
   
   ## Example
   
   Here’s an example of how the input and output images will look:
   
   **Input Image:**
   
   
    ![Example Input Image](https://private-user-images.githubusercontent.com/88871342/365470845-0d290544-e6fc-482c-8068-cb0911b0eb6c.jpg?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3MjU4MzU0NTIsIm5iZiI6MTcyNTgzNTE1MiwicGF0aCI6Ii84ODg3MTM0Mi8zNjU0NzA4NDUtMGQyOTA1NDQtZTZmYy00ODJjLTgwNjgtY2IwOTExYjBlYjZjLmpwZz9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNDA5MDglMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjQwOTA4VDIyMzkxMlomWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPTI5YmY0YThhMDYxMGE1NzU1MTZiZTZiOTdmY2M0MDA3MmMxYzlkMWU2NDZjMWYxYzJhODJlNTE2NjY4NjkzZWImWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0JmFjdG9yX2lkPTAma2V5X2lkPTAmcmVwb19pZD0wIn0.TT02QB63uRdlTRSPGl_xsyJQdv5smI-2ezUZt8CoqnI)

   
   
   **Output Image:**
   
   
   ![Example Output Image]([[https://user-images.githubusercontent.com/yourusername/yourimageid.jpg](https://private-user-images.githubusercontent.com/88871342/365470856-bf3c880a-b521-42dc-98f2-296e6fe99e8a.jpg?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3MjU4MzUxNTgsIm5iZiI6MTcyNTgzNDg1OCwicGF0aCI6Ii84ODg3MTM0Mi8zNjU0NzA4NTYtYmYzYzg4MGEtYjUyMS00MmRjLTk4ZjItMjk2ZTZmZTk5ZThhLmpwZz9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNDA5MDglMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjQwOTA4VDIyMzQxOFomWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPTFlOTk0YzkzZDhlYWJkNDYwYTg0YzU3YWNiMTAyNzAxOTk3Y2IwNDdiNDNmYTgyYTA1NWI0MjhiMDlkMGZkNzAmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0JmFjdG9yX2lkPTAma2V5X2lkPTAmcmVwb19pZD0wIn0.1va8WMEMAYk77pJnhoMHY73liylgRVL7qYsLUcBO3Gw)](https://private-user-images.githubusercontent.com/88871342/365470856-bf3c880a-b521-42dc-98f2-296e6fe99e8a.jpg?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3MjU4MzU0NTIsIm5iZiI6MTcyNTgzNTE1MiwicGF0aCI6Ii84ODg3MTM0Mi8zNjU0NzA4NTYtYmYzYzg4MGEtYjUyMS00MmRjLTk4ZjItMjk2ZTZmZTk5ZThhLmpwZz9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNDA5MDglMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjQwOTA4VDIyMzkxMlomWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPWVhNGJiYTM0ZDNiMjBlODYxNGY5M2NmMjYwNWM5ODQ3NGY4MjhiNjllZDIzZTQ1ZDNhYzIzMjI5MjlkZDk4NTMmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0JmFjdG9yX2lkPTAma2V5X2lkPTAmcmVwb19pZD0wIn0.QlK4pQoDd5V069fBX6YPlpeIutvApGty_g0oijU3Mq4))
   
   
   ## Troubleshooting
   
   - **No Input Images Found:** If no images are found in the `inputs` directory, make sure to place images there before running the script.
   - **Model Download Issues:** If the model download fails, ensure you have internet access and try running the script again.
   
   ## Contributing
   
   Feel free to contribute to this project by submitting issues or pull requests. Your feedback and improvements are welcome!
   
   ## License
   
   This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.
