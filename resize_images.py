from PIL import Image
import os

def convert_to_custom_dimension(input_folder, output_folder, width=1600, height=1200):
    # Create output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Iterate through all files in the input folder
    for filename in os.listdir(input_folder):
        input_file_path = os.path.join(input_folder, filename)
        output_file_path = os.path.join(output_folder, filename)

        try:
            # Open the input image
            with Image.open(input_file_path) as image:
                # Resize the image to custom dimensions
                resized_image = image.resize((width, height))

                # Save the resized image
                resized_image.save(output_file_path)

            print(f"Conversion successful: {input_file_path} -> {output_file_path}")
        except Exception as e:
            print(f"Error converting {input_file_path}: {e}")

# Example usage:
input_folder = 'input_folder_path'
output_folder = 'output_folder_path'

convert_to_custom_dimension(input_folder, output_folder)
