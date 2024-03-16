<!DOCTYPE html>
<html lang="en">
<body>
    <h1>Image Resizer</h1>
    <p>This script allows you to resize images in a folder to custom dimensions using Python and the Pillow library.</p>
    <h2>Usage</h2>
    <p>To resize images in a folder, follow these steps:</p>
    <ol>
        <li>Install Pillow library if not already installed:</li>
        <pre><code>pip install Pillow</code></pre>
        <li>Run the provided Python script <code>resize_images.py</code>.</li>
        <li>Specify the input folder path (<code>input_folder</code>) containing the images to be resized and the output folder path (<code>output_folder</code>) where the resized images will be saved within the script.</li>
        <li>Execute the script. It will resize all images in the input folder to the custom dimensions and save them in the output folder with the same filenames.</li>
    </ol>
    <h2>Custom Dimensions</h2>
    <p>The default custom dimensions are 1600 width and 1200 height. You can modify these dimensions by changing the <code>width</code> and <code>height</code> parameters in the script.</p>
    <h2>Notes</h2>
    <ul>
        <li>The script uses Pillow library for image resizing.</li>
        <li>For best results, ensure that the input images have sufficient resolution to be resized to the custom dimensions.</li>
    </ul>
    
</body>
</html>
