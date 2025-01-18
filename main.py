from PIL import Image, ImageEnhance, ImageFilter
import os

path = './imgs'
pathOut = 'editedImgs'


for filename in os.listdir(path):
