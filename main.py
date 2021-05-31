import sys
from wand.image import Image
import os

def main():
    path = sys.argv[1]
    _, _, filenames = next(os.walk(path))
    for file in filenames:
        image = Image(filename = os.path.join(path, file))
        print('File:', file)
        print('Size:', image.size)
        print("DPI:", image.resolution, image.units)
        print('Colorspace:', image.colorspace)
        print('Color depth:', image.depth, 'bits per channel')
        print('Compression:', image.compression)
        print()

if __name__ == "__main__":
    main()
