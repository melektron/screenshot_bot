# RPi2 Test

This folder focuses on using Raspberry Pi 2 Model B for HDMI capture via CSI.


## Setup

- Use Raspberry Pi OS Bookworm Lite (32-Bit) (note this is not what pi imager recommends for pi2)
- configure networking to liking 
- update & upgrade
- Load driver: add ```dtoverlay=tc358743``` to /boot/config.txt.
- Configure CMA: add ```cma=96M``` to end of /boot/cmdline.txt
- install the following packages:
  - vim
  - git
  - htop
  - gstreamer1.0-tools
  - gstreamer1.0-plugins-good
  - gstreamer1.0-plugins-bad
  - gstreamer1.0-plugins-ugly
  - gstreamer1.0-plugins-rtp