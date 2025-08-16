from PIL import Image
new_width = 1000
new_height = 500
max_width = 1200
max_height = 50

image = Image.open("image.jpg")
new_image = image.resize((new_width, new_height))
image_copy = image.copy()
image_copy.thumbnail((max_width, max_height))
image_copy.save("resized_image.jpg")