from pythonImager import *
import datetime, json

with open("./config.json") as file:
    js = json.load(file)

size = js["screen-size"]
rot = js["rotation"]
mods = js["modules"]

def draw_module(img:Image, mod):
    name = mod["name"]
    match name:
        case "time":
            pos = [size[i]/100*float(j[:-1:]) if "%" in j else float(j) for i, j in enumerate(mod["pos"])]
            font = mod["font"]
            fontSize = mod["font-size"]
            fontColor = eval("COL."+mod["font-color"])
            t = str(datetime.datetime.now()).split(" ")[1].split(".")[0]
            img.text(t, pos, fontColor, font=font, fontSize=fontSize, angle=rot)
        case "image":
            im = Image()
            im.open_img(mod["path"])
            im.img = im.img[:,:,:3]
            pos = [size[i]/100*float(j[:-1:])-im.size()[i]/2 if "%" in j else float(j)-im.size()[i]/2 for i, j in enumerate(mod["pos"])]
            img.img = fusionImages(im.img, img.img, pos)
            del im

img = new_img(size, background=COL.black, name="Image Mirroir Magique")
for mod in mods[::-1]:
    draw_module(img, mod)
img.save_img("./", "output.jpg")
