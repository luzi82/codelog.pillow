import PIL.Image
import common
import os

common.reset_dir('output')

img = PIL.Image.new(mode='RGBA',size=(100,100),color=(225,0,0,255))
img.save(os.path.join('output','red.png'),'PNG')

img = PIL.Image.new(mode='RGBA',size=(100,100),color=(0,255,0,255))
img.save(os.path.join('output','green.png'),'PNG')

img = PIL.Image.new(mode='RGBA',size=(100,100),color=(0,0,255,255))
img.save(os.path.join('output','blue.png'),'PNG')

img = PIL.Image.new(mode='RGBA',size=(100,100),color=(0,255,0,127))
img.save(os.path.join('output','green50.png'),'PNG')
