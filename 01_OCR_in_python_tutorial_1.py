from PIL import Image

im_file = 'test1.png'

im = Image.open(im_file)

print(im)
print(im.size)
im.show()
