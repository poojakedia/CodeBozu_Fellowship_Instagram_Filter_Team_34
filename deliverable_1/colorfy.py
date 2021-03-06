from PIL import Image
import numpy as np

im = np.array(Image.open('/Users/poojakedia/Desktop/Bozu.png'))

im_R = im.copy()
im_R[:, :, (1, 2)] = 0
im_G = im.copy()
im_G[:, :, (0, 2)] = 0
im_B = im.copy()
im_B[:, :, (0, 1)] = 0

def redify():
    pil_img = Image.fromarray(im_R)
    pil_img.save('/Users/poojakedia/Desktop/new_Bozu.png')

redify()