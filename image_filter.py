import os
import shutil
import datetime

# Introduction
print("Welcome to Images Folder Creater")

# Find parent path
parent_path = os.path.abspath(os.getcwd())

# List of all file formats
file_formats = [".jpg", ".jpeg", ".jpe", ".jif", ".jfif", ".jfi", ".png", ".gif", ".webp", ".tiff", ".tif", ".psd", ".raw", ".arw", ".cr2",
".nrw", ".k25", ".bmp", ".dib", ".heif", ".heic", ".ind", ".indd", ".indt", ".jp2", ".j2k", ".jpf", ".jpx", ".jpm", ".mj2"]

# Empty images list
images = []

# Check if there are images
check = False
for r, d, f in os.walk(parent_path):
    for file in f:

        # Check if file is a image
        for formats in file_formats:
            if formats in file:

                # Append image into list
                images.append(os.path.join(r, file))
                check = True
                break

    if check == False:
        print("No images in this folder")
        exit()

# Create Directory
# If directory is already there add a number to the end of it
counter = 1
directory = "images"
while True:
    try:
        path = os.path.join(parent_path, directory)
        os.mkdir(path)
        break
    except FileExistsError:
        directory = "images" + str(counter)
        counter += 1

# Go through the list of images
for image in images:

    # Get year and month of the image
    date = datetime.datetime.fromtimestamp(os.path.getctime(image))
    year = date.strftime("%Y")
    month = date.strftime("%B")

    # Check if year dir is there
    if os.path.isdir(os.path.join(path, year)):

        # Check if month dir is there
        if os.path.isdir(os.path.join(path, year, month)):

            # Copy the images into the month dir
            shutil.copyfile(image, os.path.join(path, year, month, os.path.basename(image)))

        # If month dir is not there then make a month dir and copy image into there
        else:
            os.mkdir(os.path.join(path, year, month))
            shutil.copyfile(image, os.path.join(path, year, month, os.path.basename(image)))

    # If year dir is not there then make a year and month dir and copy image into there
    else:
        os.mkdir(os.path.join(path, year))
        os.mkdir(os.path.join(path, year, month))
        shutil.copyfile(image, os.path.join(path, year, month, os.path.basename(image)))

# Tell user that "Done" and which folder all the photos where placed into
print("Done, inserted all photos into " + path + ", categorized by the year and month")