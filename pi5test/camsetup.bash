DEVPATH=$(realpath $1)
EDIDFILE=$(realpath $2)
echo $DEVPATH
echo $EDIDFILE

# get resolultion from edid file (extract last line)
RESSTR=$(edid-decode --native-resolution $EDIDFILE | tail -n 1 | xargs)
# split at x
IFS="x"
read -a RESARR <<< "$RESSTR"
# get hres and vres
HRES=${RESARR[0]}
VRES=${RESARR[1]}

echo $HRES
echo $VRES
# save dimensions to file so other scripts can use them
echo $HRES > ~/cap_hres
echo $VRES > ~/cap_vres

# set EDID on chip
v4l2-ctl -d $DEVPATH --set-edid=file=$EDIDFILE
v4l2-ctl -d $DEVPATH --set-dv-bt-timings query
# reset links
media-ctl -d /dev/media0 -r
# set formats
media-ctl -d /dev/media0 -l ''\''csi2'\'':4 -> '\''rp1-cfe-csi2_ch0'\'':0 [1]'
media-ctl -d /dev/media0 -V ''\''csi2'\'':0 [fmt:RGB888_1X24/'"$HRES"'x'"$VRES"' field:none colorspace:srgb]'
media-ctl -d /dev/media0 -V ''\''csi2'\'':4 [fmt:RGB888_1X24/'"$HRES"'x'"$VRES"' field:none colorspace:srgb]'
v4l2-ctl -v width=$HRES,height=$VRES,pixelformat=RGB3
