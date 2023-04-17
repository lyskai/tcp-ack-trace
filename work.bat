adb -s 8532355d root
adb -s 8532355d push \\10.231.194.176\Public\rx_path\1\jiaohua_perf\qca_cld3_qca6490.ko /data/qca_cld3_qca6490.ko_rx_path_1
#adb -s 8532355d shell insmod /data/cnss2.ko
#adb -s 8532355d shell "echo 1 > /sys/devices/platform/soc/b0000000.qcom,cnss-qca6490/fs_ready"
adb -s 8532355d shell insmod /data/qca_cld3_qca6490.ko_rx_path_1
sleep 1
adb -s 8532355d shell ifconfig wlan0 up
sleep 1
adb -s 8532355d shell svc wifi enable
pause
