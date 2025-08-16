from PIL import Image

img = Image.open('image.jpg')

img.save('image_type output/image.png')
img.save('image_type output/image.bmp')
img.save('image_type output/image.tiff')
img.save('image_type output/image.webp')

png_img = Image.open('image_type output/image.png')
bmp_img = Image.open('image_type output/image.bmp')
tiff_img = Image.open('image_type output/image.tiff')
webp_img = Image.open('image_type output/image.webp')

png_img.show()
bmp_img.show()
tiff_img.show()
webp_img.show()
img.save("image_type output/image stored as pdf file.pdf")



