import imageio
import os

# Specify the folder where your images are stored
image_folder = 'logs/siren_img/imgs/'  # Update this to your folder path
images = []

# Load images (assuming they are named sequentially as image1.png, image2.png, ..., image200.png)
#for i in range(10, 800, 10): # used for dragon, fps 15
for i in range(10, 3000, 20): # used for rickroll 
    image_path = os.path.join(image_folder, f'img_s{i}.png')
    if os.path.exists(image_path):
        images.append(imageio.imread(image_path))

# Create GIF and save it
output_path = os.path.join(image_folder, 'recon_progress.gif')
imageio.mimsave(output_path, images, fps=20, loop=0)  # Adjust fps to control the speed of the GIF

print(f"GIF saved to {output_path}")
