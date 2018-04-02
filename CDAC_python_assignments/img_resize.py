from PIL import Image
import os
image="belief_reality.jpg"
img_og=Image.open(image)
width_og, height_og = img_og.size
print("Enter the resizing factor:")
factor=float(input())
width = int(width_og * factor)
height = int(height_og * factor)
img_anti = img_og.resize((width, height), Image.ANTIALIAS)
name, ext = os.path.splitext(image)
new_image= "%s%s%s" % (name, str(factor), ext)
img_anti.save(new_image)
print("resized file saved as %s" % new_image)

