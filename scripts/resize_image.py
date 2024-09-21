from PIL import Image

# print(Image.__version__)
image = Image.open('ballon2.png')
print(image.size)

WIDTH = 80
HEIGTH = 80

resized_image = image.resize((WIDTH,HEIGTH))
resized_image.save('ballon3.png')