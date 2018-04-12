# -*- coding: utf-8 -*-
"""
Created on Tue Feb 06 15:40:41 2018
Lecture 5.9/5 Image overlay (vertically, horizontally)
@author: cmonstei
https://stackoverflow.com/questions/30227466/combine-several-images-horizontally-with-python
http://www.polarlicht-vorhersage.de/goes_archive
Do not forget to install PIL as: pip install pillow
"""
#----------------------------------------------------------------------------------------------

from PIL import Image

#----------------------------------------------------------------------------------------------

def append_images(images, direction='horizontal',
                  bg_color=(255,255,255), aligment='center'):
    """
    Appends images in horizontal/vertical direction.

    Args:
        images: List of PIL images
        direction: direction of concatenation, 'horizontal' or 'vertical'
        bg_color: Background color (default: white)
        aligment: alignment mode if images need padding;
           'left', 'right', 'top', 'bottom', or 'center'

    Returns:
        Concatenated image as a new PIL image object.
    """
    widths, heights = zip(*(i.size for i in images))

    if direction=='horizontal':
        new_width = sum(widths)
        new_height = max(heights)
    else:
        new_width = max(widths)
        new_height = sum(heights)

    new_im = Image.new('RGB', (new_width, new_height), color=bg_color)


    offset = 0
    for im in images:
        if direction=='horizontal':
            y = 0
            if aligment == 'center':
                y = int((new_height - im.size[1])/2)
            elif aligment == 'bottom':
                y = new_height - im.size[1]
            new_im.paste(im, (offset, y))
            offset += im.size[0]
        else:
            x = 0
            if aligment == 'center':
                x = int((new_width - im.size[0])/2)
            elif aligment == 'right':
                x = new_width - im.size[0]
            new_im.paste(im, (x, offset))
            offset += im.size[1]

    return new_im
    
#----------------------------------------------------------------------------------------------
list_img = ['Ooty_TypeII_resized.jpg', 'goes_xray.png']
images = map(Image.open, list_img)
combo_4 = append_images(images, direction='vertical')
combo_4.save('RadioAndXray_vertical.png')
combo_4.show()

#----------------------------------------------------------------------------------------------
list_img = ['BLENSW_20180205_144500_01.fit.gz.png', 'ESSEN_20180205_144503_58.fit.gz.png', 'GLASGOW_20180205_144502_59.fit.gz.png']
images = map(Image.open, list_img)
combo_1 = append_images(images, direction='horizontal')
combo_1.save('Radio_several_horizontal.png')
combo_1.show()

#----------------------------------------------------------------------------------------------
list_img = ['BLENSW_20180205_144500_01.fit.gz.png', 'ESSEN_20180205_144503_58.fit.gz.png', 'GLASGOW_20180205_144502_59.fit.gz.png']
images = map(Image.open, list_img)
combo_2 = append_images(images, direction='vertical', aligment='top')
combo_2.save('Radio_several_vertical.png')
combo_2.show()
#----------------------------------------------------------------------------------------------
