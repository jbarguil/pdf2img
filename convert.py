from pdf2image import convert_from_path
import os
import argparse

# Argument parser
parser = argparse.ArgumentParser(description="Convert PDF to images")
parser.add_argument("-i", "--input", required=True, help="Path to the input PDF file")
args = parser.parse_args()

pdf_path = args.input

print(f"Converting PDF to images: {pdf_path}")

# Converts each page to an image
images = convert_from_path(pdf_path)

# Create output dir
output_dir = "./output"
os.makedirs(output_dir, exist_ok=True)

print(f"Saving imagens in {output_dir}")

# Save images
image_paths = []
for i, image in enumerate(images):
    input_filename = os.path.splitext(os.path.basename(pdf_path))[0]
    image_path = f"{output_dir}/{input_filename}_page_{i+1}.png"
    image.save(image_path, "PNG")
    image_paths.append(image_path)

print(f"PDF converted to {len(images)} images:")
print("\n".join(image_paths))
