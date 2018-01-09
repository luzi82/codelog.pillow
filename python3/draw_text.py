import PIL.Image
import PIL.ImageFont
import PIL.ImageDraw
import common
import os

common.reset_dir('output')

for font_fn in os.listdir('font_set'):
    if not font_fn.endswith('.ttf'):
        continue
    font_name = font_fn[:-4]
    font = PIL.ImageFont.truetype(os.path.join('font_set','{}.ttf'.format(font_name)),16)
    img = PIL.Image.new('RGBA',(200,100),(0,0,0,255))
    draw = PIL.ImageDraw.Draw(img)
    draw.text((50,50),'HelloWorld',(255,255,255,255),font=font)
    img.save(os.path.join('output','{}.png'.format(font_name)),'PNG')
