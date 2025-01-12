from PIL import Image
import os

def split_image(image_path, grid_size, output_folder):
    """
    Splits the image into grid_size x grid_size patches and saves them.

    Args:
        image_path (str): Path to the input image.
        grid_size (int): Number of rows and columns.
        output_folder (str): Directory to save the patches.
    """
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    img = Image.open(image_path)
    img_width, img_height = img.size

    # Ensure the image is large enough
    if img_width < grid_size or img_height < grid_size:
        raise ValueError("Grid size is too large for the given image dimensions.")

    patch_width = img_width / grid_size
    patch_height = img_height / grid_size

    for row in range(grid_size):
        for col in range(grid_size):
            left = col * patch_width
            upper = row * patch_height
            right = left + patch_width
            lower = upper + patch_height

            # Crop the patch
            patch = img.crop((left, upper, right, lower))
            patch_filename = f"patch_{row}_{col}.png"
            patch.save(os.path.join(output_folder, patch_filename))

    print(f"Image successfully split into {grid_size * grid_size} patches.")

if __name__ == "__main__":
    image_path = "/Users/jonathangong/Code/Repositories/Manim Projects/ViT/assets/images/fluffy.png"   # Replace with your image path
    grid_size = 5  # Number of rows and columns
    output_folder = "image_patches_5x5"

    split_image(image_path, grid_size, output_folder)
