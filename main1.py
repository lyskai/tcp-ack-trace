def parse(file):
    file_handle = open(file, 'r')
    line = file_handle.readline()
    end = 0
    num = 0
    total_time = 0
    total_count = 0
    start_time = 0
    end_time = 0
    while line:
        idx = line.find("end")
        if idx == -1:
            count = int(line.split()[-1])
            total_count += count
            start = float(line.split()[3][:-1])
            if start_time == 0:
                start_time = start
            end_time = start
        else:
            end = float(line.split()[3][:-1])

        if end != 0:
            cost = end - start
            end = 0
            total_time += cost
            num += 1
        line = file_handle.readline()
    file_handle.close()
    print("total_count %d softirq num %d count/sed %f start_time %f end_time %f"%(total_count, num, num/(end_time - start_time), start_time, end_time))
    print("average time %f, average count %f count in unit %f"%(total_time/num, total_count/num, total_count/(end_time - start_time)))
    print("kpi %f Mbps"%(total_count*1460*8/(end_time - start_time)/1000000))



if __name__ == "__main__":
    parse("re.txt")
