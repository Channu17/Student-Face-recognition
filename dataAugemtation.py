import os
from PIL import Image, ImageEnhance

input_dir = 'dataset'
output_dir = 'augmented_dataset'  # Separate output directory to avoid overwriting


def augment_image(image_path, output_path):
    # Open the image
    img = Image.open(image_path)

    # Define augmentations
    augmentations = [
        ('flipped', img.transpose(Image.FLIP_LEFT_RIGHT)),
        ('rotated', img.rotate(45, expand=True)),  # `expand=True` to avoid cropping
        ('brightness', ImageEnhance.Brightness(img).enhance(1.5)),
    ]

    # Save augmented images
    for suffix, aug_img in augmentations:
        base_name = os.path.splitext(os.path.basename(image_path))[0]
        aug_img.save(os.path.join(output_path, f"{base_name}_{suffix}.jpg"))


# Iterate through the input directory and process images
for root, subdirs, files in os.walk(input_dir):
    for file in files:
        if file.endswith(('.jpg', '.png', '.jpeg')):
            # Get the relative path of the file
            rel_dir = os.path.relpath(root, input_dir)
            rel_output_dir = os.path.join(output_dir, rel_dir)

            # Ensure the output directory exists
            os.makedirs(rel_output_dir, exist_ok=True)

            # Augment the image
            file_path = os.path.join(root, file)
            augment_image(file_path, rel_output_dir)

            