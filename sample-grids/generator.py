# used to generate random 10x10 pixel images for mockups

import numpy
from PIL import Image

imarray = numpy.random.rand(10,10,3) * 255
im = Image.fromarray(imarray.astype('uint8')).convert('RGBA')
im.save('random.png')