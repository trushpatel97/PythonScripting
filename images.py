from PIL import Image, ImageFilter

img = Image.open('./Random Pictures/Summer Season.jpg')
img.thumbnail((400,400))
img.save('thumbnail.jpg')

'''
filtered_img = img.convert('L')
box = (100,100,400,400)
resize = filtered_img.crop(box)
resize.save("grey.png",'png')//this will crop the image


format gets the format of picture (jpg,png,etc.) size gets pixel size
mode tells if in rgb or not
dir(img) tells you the functions it has
'''