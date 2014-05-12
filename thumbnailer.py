"""A script for generating thumbnails.
A user specifies a directory which contains the images for which thumbnail has
to be generated.
Thumbnails will be stored inside directories named according to size of the
thumbnails.
Size of thumbnails to be created is passed as argument, in the following format
[(120,120),(240,240)]"""

import epeg
import os
import click
import imghdr


@click.command()
@click.option('--directory', help='Directory which contains images',
              required=True)
@click.option('--sizes', default=[(120, 120)], help='Size of the thumbnail')
def create_thumbnail(directory, sizes):
    for filename in os.listdir(directory):
        file = directory + filename
        if os.path.isfile(file) is True:
            if imghdr.what(file) is not None and imghdr.what(file) == 'jpeg':
                for size in sizes:
                    width, height = size
                    thumbnail = epeg.scale_image(file.encode('unicode-escape'),
                                                 width, height, 80)
                    pathString = "thumbnail/{0}X{1}".format(width, height)
                    dirname = os.path.join(directory, pathString)
                    thumbnailpath = "{0}/{1}".format(dirname, filename)
                    try:
                        write_thumbnail(thumbnailpath, thumbnail)
                    except IOError:
                        os.makedirs(dirname)
                        write_thumbnail(thumbnailpath, thumbnail)


def write_thumbnail(path, data):
    with open(path, 'w+') as fp:
        fp.write(data)

if __name__ == "__main__":
    create_thumbnail()