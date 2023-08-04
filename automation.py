import os
from os import listdir
from PIL import Image

# cropping size
fit_size = int(input('Enter Cropping Size: '))


# open folder
os.chdir('images')

# output folder
output_folder = input('Enter Folder Name: ')
os.makedirs(output_folder, exist_ok=True)

# loop over each image
for image in os.listdir('.'):
    if image.endswith(('.png','.JPG','.jpeg')):
        im = Image.open(image)
        width , height = im.size
        if width > height:
            height = int((fit_size/height)*width)
            width = fit_size
            
        else:
            width = int((fit_size/width)*height)
            height = fit_size
            
            
        im1 = im.resize((width, height))
        im1.save(f'{output_folder}/{image}')

