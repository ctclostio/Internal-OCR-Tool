import pytesseract
from pdf2image import convert_from_path
import os

def process_file(file_path):
    # Convert PDF to images
    images = convert_from_path(file_path)

    # Create a directory to store the extracted text
    output_dir = "extracted_text"
    os.makedirs(output_dir, exist_ok=True)

    # Perform OCR on each image
    for i, image in enumerate(images):
        # Perform OCR using pytesseract
        text = pytesseract.image_to_string(image)

        # Save the extracted text to a file
        output_file = os.path.join(output_dir, f"page_{i+1}.txt")
        with open(output_file, "w") as file:
            file.write(text)

    print("OCR completed. Extracted text saved in the 'extracted_text' directory.")
