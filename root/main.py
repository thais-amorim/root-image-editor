#!/usr/bin/python

from image_filter import *
from color_converter import *
from color_filter import *

img = read_image("images/falcon.png", "RGBA")
bg = read_image("images/bg.png", "RGBA")
final = apply_chroma_key(bg, img)
save_image("images/final.png", final)
