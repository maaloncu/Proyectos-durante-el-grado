from PIL import Image

im = Image.open("metro_lyon.PNG")
print(im.size)
#new_size =im.resize((400, 400))


new_height =700
new_width = int(new_height / im.height * im.width)

new_size =im.resize((new_width, new_height ))
new_size.show()

new_size.save("metro_lyon_700.png", "PNG")