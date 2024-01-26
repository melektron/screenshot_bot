# Version 2 hardware

## HW list

- Raspberry Pi 5
- RPi 5A 5V Power Supply ([order](https://www.amazon.de/dp/B0CM46P7MC?psc=1&ref=ppx_yo2ov_dt_b_product_details))
- WaveShare TC358743XBG HDMI-to-CSI converter ([docs](https://www.waveshare.com/wiki/HDMI_to_CSI_Adapter#Extend_Computer_Screen_to_Raspberry_Pi), [order](https://www.amazon.de/dp/B092HVP926?psc=1&ref=ppx_yo2ov_dt_b_product_details))
- Wide to Narrow CSI/DSI cable ([order](https://www.amazon.de/dp/B07CMZ9DV2?psc=1&ref=ppx_yo2ov_dt_b_product_details))
- some fancy HDMI cables and connectors
  - male-male 180° bridge ([order](https://www.amazon.de/dp/B0BWRKR6H2?psc=1&ref=ppx_yo2ov_dt_b_product_details))
  - FPC HDMI cable ([order](https://www.amazon.de/dp/B07D9FSMD7?psc=1&ref=ppx_yo2ov_dt_b_product_details))
- HDMI splitter ([order](https://www.amazon.de/dp/B09F2N17H5?psc=1&ref=ppx_yo2ov_dt_b_product_details))


## WaveShare Adapter Config

Following the instructions from the docs doesn't work, they say RPi5 is not supported.
that would be about:

```bash
# to verify that appropriate kernel modules are present
find /lib/modules/$(uname -r) -type f -name '*.ko*' | grep tc358743

# add "dtoverlay=tc358743" to boot config (in [All] section)
vim /boot/config.txt # edit...

# increase contiguous memory allocator size for large physical DMA-accessible frame buffer
# add "cma=96M" to kernel command line
vim /boot/cmdline.txt # edit...

# get some scripts to configure rpi
mkdir -p ~/Documents/screenshot_bot_install
cd ~/Documents/screenshot_bot_install
wget https://files.waveshare.com/upload/8/89/TC358743-Driver.zip
unzip TC358743-Driver.zip
cd ~/TC358743-Driver
sudo sh set_edid.sh # This executes just a v4l2-ctl command



```

Info what CMA does: https://developer.toradex.com/software/linux-resources/linux-features/contiguous-memory-allocator-cma-linux/

The following threads talk about getting such kinds of HDMI to CSI adapters to work on pi5:
- TC358743: https://forums.raspberrypi.com/viewtopic.php?t=359412
- ADV7282-M: https://forums.raspberrypi.com/viewtopic.php?p=2156480#p2156480

Both have the same problem that RPi5 using it's new RP1 chip is much more complex system which cannot simply memory map the frame buffer. In first post they talk about getting it to work, but it doesn't really work for me. Using the v4l2-ctl frame capture test command does seem to capture frames and I was able to save raw data (with the expected byte size of 3 * HRES * VRES) but couldn't use it. gstreamer didn't work at all with this error:

```
melektron@rpi5b:~/Documents/screenshot_bot_install $ gst-launch-1.0 v4l2src ! video/x-raw,width=1280,height=720,format=RGB ! capssetter caps="video/x-raw,format=BGR" ! kmssink
Setting pipeline to PAUSED ...
ERROR: from element /GstPipeline:pipeline0/GstKMSSink:kmssink0: Could not open DRM module (NULL)
Additional debug info:
../sys/kms/gstkmssink.c(1160): gst_kms_sink_start (): /GstPipeline:pipeline0/GstKMSSink:kmssink0:
reason: No such file or directory (2)
ERROR: pipeline doesn't want to preroll.
ERROR: from element /GstPipeline:pipeline0/GstKMSSink:kmssink0: GStreamer error: state change failed and some element failed to post a proper error message with the reason for the failure.
Additional debug info:
../libs/gst/base/gstbasesink.c(5878): gst_base_sink_change_state (): /GstPipeline:pipeline0/GstKMSSink:kmssink0:
Failed to start
ERROR: pipeline doesn't want to preroll.
Failed to set pipeline to PAUSED.
Setting pipeline to NULL ...
Freeing pipeline ...
```

Important to get this far in the first place is to add both the dtoverlay and cma (even though the second is not mentioned i the posts) configuration to boot config as described in above block for supplier documentation. However adding cma=96M breaks some other things such as GUI and apparently RTC stuff as there are crash logs in dmesg.

gst-launch-1.0 v4l2src ! video/x-raw-yuv,width=128,height=96,format='(fourcc)'UYVY ! videoconvert ! ffenc_h263 ! video/x-h263 ! rtph263ppay pt=96 ! udpsink host=192.168.1.1 port=5000 sync=false


```bash
sudo apt install gstreamer1.0-tools gstreamer
```



# Links

- Tried to stream with gstreamer between raspberry pis (doesn't seem to work for me) https://forums.raspberrypi.com/viewtopic.php?t=307790

