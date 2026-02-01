from pythonImager import *
import datetime, json

with open("./config.json") as file:
    js = json.load(file)

size = js["screen-size"]
rot = js["rotation"]
mods = js["modules"]
print(mods, type(mods))

def draw_module(img:Image, mod):
    name = mod["name"]
    pos = [size[i]/100*float(j[:-1:]) if "%" in j else float(j) for i, j in enumerate(mod["pos"])]
    font = mod["font"]
    fontSize = mod["font-size"]
    fontColor = eval("COL."+mod["font-color"])
    match name:
        case "time":
            t = str(datetime.datetime.now()).split(" ")[1].split(".")[0]
            img.text(t, pos, fontColor, font=font, fontSize=fontSize, angle=rot)
    return

img = new_img(size, background=COL.black, name="Image Mirroir Magique")
for mod in mods:
    draw_module(img, mod)
img.save_img("./", "output.jpg")


img.build()


while img.is_opened():
    img.show()
