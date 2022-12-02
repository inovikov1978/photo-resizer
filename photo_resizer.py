'''
PHOTOS:
Photo by Josh Sorenson from Pexels
Photo by Darrel Und from Pexels
Photo by cottonbro from Pexels
'''

import pathlib
import sys,os,shutil
from PIL import Image

def get_images(path,legal_ext):
    '''
    function returning a list of files based on the legal
    extention provided by the user
    '''
    files = [str(p) for p in pathlib.Path(path).iterdir() if p.is_file()]

    image_files = [image for image in files if os.path.splitext(image)[1][1:].lower() in legal_ext]
    return image_files

def duplicate_work_files(source_list,identifier):
    '''
    procedure duplicating files to not edit the original
    The identifier is a suffix added to the file so you can separate it from
    the original
    '''
    for file in source_list:
        existing_name = file.filename
        name,ext = os.path.splitext(existing_name)
        new_name = name + identifier + ext
        shutil.copyfile(existing_name,new_name)

def filter_images(image_source,min_width,min_height):
    '''
    function that makes sure we only work on files that meed a certain criteria.
    In our case, width and height.
    '''
    #convert list items to image objects
    image_objects = [Image.open(file) for file in image_source]
    filtered_on_size = [each_image for each_image in image_objects if each_image.size[0] > min_width or each_image.size[1] > min_height]

    return filtered_on_size

def resize_images(image_source,size):
    '''
    procedure resizing photo uniformly
    '''

    for image in image_source:
        image.thumbnail(size)
        image.save(image.filename)

        #message to the user about the successful resize (optional)
        print(f'resized {image.filename} to {image.size}')


def main():
    texture_ext = ('png','jpg','tif','exr') # tuple containing our legal extentions
    images_to_process = get_images(sys.argv[1],texture_ext)
    apply_filter = filter_images(images_to_process,6000,6000) #minimum width or height for the photos
    duplicate_work_files(apply_filter,'_8k')
    resize_images(apply_filter,(2048,2048))


if __name__ ==  '__main__':
    main()
