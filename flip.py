import sys
from PIL import Image


def flip(pic):
    width, height = pic.size
    newpic = pic.copy()
    m = pic.load()
    n = newpic.load()

    for i in range(0, width):
        for j in range(0, height):
            n[i, j] = m[width-i-1, j]

    return newpic

if len(sys.argv) <= 1:
    print "missing image filename"
    sys.exit(1)
filename = sys.argv[1]
img = Image.open(filename)

img.show()
newimg = flip(img)
newimg.show()

