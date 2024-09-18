# Re-attempting the PDF to image conversion
from pdf2image import convert_from_path

# Path to the uploaded PDF
pdf_path = '6936946182.pdf'

# Convert PDF to images
images = convert_from_path(pdf_path)

# Save the images temporarily for OCR processing
image_paths = []
for i, image in enumerate(images):
    image_path = f'pdf_image_{i}.png'
    image.save(image_path, 'PNG')
    image_paths.append(image_path)

image_paths  # Returning the paths to the extracted images
