
import numpy as np
from PIL import Image
import os

# read resolution saved by camsetup.bash 
hres: int = 1920
vres: int = 1080
#with open("/home/melektron/cap_hres", "r") as f:
#    hres = int(f.read())
#with open("/home/melektron/cap_vres", "r") as f:
#    vres = int(f.read())
    
# capture a frame. 1 frame is skipped as that first one is probably incomplete. after that, everything works fine.
os.system("v4l2-ctl --stream-mmap=3 --stream-count=1 --stream-skip=1 --stream-to=./testimg")

# read raw frame bytes
data: bytes = None
with open("./testimg", "rb") as f:
    data = f.read()
bytes_per_pixel = len(data) // (hres * vres)
print(f"Resolution: {hres}x{vres}, {bytes_per_pixel} bytes per pixel")

# reshape
data_array = np.array(list(data), dtype=np.uint8)
picture_array: np.ndarray[int] = np.reshape(data_array, (vres, hres, bytes_per_pixel))
print(picture_array.shape)

# save
img = Image.fromarray(picture_array)
img.save("./testimg.png")
