# Using Pi5

As described in [v2_hardware.md](../v2_hardware.md) there are a lot of problems with getting the thing to work with the pi5.
We have managed to extract frames in a somewhat manuall, dogy way.

Connect adapter to MIPI 1 Port. First use the camsetup script to configure everything with 1080p30 and the correct subdevice (probably subdev2):

```bash
bash camsetup.bash /dev/v4l-subdev2 pi5test/1080p30edid
```

Then you can run the createimg.py file and it will spit out "testimg.png" which is a single frame captured.
View comments in script for details of how it works
