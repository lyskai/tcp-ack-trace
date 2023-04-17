adb -s 8532355d root
adb -s 8532355d shell iw dev wlan0 interface add wlan2 type station
adb -s 8532355d shell ip link set wlan2 up
adb -s 8532355d shell "iw wlan2 scan | grep SSID"
adb -s 8532355d shell iw wlan2 connect AndroidAP_6366
adb -s 8532355d shell ip route add 192.168.226.0/24 dev wlan2 table local_network proto static scope link
adb -s 8532355d shell ifconfig wlan2 192.168.226.222
pause