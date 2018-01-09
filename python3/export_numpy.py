import PIL.Image
import PIL.ImageFont
import PIL.ImageDraw
import numpy as np
import os

img = PIL.Image.new(mode='RGBA',size=(100,200),color=(123,45,67,255))
data = np.asarray(img,dtype=np.uint8)

assert(data.shape==(200,100,4))
assert(data[12,34,0]==123)
assert(data[12,34,1]==45)
assert(data[12,34,2]==67)
assert(data[12,34,3]==255)

#print(np.average(data[50:60,50:60],axis=(0,1)))
m0 = np.average(data[50:60,50:60],axis=(0,1))
m1 = np.average(data[50:60,50:60],axis=(0,1))
assert(np.array_equal(m0,m1))

font = PIL.ImageFont.truetype(os.path.join('font_set','DroidSans.ttf'),16)
draw = PIL.ImageDraw.Draw(img)
draw.text((50,50),'HelloWorld',(255,255,255,255),font=font)
data = np.asarray(img,dtype=np.uint8)

m2 = np.average(data[50:60,50:60],axis=(0,1))
assert(not np.array_equal(m0,m2))
