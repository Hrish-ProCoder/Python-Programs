import pyscreenshot

# im=pyscreenshot.grab(bbox=(x1,x2,y1,y2))
image = pyscreenshot.grab(bbox=(8, 8, 1200, 600))

image.show()

image.save("UserSpeci.png")
