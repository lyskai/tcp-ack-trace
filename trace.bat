adb -s 8532355d shell "echo 0 > /sys/kernel/tracing/tracing_on"
adb -s 8532355d shell "echo '' > /sys/kernel/tracing/set_event"
adb -s 8532355d shell "echo 11280 > /sys/kernel/tracing/buffer_size_kb"
adb -s 8532355d shell "echo '' > /sys/kernel/tracing/trace"
adb -s 8532355d shell "echo 1 > /sys/kernel/tracing/tracing_on"
timeout /t 15
adb -s 8532355d shell "echo 0 > /sys/kernel/tracing/tracing_on"
adb -s 8532355d shell "cat /sys/kernel/tracing/trace > /data/117_co2.txt"
adb -s 8532355d pull /data/117_co2.txt
pause