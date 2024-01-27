# Using Pi5

As described in [v2_hardware.md](v2_hardware.md) there are a lot of problems with getting the thing to work with the pi5.
We have managed to extract frames in a somewhat manuall, dogy way.

To make it work, add a cma=96M (or more, doesn't really matter) kernel cmdlink parameter and the dtoverlay to the boot config (as described in [v2_hardware.md here](v2_hardware.md#waveshare-adapter-config)).

Setting the CMA manually will move it to a different memory location, breaking various build-in peripherals of the pi, so no propper video output, power button, RTC will work (fan might not work either, not sure).

You can run ```sudo cat /proc/iomem``` and compare the output to [memlayout_default.txt](memlayout_default.txt) to see that the usual CMA memory block (equivalent to param "cma=320M@416M") in line 6 is gone and instead the memory originally defined in line 9 now contains the extra block.

Connect adapter to MIPI 1 Port. First use the camsetup script to configure everything with 1080p30 and the correct subdevice (probably subdev2):

```bash
bash camsetup.bash /dev/v4l-subdev2 pi5test/1080p30edid
```

This might sometimes say something like "link severed". In that case it might be necessary to disconnect and reconnect the HDMI cable, then it shoudl work.

Optionally you can check the media device tree using the following commands (also described in [v2_hardware.md](v2_hardware.md) line 128):

```bash
media-ctl --print-dot > config.dot
dot -Tpng config.dot -o config.png
```

Compare the output to the provided ```config_good.png``` to check if the device tree is whats needed. There should be a subddev2 all the way at the top and a /dev/video0 present.

Then you can run the createimg.py file and it will spit out "testimg.png" which is a single frame captured.
View comments in script for details of how it works. (It expects user to be called "melektron")

